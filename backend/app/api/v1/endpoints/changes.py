from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_change_detection_results():
    return {"status": "success", "changes_detected": []}

@router.post("/run")
def trigger_change_detection(dataset_a_id: str, dataset_b_id: str):
    return {"status": "processing", "job_id": "job_change_001"}
