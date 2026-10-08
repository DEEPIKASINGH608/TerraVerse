from pathlib import Path
from typing import Union
import geopandas as gpd


class GeoJSONExporter:
    """Exports spatial layers to GeoJSON format."""

    @staticmethod
    def export(gdf: gpd.GeoDataFrame, output_path: Union[str, Path]) -> Path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        gdf.to_file(output_path, driver="GeoJSON")
        return output_path
