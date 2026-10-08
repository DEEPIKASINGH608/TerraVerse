from abc import ABC, abstractmethod
from pathlib import Path
from typing import Union
import geopandas as gpd


class BaseIngestor(ABC):
    """Abstract base class for data ingestion engines."""

    @abstractmethod
    def ingest(self, file_path: Union[str, Path]) -> gpd.GeoDataFrame:
        pass
