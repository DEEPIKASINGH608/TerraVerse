from backend.app.services.confidence.scorer import ConfidenceScorer
from backend.app.services.confidence.source_reliability import SourceReliabilityEvaluator


def test_source_reliability_evaluation():
    """Validates departmental weight lookups."""
    survey_weight = SourceReliabilityEvaluator.get_source_weight("survey_department")
    unknown_weight = SourceReliabilityEvaluator.get_source_weight("non_existent_dept")

    assert survey_weight > 0.0
    assert unknown_weight == 0.70


def test_confidence_scoring():
    """Validates confidence calculation math and output range."""
    result = ConfidenceScorer.calculate_harmonization_confidence(
        geometry_agreement=0.90,
        attribute_agreement=0.80,
        source_department="survey_department",
    )

    assert "final_confidence" in result
    assert 0.0 <= result["final_confidence"] <= 1.0