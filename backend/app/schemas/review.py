from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, ConfigDict


class ReviewTaskBase(BaseModel):
    conflict_id: int
    parcel_id: str
    assigned_to: Optional[str] = None
    status: str = "PENDING"
    resolution_notes: Optional[str] = None
    overridden_data: Optional[Dict[str, Any]] = None


class ReviewTaskCreate(ReviewTaskBase):
    pass


class ReviewTaskAction(BaseModel):
    action: str  # "APPROVE", "REJECT", "OVERRIDE"
    resolver_id: str
    notes: Optional[str] = None
    overridden_attributes: Optional[Dict[str, Any]] = None


class ReviewTaskResponse(ReviewTaskBase):
    id: int
    created_at: datetime
    resolved_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)