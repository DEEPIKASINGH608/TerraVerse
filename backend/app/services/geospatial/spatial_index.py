from typing import List
import geopandas as gpd


class SpatialIndexManager:
    """Provides spatial indexing wrappers using PyGEOS / R-tree integration."""

    @staticmethod
    def query_bbox(gdf: gpd.GeoDataFrame, minx: float, miny: float, maxx: float, maxy: float) -> gpd.GeoDataFrame:
        """Queries GeoDataFrame features intersecting specified bounding box."""
        sindex = gdf.sindex
        possible_matches_index = list(sindex.intersection((minx, miny, maxx, maxy)))
        return gdf.iloc[possible_matches_index]