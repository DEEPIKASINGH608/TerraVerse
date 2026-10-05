import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from pathlib import Path
from typing import Dict, Any
from app.core.config import settings

class TabularIngestor:
    @staticmethod
    def process_tabular_file(file_path: Path, dataset_id: str) -> Dict[str, Any]:
        """Finds Latitude/Longitude column variants and converts to spatial GeoJSON."""
        df = pd.read_csv(file_path)
        cols_lower = [str(c).lower().strip() for c in df.columns]
        df.columns = cols_lower

        lat_col = next((c for c in cols_lower if "lat" in c or "y" in c), None)
        lon_col = next((c for c in cols_lower if "lon" in c or "lng" in c or "x" in c), None)

        if not lat_col or not lon_col:
            raise ValueError(f"Tabular dataset {file_path.name} lacks valid Latitude/Longitude spatial columns.")

        geometry = [Point(xy) for xy in zip(df[lon_col], df[lat_col])]
        gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")

        output_normalized_path = settings.NORMALIZED_STORAGE_DIR / f"{dataset_id}_normalized.geojson"
        gdf.to_file(output_normalized_path, driver="GeoJSON")

        return {
            "dataset_id": dataset_id,
            "feature_count": len(gdf),
            "detected_crs": "EPSG:4326",
            "normalized_file_path": str(output_normalized_path),
            "columns": list(gdf.columns)
        }