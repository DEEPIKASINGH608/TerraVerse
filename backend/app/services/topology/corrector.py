import geopandas as gpd
from backend.app.services.geospatial.geometry_utils import GeometryUtils


class TopologyCorrector:
    """Fixes invalid spatial topology in vector layers."""

    @staticmethod
    def fix_invalid_geometries(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        gdf_copy = gdf.copy()
        gdf_copy["geometry"] = gdf_copy["geometry"].apply(GeometryUtils.ensure_valid_geometry)
        return gdf_copy
