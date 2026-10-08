from fastapi import APIRouter

router = APIRouter()

@router.post("/validate")
def validate_topology():
    return {"errors_found": 0, "overlaps": 0, "gaps": 0}

@router.post("/fix")
def fix_topology():
    return {"fixed_count": 0}
