from app.db.session import engine, Base
from app.db.models.dataset import DatasetModel
from app.db.models.parcel import CanonicalParcelModel
from app.db.models.conflict import ConflictModel

try:
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")
except Exception as e:
    print(f"Database connection error: {e}")