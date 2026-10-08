from fastapi import APIRouter

router = APIRouter()

@router.post("/record-linkage")
def match_records(threshold: float = 0.8):
    return {"status": "completed", "matches_found": 0, "threshold": threshold}
