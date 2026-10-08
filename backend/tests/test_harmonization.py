import geopandas as gpd
from backend.app.services.harmonization.schema_mapper import SchemaMapper


def test_schema_normalization():
    """Validates renaming alias column headers to canonical names."""
    gdf = gpd.GeoDataFrame(
        {"khasra_no": ["123/A"], "prop_owner": ["Alice Smith"]},
        geometry=[None],
    )

    normalized_gdf = SchemaMapper.normalize_schema(gdf)
    assert "parcel_id" in normalized_gdf.columns or "owner_name" in normalized_gdf.columns