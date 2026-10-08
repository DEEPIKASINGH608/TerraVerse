from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_parcels():
    return {"parcels": []}

@router.get("/{parcel_id}")
def get_parcel(parcel_id: str):
    return {"parcel_id": parcel_id, "geometry": "POLYGON(...)"}
