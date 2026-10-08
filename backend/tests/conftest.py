import pytest
import geopandas as gpd
from shapely.geometry import Polygon
from fastapi.testclient import TestClient

from backend.app.main import app


@pytest.fixture
def api_client():
    """Provides a FastAPI TestClient instance."""
    return TestClient(app)


@pytest.fixture
def sample_polygon_a():
    """Creates a sample valid polygon geometry representing Parcel A."""
    return Polygon([(77.100, 28.600), (77.105, 28.600), (77.105, 28.605), (77.100, 28.605)])


@pytest.fixture
def sample_polygon_b():
    """Creates an overlapping polygon geometry representing Parcel B."""
    return Polygon([(77.102, 28.602), (77.107, 28.602), (77.107, 28.607), (77.102, 28.607)])


@pytest.fixture
def sample_geodataframe(sample_polygon_a):
    """Creates a mock GeoDataFrame for testing spatial operations."""
    data = {
        "parcel_id": ["PCL-101"],
        "owner_name": ["Jane Doe"],
        "geometry": [sample_polygon_a],
    }
    return gpd.GeoDataFrame(data, crs="EPSG:4326")