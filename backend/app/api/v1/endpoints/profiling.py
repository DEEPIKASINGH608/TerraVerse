from fastapi import APIRouter

router = APIRouter()

@router.get("/geometry")
def profile_geometry():
    return {"geometry_types": {"Polygons": 0, "MultiPolygons": 0}, "invalid_count": 0}
