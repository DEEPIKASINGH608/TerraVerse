from sqlalchemy import Column, String, Float, DateTime, JSON, Integer
from geoalchemy2 import Geometry
from datetime import datetime, timezone
import uuid
from app.db.session import Base

class CanonicalParcelModel(Base):
    __tablename__ = "canonical_parcels"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    parcel_id = Column(String, index=True, nullable=False)
    geometry = Column(Geometry(geometry_type='POLYGON', srid=4326), nullable=False)

    
    owner_name = Column(String, nullable=True)
    land_use = Column(String, nullable=True)
    area_sqm = Column(Float, nullable=True)
    building_count = Column(Integer, default=0)

    revenue_id = Column(String, nullable=True)
    municipal_id = Column(String, nullable=True)
    survey_id = Column(String, nullable=True)

    confidence_score = Column(Float, nullable=False, default=0.0)
    geometry_score = Column(Float, default=0.0)
    attribute_score = Column(Float, default=0.0)
    status = Column(String, default="harmonized")

    provenance = Column(JSON, default={})
    conflicts_summary = Column(JSON, default=[])

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))