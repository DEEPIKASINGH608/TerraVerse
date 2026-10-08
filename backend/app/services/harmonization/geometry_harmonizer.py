import geopandas as gpd
from backend.app.services.geospatial.geometry_utils import GeometryUtils


class GeometryHarmonizer:
    """Standardizes geometries across multiple spatial layers."""

    @staticmethod
    def snap_and_clean_boundaries(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        """Applies geometry validation across all layer features."""
        gdf_copy = gdf.copy()
        gdf_copy["geometry"] = gdf_copy["geometry"].apply(GeometryUtils.ensure_valid_geometry)
        return gdf_copy