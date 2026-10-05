from typing import Dict, List

DEPARTMENT_RELIABILITY_WEIGHTS: Dict[str, float] = {
    "survey_department": 0.98,
    "cors_gnss": 0.99,
    "ground_truth_team": 0.96,
    "drone_survey": 0.94,
    "revenue_department": 0.90,
    "municipal_corporation": 0.88,
    "utility_department": 0.85,
    "unknown": 0.70
}

CONFIDENCE_THRESHOLD_HIGH = 0.90
CONFIDENCE_THRESHOLD_MEDIUM = 0.70

FIELD_ALIASES: Dict[str, List[str]] = {
    "parcel_id": [
        "parcel_id", "parcel_no", "plot_id", "khasra_no",
        "survey_no", "property_id", "pid", "gis_id"
    ],
    "owner_name": [
        "owner_name", "owner", "landowner", "property_owner",
        "khatadaar", "khata_holder", "title_holder"
    ],
    "land_use": [
        "land_use", "usage", "use_type", "zone",
        "category", "property_type", "classification"
    ],
    "area_sqm": [
        "area_sqm", "area", "calculated_area", "plot_area",
        "shape_area", "gis_area", "total_area"
    ]
}