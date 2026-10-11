from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_conflicts():
    return {"conflicts": []}

@router.get("/{conflict_id}")
def get_conflict(conflict_id: str):
    return {"conflict_id": conflict_id, "type": "overlap", "severity": "high"}