from typing import Any, Dict, List, Optional
from pydantic import BaseModel


class HarmonizationRequest(BaseModel):
    dataset_ids: List[int]
    target_crs: str = "EPSG:4326"
    geometry_precision_meters: float = 0.05
    attribute_mapping_rules: Optional[Dict[str, str]] = None


class HarmonizationResponse(BaseModel):
    status: str
    total_processed: int
    auto_harmonized: int
    conflicts_flagged: int
    harmonized_parcel_ids: List[str]
    job_details: Optional[Dict[str, Any]] = None