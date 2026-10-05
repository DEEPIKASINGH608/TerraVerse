from shapely.geometry import Polygon
import numpy as np

class FeatureEngineering:
    @staticmethod
    def compute_pairwise_metrics(poly_a: Polygon, poly_b: Polygon) -> dict:
        """Derives invariant spatial metrics between candidate polygons."""
        if not poly_a.intersects(poly_b):
            return {
                "iou": 0.0,
                "area_ratio": 0.0,
                "centroid_dist": 999.0,
                "hausdorff_dist": 999.0
            }

        intersection = poly_a.intersection(poly_b).area
        union = poly_a.union(poly_b).area
        iou = intersection / union if union > 0 else 0.0

        area_a = poly_a.area
        area_b = poly_b.area
        area_ratio = min(area_a, area_b) / max(area_a, area_b) if max(area_a, area_b) > 0 else 0.0

        centroid_dist = poly_a.centroid.distance(poly_b.centroid)

        hausdorff_dist = poly_a.hausdorff_distance(poly_b)

        return {
            "iou": float(iou),
            "area_ratio": float(area_ratio),
            "centroid_dist": float(centroid_dist),
            "hausdorff_dist": float(hausdorff_dist)
        }