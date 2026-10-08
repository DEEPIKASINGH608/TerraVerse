from typing import Dict, List
import geopandas as gpd
from backend.app.core.constants import FIELD_ALIASES


class SchemaMapper:
    """Standardizes disparate column names across department datasets."""

    @staticmethod
    def normalize_schema(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        """Renames known aliases to standardized target field names."""
        gdf_copy = gdf.copy()
        rename_dict = {}

        for col in gdf_copy.columns:
            cleaned_col = str(col).strip().lower()
            for target_field, aliases in FIELD_ALIASES.items():
                if cleaned_col in aliases:
                    rename_dict[col] = target_field
                    break

        return gdf_copy.rename(columns=rename_dict)
