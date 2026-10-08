from typing import Dict, Any
from backend.app.services.geospatial.geometry_utils import GeometryUtils


class FeatureEngineer:
    """Engineers similarity features between candidate record pairs."""

    @staticmethod
    def compute_pair_features(row_a: Any, row_b: Any) -> Dict[str, float]:
        iou = GeometryUtils.calculate_intersection_over_union(row_a.geometry, row_b.geometry)

        area_a = row_a.geometry.area
        area_b = row_b.geometry.area
        area_ratio = (min(area_a, area_b) / max(area_a, area_b)) if max(area_a, area_b) > 0 else 0.0

        return {
            "iou": round(iou, 4),
            "area_ratio": round(area_ratio, 4),
        }