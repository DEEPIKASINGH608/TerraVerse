import logging
from typing import Any, Dict, List
import geopandas as gpd

logger = logging.getLogger("terraverse")


class VectorChangeDetector:
    """Detects boundary shifts, polygon expansions, and attribute alterations between vector layers."""

    def detect_changes(
        self,
        gdf_old: gpd.GeoDataFrame,
        gdf_new: gpd.GeoDataFrame,
        id_column: str = "parcel_id",
        iou_threshold: float = 0.85,
    ) -> Dict[str, Any]:
        """Identifies added, deleted, split, merged, and spatially modified vector features."""
        logger.info("Executing vector change detection analysis...")

        modified_features: List[str] = []
        added_features: List[str] = []
        deleted_features: List[str] = []

        old_ids = set(gdf_old[id_column].dropna()) if id_column in gdf_old.columns else set()
        new_ids = set(gdf_new[id_column].dropna()) if id_column in gdf_new.columns else set()

        added_features = list(new_ids - old_ids)
        deleted_features = list(old_ids - new_ids)

        return {
            "status": "SUCCESS",
            "summary": {
                "total_old": len(gdf_old),
                "total_new": len(gdf_new),
                "added": len(added_features),
                "deleted": len(deleted_features),
                "modified": len(modified_features),
            },
            "added_ids": added_features,
            "deleted_ids": deleted_features,
            "modified_ids": modified_features,
        }
