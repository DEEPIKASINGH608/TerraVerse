from sqlalchemy import Column, String, Float, DateTime, JSON, Text
from datetime import datetime, timezone
import uuid
from app.db.session import Base

class ConflictModel(Base):
    __tablename__ = "geometry_conflicts"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    parcel_id = Column(String, index=True, nullable=False)
    conflict_type = Column(String, nullable=False)
    severity = Column(String, nullable=False)
    status = Column(String, default="OPEN")         

    contending_sources = Column(JSON, nullable=False)
    evidence_data = Column(JSON, nullable=False)
    ai_recommendation = Column(JSON, nullable=False)
    confidence = Column(Float, default=0.0)

    resolution_notes = Column(Text, nullable=True)
    resolved_by = Column(String, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))