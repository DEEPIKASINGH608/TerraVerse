import pyproj
import geopandas as gpd
from app.core.config import settings

class CRSEngine:
    @staticmethod
    def verify_and_transform(gdf: gpd.GeoDataFrame, target_crs: str = settings.TARGET_CRS) -> gpd.GeoDataFrame:
        """Transforms GeoDataFrame safely to target projection."""
        if gdf.crs is None:
            gdf.set_crs("EPSG:4326", inplace=True)

        if gdf.crs.to_string() != target_crs:
            gdf = gdf.to_crs(target_crs)

        return gdf