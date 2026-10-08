from fastapi import APIRouter

router = APIRouter()

@router.get("/scores")
def get_confidence_scores():
    return {"mean_confidence": 0.92, "parcel_scores": []}

@router.post("/evaluate")
def evaluate_parcel_confidence(parcel_id: str):
    return {"parcel_id": parcel_id, "confidence_score": 0.88, "factors": ["area_match", "iou"]}
