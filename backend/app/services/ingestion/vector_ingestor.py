import geopandas as gpd
import json
from pathlib import Path
from typing import Dict, Any
from app.core.config import settings

class VectorIngestor:
    @staticmethod
    def process_vector_file(file_path: Path, dataset_id: str) -> Dict[str, Any]:
        """In-memory spatial load and normalization to GeoJSON contract."""
        try:
            gdf = gpd.read_file(file_path)

            detected_crs = str(gdf.crs) if gdf.crs else "EPSG:4326"

            if gdf.crs and gdf.crs.to_string() != settings.TARGET_CRS:
                gdf = gdf.to_crs(settings.TARGET_CRS)

            gdf.columns = [str(col).lower().strip() for col in gdf.columns]

            output_normalized_path = settings.NORMALIZED_STORAGE_DIR / f"{dataset_id}_normalized.geojson"
            gdf.to_file(output_normalized_path, driver="GeoJSON")

            return {
                "dataset_id": dataset_id,
                "feature_count": len(gdf),
                "detected_crs": detected_crs,
                "normalized_file_path": str(output_normalized_path),
                "columns": list(gdf.columns)
            }
        except Exception as e:
            raise RuntimeError(f"Vector Ingestion Failure for {file_path.name}: {str(e)}")