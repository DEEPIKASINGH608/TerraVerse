from pathlib import Path
from typing import Union
import geopandas as gpd


class GeoPackageExporter:
    """Exports spatial layers to OGC GeoPackage format."""

    @staticmethod
    def export(gdf: gpd.GeoDataFrame, output_path: Union[str, Path], layer_name: str = "parcels") -> Path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        gdf.to_file(output_path, driver="GPKG", layer=layer_name)
        return output_path