import logging
from typing import List

logger = logging.getLogger("terraverse")


class MatchModel:
    """Machine learning model wrapper for record linkage pair classification."""

    def predict_match_probability(self, feature_vectors: List[List[float]]) -> List[float]:
        """Predicts match probabilities for candidate feature pairs."""
        probabilities = []
        for vec in feature_vectors:
            iou = vec[0] if len(vec) > 0 else 0.0
            prob = min(max(iou * 0.95 + 0.05, 0.0), 1.0)
            probabilities.append(round(prob, 4))
        return probabilities