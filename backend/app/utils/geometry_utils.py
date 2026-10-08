from typing import Optional, Tuple, Any, Dict
from shapely.geometry import shape, mapping, base
import shapely.wkt


def clean_geometry(geom: base.BaseGeometry) -> base.BaseGeometry:
    """Repairs invalid geometries using zero-distance buffering or topological cleanup."""
    if geom is None:
        return None
    if not geom.is_valid:
        return geom.buffer(0)
    return geom


def calculate_area(geom: base.BaseGeometry, in_square_meters: bool = True) -> float:
    """Calculates the surface area of a geometry."""
    if geom is None or geom.is_empty:
        return 0.0
    return float(geom.area)


def calculate_centroid(geom: base.BaseGeometry) -> Optional[Tuple[float, float]]:
    """Calculates the (longitude, latitude) / (x, y) centroid of a geometry."""
    if geom is None or geom.is_empty:
        return None
    centroid = geom.centroid
    return float(centroid.x), float(centroid.y)


def check_geometry_validity(geom: base.BaseGeometry) -> Dict[str, Any]:
    """Inspects a Shapely geometry and returns validity information."""
    if geom is None:
        return {"is_valid": False, "reason": "Geometry object is None"}

    is_valid = geom.is_valid
    reason = "Valid Geometry" if is_valid else "Topology error / self-intersection"

    return {
        "is_valid": is_valid,
        "reason": reason,
        "geom_type": geom.geom_type,
        "is_empty": geom.is_empty,
    }