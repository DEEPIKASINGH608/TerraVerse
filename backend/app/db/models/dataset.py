from sqlalchemy import Column, String, Integer, Float, DateTime, JSON, Text
from datetime import datetime, timezone
import uuid
from app.db.session import Base

class DatasetModel(Base):
    __tablename__ = "datasets"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    source_department = Column(String, nullable=False)
    file_format = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    original_crs = Column(String, nullable=True)
    feature_count = Column(Integer, default=0)
    quality_score = Column(Float, default=0.0)
    status = Column(String, default="uploaded")  
    metadata_info = Column(JSON, default={})
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))