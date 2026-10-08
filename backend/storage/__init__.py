"""
TerraVerse Backend File Storage Package.

Handles local file storage paths for raw, normalized, processed,
and harmonized geospatial data layers.
"""

from pathlib import Path

STORAGE_BASE_DIR = Path(__file__).resolve().parent

RAW_DATA_DIR = STORAGE_BASE_DIR / "raw"
NORMALIZED_DATA_DIR = STORAGE_BASE_DIR / "normalized"
PROCESSED_DATA_DIR = STORAGE_BASE_DIR / "processed"
HARMONIZED_DATA_DIR = STORAGE_BASE_DIR / "harmonized"

# Ensure storage directories exist at runtime
for directory in [
    RAW_DATA_DIR,
    NORMALIZED_DATA_DIR,
    PROCESSED_DATA_DIR,
    HARMONIZED_DATA_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)