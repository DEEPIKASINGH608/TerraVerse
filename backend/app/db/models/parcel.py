from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, JSON

from backend.app.db.base import Base


class CanonicalParcelModel(Base):
    __tablename__ = "canonical_parcels"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    parcel_id = Column(String(100), unique=True, nullable=False, index=True)
    geometry = Column(String, nullable=False)  # Stored as WKT string or PostGIS Geometry
    owner_name = Column(String(255), nullable=True)
    land_use = Column(String(100), nullable=True)
    area_sqm = Column(Float, nullable=True)
    revenue_id = Column(String(100), nullable=True)
    municipal_id = Column(String(100), nullable=True)
    survey_id = Column(String(100), nullable=True)
    confidence_score = Column(Float, nullable=False, default=0.0)
    geometry_score = Column(Float, nullable=True)
    attribute_score = Column(Float, nullable=True)
    status = Column(String(50), default="harmonized", index=True)  # harmonized, needs_review
    provenance = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)