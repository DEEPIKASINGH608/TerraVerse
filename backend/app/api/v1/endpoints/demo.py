from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pathlib import Path
import geopandas as gpd
import json

from app.db.session import get_db
from app.db.models.parcel import CanonicalParcelModel
from app.db.models.conflict import ConflictModel
from app.services.confidence.scorer import ConfidenceScorer

router = APIRouter()

DEMO_DATA_DIR = Path("data/demo")

@router.post("/run")
def execute_one_click_demo(db: Session = Depends(get_db)):
    """Runs the Shakti Nagar harmonization demo pipeline."""
    try:
        revenue_path = DEMO_DATA_DIR / "revenue_parcels.geojson"
        municipal_path = DEMO_DATA_DIR / "municipal_parcels.geojson"
        drone_path = DEMO_DATA_DIR / "drone_parcels.geojson"

        if not revenue_path.exists():
            raise HTTPException(status_code=404, detail="Demo dataset missing. Run scripts/generate_demo_data.py first.")

        rev_gdf = gpd.read_file(revenue_path)
        mun_gdf = gpd.read_file(municipal_path)
        drone_gdf = gpd.read_file(drone_path)

        # Purge existing demo records
        db.query(CanonicalParcelModel).delete()
        db.query(ConflictModel).delete()
        db.commit()

        harmonized_parcels = []
        created_conflicts = 0

        for idx in range(min(len(rev_gdf), 50)):
            rev_row = rev_gdf.iloc[idx]
            drone_row = drone_gdf.iloc[idx]
            mun_row = mun_gdf.iloc[idx]

            khasra_no = str(rev_row.get("Khasra_No", f"10{idx}"))
            parcel_id = f"SN-P-{khasra_no}"

            # Compute confidence score
            conf_data = ConfidenceScorer.calculate_harmonization_confidence(
                geometry_agreement=0.94 if idx % 5 != 0 else 0.68,
                attribute_agreement=0.90,
                source_department="survey_department"
            )

            status = "harmonized" if conf_data["final_confidence"] >= 0.90 else "needs_review"

            # Store Canonical Parcel
            parcel = CanonicalParcelModel(
                parcel_id=parcel_id,
                geometry=drone_row.geometry.wkt,
                owner_name=str(rev_row.get("Owner_Name", "Unknown")),
                land_use=str(rev_row.get("Land_Type", "Residential")),
                area_sqm=round(drone_row.geometry.area * 10000000, 2),
                revenue_id=khasra_no,
                municipal_id=str(mun_row.get("Property_ID", f"M-{idx}")),
                survey_id=str(drone_row.get("Drone_Feature_ID", f"D-{idx}")),
                confidence_score=conf_data["final_confidence"],
                geometry_score=conf_data["geometry_score"],
                attribute_score=conf_data["attribute_score"],
                status=status,
                provenance={
                    "geometry_source": "Survey Dept Drone Imagery (2026)",
                    "attribute_source": "Revenue Records (2012)"
                }
            )
            db.add(parcel)

            # Generate intentional conflict for low-confidence items
            if status == "needs_review":
                created_conflicts += 1
                conflict = ConflictModel(
                    parcel_id=parcel_id,
                    conflict_type="BOUNDARY_GEOMETRY_DISCREPANCY",
                    severity="HIGH",
                    status="OPEN",
                    contending_sources=["Revenue Department", "Municipal Corporation"],
                    evidence_data={
                        "revenue_area": round(rev_row.geometry.area * 10000000, 2),
                        "municipal_area": round(mun_row.geometry.area * 10000000, 2)
                    },
                    ai_recommendation={
                        "action": "Adopt Drone Survey Spatial Boundary",
                        "reasoning": "Highest positional control and survey accuracy score (0.98).",
                        "confidence": conf_data["final_confidence"]
                    },
                    confidence=conf_data["final_confidence"]
                )
                db.add(conflict)

        db.commit()

        return {
            "status": "SUCCESS",
            "message": "Shakti Nagar Urban Land Harmonization Completed!",
            "parcels_processed": 50,
            "auto_harmonized": 50 - created_conflicts,
            "flagged_for_review": created_conflicts
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))