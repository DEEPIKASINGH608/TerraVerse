from pathlib import Path
from typing import Union
import geopandas as gpd


class ShapefileExporter:
    """Exports spatial layers to ESRI Shapefile format."""

    @staticmethod
    def export(gdf: gpd.GeoDataFrame, output_path: Union[str, Path]) -> Path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        gdf.to_file(output_path, driver="ESRI Shapefile")
        return output_path