import geopandas as gpd


class SchemaProfiler:
    """Profiles dataset schemas for null values and column data types."""

    @staticmethod
    def profile(gdf: gpd.GeoDataFrame):
        null_counts = gdf.isnull().sum().to_dict()
        data_types = {col: str(dtype) for col, dtype in gdf.dtypes.items()}

        return {
            "column_count": len(gdf.columns),
            "null_counts": null_counts,
            "data_types": data_types,
        }