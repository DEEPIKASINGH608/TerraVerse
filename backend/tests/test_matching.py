from backend.app.services.geospatial.geometry_utils import GeometryUtils


def test_intersection_over_union(sample_polygon_a, sample_polygon_b):
    """Validates IoU spatial similarity metric calculation."""
    iou = GeometryUtils.calculate_intersection_over_union(sample_polygon_a, sample_polygon_b)
    assert 0.0 < iou < 1.0

    identical_iou = GeometryUtils.calculate_intersection_over_union(sample_polygon_a, sample_polygon_a)
    assert round(identical_iou, 2) == 1.0