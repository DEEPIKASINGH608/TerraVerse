import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import os
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier

def train_model():
    print("Training parcel-matching model...")

    X_train = np.array([
        [0.95, 0.02, 0.98],
        [0.88, 0.05, 0.90],
        [0.40, 0.35, 0.20],
        [0.20, 0.50, 0.10],
        [0.92, 0.01, 0.95],
        [0.30, 0.40, 0.15],
    ])

    y_train = np.array([1, 1, 0, 0, 1, 0])

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    models_dir = Path(__file__).resolve().parent.parent / "models"
    os.makedirs(models_dir, exist_ok=True)

    model_path = models_dir / "parcel_matcher.pkl"
    joblib.dump(model, model_path)
    print(f"Model trained and saved to: {model_path}")

if __name__ == "__main__":
    train_model()