from pathlib import Path
from typing import Any, Dict, Union


class RasterIngestor:
    """Ingests spatial raster files (GeoTIFF, ECW)."""

    def inspect_raster(self, file_path: Union[str, Path]) -> Dict[str, Any]:
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"Raster file missing at: {file_path}")

        return {
            "file_name": file_path.name,
            "status": "VALID",
            "format": "GeoTIFF",
        }