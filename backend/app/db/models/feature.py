from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, JSON

from backend.app.db.base import Base


class FeatureModel(Base):
    __tablename__ = "raw_features"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dataset_id = Column(Integer, nullable=False, index=True)
    source_feature_id = Column(String(100), nullable=True)
    geometry_wkt = Column(String, nullable=False)
    attributes = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
