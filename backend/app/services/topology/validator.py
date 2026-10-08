import geopandas as gpd


class TopologyValidator:
    """Validates spatial layer topology rules (overlaps, gaps, self-intersections)."""

    @staticmethod
    def find_overlapping_polygons(gdf: gpd.GeoDataFrame) -> int:
        overlap_count = 0
        sindex = gdf.sindex

        for idx, geom in enumerate(gdf.geometry):
            possible_matches = list(sindex.intersection(geom.bounds))
            for p_idx in possible_matches:
                if idx < p_idx and geom.intersects(gdf.geometry.iloc[p_idx]):
                    intersection = geom.intersection(gdf.geometry.iloc[p_idx])
                    if intersection.area > 0.000001:
                        overlap_count += 1

        return overlap_count