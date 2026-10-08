import os
import shutil
from pathlib import Path
from typing import Union

SUPPORTED_EXTENSIONS = {
    ".geojson",
    ".json",
    ".shp",
    ".gpkg",
    ".kml",
    ".tif",
    ".tiff",
    ".csv",
}


def ensure_directory(path: Union[str, Path]) -> Path:
    """Ensures that a target directory exists, creating missing parent folders if necessary."""
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def get_file_extension(file_path: Union[str, Path]) -> str:
    """Extracts the lowercase file extension from a file path."""
    return Path(file_path).suffix.lower()


def is_supported_geospatial_file(file_path: Union[str, Path]) -> bool:
    """Checks whether the file has a supported spatial or tabular format extension."""
    ext = get_file_extension(file_path)
    return ext in SUPPORTED_EXTENSIONS


def safe_remove_file(file_path: Union[str, Path]) -> bool:
    """Safely removes a file or directory path without raising unhandled exceptions."""
    path = Path(file_path)
    try:
        if path.is_file() or path.is_symlink():
            path.unlink()
            return True
        elif path.is_dir():
            shutil.rmtree(path)
            return True
    except Exception:
        pass
    return False
