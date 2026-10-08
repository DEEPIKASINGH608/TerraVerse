from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def check_db_status():
    return {"connected": True, "database": "PostGIS"}

@router.post("/sync")
def sync_database():
    return {"status": "success", "message": "Database synchronized"}
