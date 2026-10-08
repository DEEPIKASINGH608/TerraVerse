from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, ConfigDict


class CanonicalParcelBase(BaseModel):
    parcel_id: str
    geometry: str
    owner_name: Optional[str] = None
    land_use: Optional[str] = None
    area_sqm: Optional[float] = None
    revenue_id: Optional[str] = None
    municipal_id: Optional[str] = None
    survey_id: Optional[str] = None
    status: str = "harmonized"
    provenance: Optional[Dict[str, Any]] = None


class CanonicalParcelCreate(CanonicalParcelBase):
    confidence_score: float
    geometry_score: Optional[float] = None
    attribute_score: Optional[float] = None


class CanonicalParcelResponse(CanonicalParcelBase):
    id: int
    confidence_score: float
    geometry_score: Optional[float] = None
    attribute_score: Optional[float] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)