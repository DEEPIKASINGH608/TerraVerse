import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import json
from src.db.session import engine, SessionLocal, Base
from src.db.models import Parcel

def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    if db.query(Parcel).first():
        print("Database already contains data. Skipping seed.")
        db.close()
        return

    demo_data_path = Path(__file__).resolve().parent.parent / "data" / "processed" / "shakti_nagar_demo.geojson"

    if demo_data_path.exists():
        with open(demo_data_path, "r") as f:
            data = json.load(f)

        for feature in data.get("features", []):
            props = feature.get("properties", {})
            geom = json.dumps(feature.get("geometry", {}))

            parcel = Parcel(
                parcel_id=props.get("parcel_id", "UNKNOWN"),
                owner_name=props.get("owner_name", "Unknown"),
                area_sqm=props.get("area_sqm", 0.0),
                confidence_score=props.get("confidence", 0.90),
                geometry=geom
            )
            db.add(parcel)

        db.commit()
        print(f"Database seeded with {len(data.get('features', []))} parcels successfully.")
    else:
        print(f"Seed file not found at: {demo_data_path}")

    db.close()

if __name__ == "__main__":
    seed()