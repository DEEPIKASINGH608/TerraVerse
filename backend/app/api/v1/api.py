from fastapi import APIRouter

from backend.app.api.v1.endpoints import (
    auth,
    changes,
    confidence,
    conflicts,
    databases,
    demo,
    exports,
    georeferencing,
    harmonization,
    matching,
    parcels,
    profiling,
    review,
    statistics,
    topology,
)

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(changes.router, prefix="/changes", tags=["Change Detection"])
api_router.include_router(confidence.router, prefix="/confidence", tags=["Confidence Scoring"])
api_router.include_router(conflicts.router, prefix="/conflicts", tags=["Conflict Resolution"])
api_router.include_router(databases.router, prefix="/databases", tags=["Database Management"])
api_router.include_router(demo.router, prefix="/demo", tags=["Demo Pipeline"])
api_router.include_router(exports.router, prefix="/exports", tags=["Data Export"])
api_router.include_router(georeferencing.router, prefix="/georeferencing", tags=["Georeferencing"])
api_router.include_router(harmonization.router, prefix="/harmonization", tags=["Schema Harmonization"])
api_router.include_router(matching.router, prefix="/matching", tags=["Entity Matching"])
api_router.include_router(parcels.router, prefix="/parcels", tags=["Parcels Management"])
api_router.include_router(profiling.router, prefix="/profiling", tags=["Spatial Profiling"])
api_router.include_router(review.router, prefix="/review", tags=["Manual Review"])
api_router.include_router(statistics.router, prefix="/statistics", tags=["Statistics & Metrics"])
api_router.include_router(topology.router, prefix="/topology", tags=["Topology Engine"])
