from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, JSON

from backend.app.db.base import Base


class AuditLogModel(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    action = Column(String(100), nullable=False, index=True)
    user_id = Column(String(100), nullable=True)
    target_type = Column(String(50), nullable=True)
    target_id = Column(String(100), nullable=True, index=True)
    details = Column(JSON, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
