from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/geojson")
def export_geojson():
    return {"type": "FeatureCollection", "features": []}

@router.get("/shapefile")
def export_shapefile():
    return {"message": "Export shapefile job queued"}