import logging
from typing import Any, Dict, List
import geopandas as gpd

from backend.app.services.conflict.rules import ConflictRulesEngine

logger = logging.getLogger("terraverse")


class ConflictDetector:
    """Scans multi-source land record datasets for spatial overlaps and ownership mismatches."""

    def detect_spatial_conflicts(self, gdf_a: gpd.GeoDataFrame, gdf_b: gpd.GeoDataFrame) -> List[Dict[str, Any]]:
        """Identifies boundary spatial overlaps exceeding tolerance thresholds."""
        logger.info("Executing spatial conflict detection...")
        conflicts = []

        if gdf_a.crs != gdf_b.crs:
            gdf_b = gdf_b.to_crs(gdf_a.crs)

        sindex_b = gdf_b.sindex

        for idx_a, row_a in gdf_a.iterrows():
            geom_a = row_a.geometry
            possible_matches_index = list(sindex_b.intersection(geom_a.bounds))
            possible_matches = gdf_b.iloc[possible_matches_index]

            for idx_b, row_b in possible_matches.iterrows():
                geom_b = row_b.geometry
                if geom_a.intersects(geom_b):
                    intersection_area = geom_a.intersection(geom_b).area
                    min_area = min(geom_a.area, geom_b.area)
                    overlap_ratio = (intersection_area / min_area) if min_area > 0 else 0

                    if 0.05 < overlap_ratio < 0.95:
                        eval_res = ConflictRulesEngine.evaluate_area_discrepancy(geom_a.area, geom_b.area)
                        conflicts.append({
                            "parcel_id_a": row_a.get("parcel_id", str(idx_a)),
                            "parcel_id_b": row_b.get("parcel_id", str(idx_b)),
                            "overlap_ratio": round(overlap_ratio, 4),
                            "conflict_type": "BOUNDARY_OVERLAP",
                            "severity": eval_res["severity"],
                        })

        logger.info(f"Conflict detection finished. Found {len(conflicts)} conflict items.")
        return conflicts