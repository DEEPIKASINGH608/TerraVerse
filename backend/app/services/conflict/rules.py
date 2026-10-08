from typing import Any, Dict


class ConflictRulesEngine:
    """Rule suite for identifying spatial overlapping and attribute inconsistency severity."""

    @staticmethod
    def evaluate_area_discrepancy(area_a: float, area_b: float) -> Dict[str, Any]:
        """Calculates area divergence ratio and assigns conflict severity."""
        if area_a <= 0 or area_b <= 0:
            return {"discrepancy_ratio": 1.0, "severity": "CRITICAL"}

        ratio = abs(area_a - area_b) / max(area_a, area_b)

        if ratio > 0.25:
            severity = "HIGH"
        elif ratio > 0.10:
            severity = "MEDIUM"
        else:
            severity = "LOW"

        return {"discrepancy_ratio": round(ratio, 4), "severity": severity}
