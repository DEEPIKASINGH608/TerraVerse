import geopandas as gpd
from backend.app.services.topology.validator import TopologyValidator


def test_topology_overlap_detection(sample_polygon_a, sample_polygon_b):
    """Validates detecting spatial overlaps across layer features."""
    gdf = gpd.GeoDataFrame(
        {"parcel_id": ["A", "B"]},
        geometry=[sample_polygon_a, sample_polygon_b],
        crs="EPSG:4326",
    )

    overlaps = TopologyValidator.find_overlapping_polygons(gdf)
    assert overlaps >= 1