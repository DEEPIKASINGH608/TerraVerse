from typing import Dict, Any
from app.core.constants import DEPARTMENT_RELIABILITY_WEIGHTS

class ConfidenceScorer:
    @staticmethod
    def calculate_harmonization_confidence(
        geometry_agreement: float,
        attribute_agreement: float,
        source_department: str,
        has_topology_error: bool = False
    ) -> Dict[str, float]:
        """Calculates multi-criteria confidence score S_H."""

        s_r = DEPARTMENT_RELIABILITY_WEIGHTS.get(source_department.lower(), 0.70)

        s_g = max(0.0, min(1.0, geometry_agreement))

        s_a = max(0.0, min(1.0, attribute_agreement))

        s_o = 0.50 if has_topology_error else 1.0

        final_score = (s_g * 0.35) + (s_a * 0.25) + (s_r * 0.25) + (s_o * 0.15)

        return {
            "final_confidence": round(final_score, 4),
            "geometry_score": round(s_g, 4),
            "attribute_score": round(s_a, 4),
            "source_reliability": round(s_r, 4),
            "topology_health": round(s_o, 4)
        }