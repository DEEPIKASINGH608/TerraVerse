"""
TerraVerse Backend Utilities Package.
"""

from backend.app.utils.file_utils import (
    ensure_directory,
    get_file_extension,
    is_supported_geospatial_file,
    safe_remove_file,
)
from backend.app.utils.geometry_utils import (
    calculate_area,
    calculate_centroid,
    check_geometry_validity,
    clean_geometry,
)
from backend.app.utils.identifiers import (
    generate_conflict_id,
    generate_dataset_id,
    generate_parcel_id,
    generate_uuid,
)
from backend.app.utils.logger import get_logger, setup_logging
from backend.app.utils.validation import (
    validate_crs_string,
    validate_email_format,
    validate_geojson_structure,
)

__all__ = [
    "ensure_directory",
    "get_file_extension",
    "is_supported_geospatial_file",
    "safe_remove_file",
    "clean_geometry",
    "calculate_area",
    "calculate_centroid",
    "check_geometry_validity",
    "generate_uuid",
    "generate_parcel_id",
    "generate_conflict_id",
    "generate_dataset_id",
    "setup_logging",
    "get_logger",
    "validate_geojson_structure",
    "validate_crs_string",
    "validate_email_format",
]
