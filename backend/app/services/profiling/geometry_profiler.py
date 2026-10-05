import geopandas as gpd
from typing import Dict, Any

class GeometryProfiler:
    @staticmethod
    def profile_geometry(file_path: str) -> Dict[str, Any]:
        gdf = gpd.read_file(file_path)
        total_features = len(gdf)

        if total_features == 0:
            return {"validity_pct": 0.0, "overlap_count": 0, "sliver_count": 0}

        # 1. Geometry Validity
        valid_series = gdf.is_valid
        valid_count = int(valid_series.sum())
        validity_pct = round((valid_count / total_features) * 100, 2)

        # 2. Overlap & Sliver Detection
        sliver_count = 0
        for geom in gdf.geometry:
            if geom and geom.geom_type in ['Polygon', 'MultiPolygon']:
                perimeter = geom.length
                area = geom.area
                if area > 0 and (perimeter ** 2 / area) > 100:  
                    sliver_count += 1

        return {
            "total_features": total_features,
            "valid_features": valid_count,
            "validity_pct": validity_pct,
            "sliver_count": sliver_count,
            "bounds": list(gdf.total_bounds)
        }