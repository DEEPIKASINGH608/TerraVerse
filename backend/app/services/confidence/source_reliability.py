from typing import Dict
from backend.app.core.constants import DEPARTMENT_RELIABILITY_WEIGHTS


class SourceReliabilityEvaluator:
    """Evaluates spatial data authority based on departmental weights."""

    @staticmethod
    def get_source_weight(source_name: str) -> float:
        """Returns normalized reliability weight (0.0 to 1.0) for a target department."""
        cleaned_key = str(source_name).strip().lower()
        return DEPARTMENT_RELIABILITY_WEIGHTS.get(cleaned_key, DEPARTMENT_RELIABILITY_WEIGHTS.get("unknown", 0.70))