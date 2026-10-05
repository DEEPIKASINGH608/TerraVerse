import numpy as np
from xgboost import XGBClassifier
from typing import Dict, Any

class MatchModel:
    def __init__(self):
        self.model = XGBClassifier(
            n_estimators=50,
            max_depth=4,
            learning_rate=0.1,
            eval_metric="logloss"
        )
        self.is_trained = False
        self._bootstrap_synthetic_model()

    def _bootstrap_synthetic_model(self):
        """Train classifier on synthetic geometric feature distributions."""
        X_train = []
        y_train = []

        for _ in range(200):
            iou = np.random.uniform(0.75, 0.99)
            area_ratio = np.random.uniform(0.85, 1.0)
            centroid_dist = np.random.uniform(0.0, 0.0001)
            hausdorff_dist = np.random.uniform(0.0, 0.0002)
            X_train.append([iou, area_ratio, centroid_dist, hausdorff_dist])
            y_train.append(1)

        for _ in range(200):
            iou = np.random.uniform(0.0, 0.35)
            area_ratio = np.random.uniform(0.1, 0.6)
            centroid_dist = np.random.uniform(0.0005, 0.005)
            hausdorff_dist = np.random.uniform(0.0008, 0.008)
            X_train.append([iou, area_ratio, centroid_dist, hausdorff_dist])
            y_train.append(0)

        self.model.fit(np.array(X_train), np.array(y_train))
        self.is_trained = True

    def predict_match_probability(self, metrics: Dict[str, float]) -> float:
        """Predict probability that two input geometries refer to the same land parcel."""
        if not self.is_trained:
            return 0.0

        features = np.array([[
            metrics["iou"],
            metrics["area_ratio"],
            metrics["centroid_dist"],
            metrics["hausdorff_dist"]
        ]])

        prob = self.model.predict_proba(features)[0][1]
        return float(prob)

match_model_instance = MatchModel()