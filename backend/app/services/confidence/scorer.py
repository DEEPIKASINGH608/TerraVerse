from typing import Dict, Any
from backend.app.services.confidence.source_reliability import SourceReliabilityEvaluator


class ConfidenceScorer:
    """Calculates overall composite confidence scores for harmonized parcel records."""

    @staticmethod
    def calculate_harmonization_confidence(
        geometry_agreement: float,
        attribute_agreement: float,
        source_department: str = "survey_department",
        geom_weight: float = 0.50,
        attr_weight: float = 0.30,
        source_weight_factor: float = 0.20,
    ) -> Dict[str, Any]:
        """Calculates weighted confidence score factoring spatial agreement and departmental trust."""
        source_score = SourceReliabilityEvaluator.get_source_weight(source_department)

        final_score = (
            (geometry_agreement * geom_weight) +
            (attribute_agreement * attr_weight) +
            (source_score * source_weight_factor)
        )

        final_score = round(min(max(final_score, 0.0), 1.0), 4)

        return {
            "final_confidence": final_score,
            "geometry_score": round(geometry_agreement, 4),
            "attribute_score": round(attribute_agreement, 4),
            "source_reliability_score": round(source_score, 4),
        }
