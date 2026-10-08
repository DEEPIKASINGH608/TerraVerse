from shapely.geometry import Polygon
from backend.app.utils.geometry_utils import clean_geometry, calculate_area


def test_self_intersecting_polygon_repair():
    """Validates auto-correction of invalid self-intersecting geometries."""
    # Bowtie self-intersecting polygon
    invalid_poly = Polygon([(0, 0), (0, 2), (2, 0), (2, 2), (0, 0)])
    assert invalid_poly.is_valid is False

    cleaned = clean_geometry(invalid_poly)
    assert cleaned.is_valid is True


def test_area_calculation(sample_polygon_a):
    """Validates polygon surface area calculation."""
    area = calculate_area(sample_polygon_a)
    assert area > 0.0