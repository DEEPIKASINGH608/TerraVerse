from typing import Any, Dict


class AttributeHarmonizer:
    """Merges and reconciles land ownership and usage metadata."""

    @staticmethod
    def resolve_attribute_conflicts(attr_a: Dict[str, Any], attr_b: Dict[str, Any]) -> Dict[str, Any]:
        """Fuses non-spatial properties giving precedence to complete values."""
        harmonized = {}
        all_keys = set(attr_a.keys()).union(set(attr_b.keys()))

        for key in all_keys:
            val_a = attr_a.get(key)
            val_b = attr_b.get(key)
            harmonized[key] = val_a if val_a is not None else val_b

        return harmonized