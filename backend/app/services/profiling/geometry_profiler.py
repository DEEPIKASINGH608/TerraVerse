import geopandas as gpd


class GeometryProfiler:
    """Profiles spatial layers for invalid geometries, empty bounds, and feature types."""

    @staticmethod
    def profile(gdf: gpd.GeoDataFrame):
        invalid_count = (~gdf.is_valid).sum()
        empty_count = gdf.is_empty.sum()

        return {
            "total_features": len(gdf),
            "invalid_geometries": int(invalid_count),
            "empty_geometries": int(empty_count),
            "geometry_types": gdf.geometry.type.value_counts().to_dict(),
        }