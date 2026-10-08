import re
from typing import Any, Dict


def validate_geojson_structure(data: Dict[str, Any]) -> bool:
    """Validates if a dictionary conforms to basic GeoJSON structure specifications."""
    if not isinstance(data, dict):
        return False

    geojson_type = data.get("type")
    if geojson_type not in ["FeatureCollection", "Feature", "Polygon", "MultiPolygon", "Point"]:
        return False

    if geojson_type == "FeatureCollection" and "features" not in data:
        return False

    if geojson_type == "Feature" and ("geometry" not in data or "properties" not in data):
        return False

    return True


def validate_crs_string(crs_str: str) -> bool:
    """Validates standard EPSG format strings (e.g., 'EPSG:4326')."""
    if not isinstance(crs_str, str):
        return False
    pattern = r"^EPSG:\d{4,5}$"
    return bool(re.match(pattern, crs_str.strip(), re.IGNORECASE))


def validate_email_format(email: str) -> bool:
    """Validates email format using regex pattern."""
    if not isinstance(email, str):
        return False
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email.strip()))