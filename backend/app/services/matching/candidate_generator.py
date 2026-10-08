from typing import List, Tuple
import geopandas as gpd


class SpatialCandidateGenerator:
    """Generates candidate matching pairs using bounding box index bounds."""

    @staticmethod
    def generate_candidate_pairs(gdf_a: gpd.GeoDataFrame, gdf_b: gpd.GeoDataFrame) -> List[Tuple[int, int]]:
        pairs = []
        sindex_b = gdf_b.sindex

        for idx_a, geom_a in enumerate(gdf_a.geometry):
            possible_matches = list(sindex_b.intersection(geom_a.bounds))
            for idx_b in possible_matches:
                pairs.append((idx_a, idx_b))

        return pairs