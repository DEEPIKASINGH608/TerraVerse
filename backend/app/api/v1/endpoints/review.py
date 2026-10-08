from fastapi import APIRouter

router = APIRouter()

@router.post("/approve/{conflict_id}")
def approve_conflict(conflict_id: str):
    return {"conflict_id": conflict_id, "status": "approved"}

@router.post("/reject/{conflict_id}")
def reject_conflict(conflict_id: str):
    return {"conflict_id": conflict_id, "status": "rejected"}