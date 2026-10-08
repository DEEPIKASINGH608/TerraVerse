from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, ConfigDict


class DatasetBase(BaseModel):
    name: str
    department: str
    format: str
    crs: str = "EPSG:4326"
    metadata_info: Optional[Dict[str, Any]] = None


class DatasetCreate(DatasetBase):
    file_path: str
    feature_count: Optional[int] = 0


class DatasetResponse(DatasetBase):
    id: int
    file_path: str
    feature_count: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
