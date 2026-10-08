from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, JSON

from backend.app.db.base import Base


class ConflictModel(Base):
    __tablename__ = "conflicts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    parcel_id = Column(String(100), nullable=False, index=True)
    conflict_type = Column(String(100), nullable=False)
    severity = Column(String(20), default="MEDIUM")
    status = Column(String(50), default="OPEN", index=True)
    contending_sources = Column(JSON, nullable=True)
    evidence_data = Column(JSON, nullable=True)
    ai_recommendation = Column(JSON, nullable=True)
    confidence = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
