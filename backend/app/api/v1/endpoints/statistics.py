from fastapi import APIRouter

router = APIRouter()

@router.get("/summary")
def get_summary_statistics():
    return {"total_parcels": 0, "conflicts_resolved": 0, "accuracy_score": 0.95}