from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, ConfigDict


class ConflictBase(BaseModel):
    parcel_id: str
    conflict_type: str
    severity: str = "MEDIUM"
    status: str = "OPEN"
    contending_sources: Optional[List[str]] = None
    evidence_data: Optional[Dict[str, Any]] = None
    ai_recommendation: Optional[Dict[str, Any]] = None
    confidence: Optional[float] = None


class ConflictCreate(ConflictBase):
    pass


class ConflictUpdate(BaseModel):
    severity: Optional[str] = None
    status: Optional[str] = None
    ai_recommendation: Optional[Dict[str, Any]] = None
    confidence: Optional[float] = None


class ConflictResponse(ConflictBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
