from fastapi import APIRouter

router = APIRouter()

@router.post("/align")
def align_coordinates(source_crs: str, target_crs: str):
    return {"status": "success", "source_crs": source_crs, "target_crs": target_crs}