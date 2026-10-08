from pathlib import Path
from typing import Union
import pandas as pd
import geopandas as gpd
from shapely.wkt import loads


class TabularIngestor:
    """Ingests CSV or Excel files with spatial geometry columns."""

    def ingest_csv_with_wkt(self, file_path: Union[str, Path], wkt_column: str = "geometry", crs: str = "EPSG:4326") -> gpd.GeoDataFrame:
        df = pd.read_csv(file_path)
        if wkt_column not in df.columns:
            raise ValueError(f"WKT column '{wkt_column}' missing in CSV.")

        df[wkt_column] = df[wkt_column].apply(loads)
        return gpd.GeoDataFrame(df, geometry=wkt_column, crs=crs)