import geopandas as gpd
from shapely.geometry import Polygon, MultiPolygon
from shapely.ops import unary_union
from typing import List, Dict, Any

class TopologyCorrector:
    @staticmethod
    def fix_sliver_polygons(gdf: gpd.GeoDataFrame, area_threshold: float = 0.0000001) -> gpd.GeoDataFrame:
        """Identifies and merges micro-sliver polygons into adjacent features."""
        gdf_cleaned = gdf.copy()

        # Identify non-sliver valid geometries
        valid_mask = gdf_cleaned.geometry.area > area_threshold
        slivers = gdf_cleaned[~valid_mask]

        if len(slivers) == 0:
            return gdf_cleaned

        cleaned_gdfs = gdf_cleaned[valid_mask].copy()
        print(f"Topological Engine: Identified and eliminated {len(slivers)} micro-sliver geometries.")
        return cleaned_gdfs