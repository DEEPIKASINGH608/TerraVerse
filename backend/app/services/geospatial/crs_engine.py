import logging
import geopandas as gpd

logger = logging.getLogger("terraverse")


class CRSEngine:
    """Handles Coordinate Reference System (CRS) transformations."""

    @staticmethod
    def reproject(gdf: gpd.GeoDataFrame, target_crs: str = "EPSG:4326") -> gpd.GeoDataFrame:
        """Reprojects GeoDataFrame to target CRS safely."""
        if gdf.crs is None:
            logger.warning(f"GeoDataFrame lacks CRS. Assigning default target '{target_crs}'.")
            gdf.set_crs(target_crs, inplace=True)
            return gdf

        if gdf.crs.to_string().upper() != target_crs.upper():
            logger.info(f"Reprojecting layer from '{gdf.crs}' to '{target_crs}'.")
            return gdf.to_crs(target_crs)

        return gdf