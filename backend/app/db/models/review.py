from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, JSON

from backend.app.db.base import Base


class ReviewTaskModel(Base):
    __tablename__ = "review_tasks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    conflict_id = Column(Integer, nullable=False, index=True)
    parcel_id = Column(String(100), nullable=False)
    assigned_to = Column(String(100), nullable=True)
    status = Column(String(50), default="PENDING")  # PENDING, APPROVED, REJECTED
    resolution_notes = Column(String, nullable=True)
    overridden_data = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    resolved_at = Column(DateTime, nullable=True)