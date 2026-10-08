from backend.app.utils.file_utils import is_supported_geospatial_file


def test_supported_extensions():
    """Validates file extension checking for supported spatial formats."""
    assert is_supported_geospatial_file("data/parcels.geojson") is True
    assert is_supported_geospatial_file("data/cadastre.shp") is True
    assert is_supported_geospatial_file("data/document.pdf") is False