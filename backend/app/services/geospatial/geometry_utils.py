from shapely.geometry import base, MultiPolygon, Polygon


class GeometryUtils:
    """Utility class for standardizing spatial geometries."""

    @staticmethod
    def ensure_valid_geometry(geom: base.BaseGeometry) -> base.BaseGeometry:
        """Fixes self-intersections or invalid polygon structures using buffer(0)."""
        if geom is None:
            return None
        if not geom.is_valid:
            return geom.buffer(0)
        return geom

    @staticmethod
    def calculate_intersection_over_union(geom_a: base.BaseGeometry, geom_b: base.BaseGeometry) -> float:
        """Computes IoU overlap metric between two geometries."""
        if geom_a is None or geom_b is None or not geom_a.intersects(geom_b):
            return 0.0

        intersection = geom_a.intersection(geom_b).area
        union = geom_a.union(geom_b).area

        return (intersection / union) if union > 0 else 0.0