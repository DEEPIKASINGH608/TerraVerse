from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, JSON

from backend.app.db.base import Base


class DatasetModel(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    department = Column(String(100), nullable=False, index=True)
    format = Column(String(50), nullable=False)  # GeoJSON, Shapefile, GeoTIFF
    file_path = Column(String(500), nullable=False)
    crs = Column(String(50), default="EPSG:4326")
    feature_count = Column(Integer, default=0)
    metadata_info = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)