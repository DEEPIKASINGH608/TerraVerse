import geopandas as gpd
from shapely.geometry import Point
from backend.app.services.geospatial.crs_engine import CRSEngine


def test_crs_reprojection():
    """Validates reprojecting a layer from WGS84 (EPSG:4326) to Web Mercator (EPSG:3857)."""
    gdf = gpd.GeoDataFrame(
        {"id": [1]},
        geometry=[Point(77.100, 28.600)],
        crs="EPSG:4326",
    )

    reprojected = CRSEngine.reproject(gdf, target_crs="EPSG:3857")
    assert reprojected.crs.to_string().upper() == "EPSG:3857"