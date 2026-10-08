import geopandas as gpd
from backend.app.services.profiling.geometry_profiler import GeometryProfiler
from backend.app.services.profiling.scheme_profiler import SchemaProfiler


class SpatialQualityProfiler:
    """Runs comprehensive spatial data quality profiling."""

    @staticmethod
    def generate_full_profile(gdf: gpd.GeoDataFrame):
        return {
            "geometry_profile": GeometryProfiler.profile(gdf),
            "schema_profile": SchemaProfiler.profile(gdf),
            "crs": str(gdf.crs),
        }