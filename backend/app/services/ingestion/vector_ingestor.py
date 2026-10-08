from pathlib import Path
from typing import Union
import geopandas as gpd
from backend.app.services.ingestion.base import BaseIngestor


class VectorIngestor(BaseIngestor):
    """Ingests vector formats (GeoJSON, Shapefile, KML, GeoPackage)."""

    def ingest(self, file_path: Union[str, Path]) -> gpd.GeoDataFrame:
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"Vector dataset missing at: {file_path}")
        return gpd.read_file(file_path)
