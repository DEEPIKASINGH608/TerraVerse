import difflib
from typing import Dict, Any, List
from app.core.constants import FIELD_ALIASES

class SchemaMapper:
    @staticmethod
    def map_columns(incoming_columns: List[str]) -> Dict[str, str]:
        """Maps arbitrary input column headers to GeoLand canonical keys."""
        mapping = {}
        for col in incoming_columns:
            clean_col = str(col).lower().strip()

            matched = False
            for canonical_key, aliases in FIELD_ALIASES.items():
                if clean_col in aliases:
                    mapping[col] = canonical_key
                    matched = True
                    break

            if not matched:
                for canonical_key, aliases in FIELD_ALIASES.items():
                    matches = difflib.get_close_matches(clean_col, aliases, cutoff=0.75)
                    if matches:
                        mapping[col] = canonical_key
                        matched = True
                        break

            if not matched:
                mapping[col] = clean_col

        return mapping