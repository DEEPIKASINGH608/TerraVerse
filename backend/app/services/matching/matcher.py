import geopandas as gpd
from backend.app.services.matching.candidate_generator import SpatialCandidateGenerator
from backend.app.services.matching.feature_engineering import FeatureEngineer
from backend.app.services.matching.match_model import MatchModel


class RecordMatcher:
    """Orchestrates end-to-end entity matching across spatial datasets."""

    def __init__(self):
        self.model = MatchModel()

    def find_matches(self, gdf_a: gpd.GeoDataFrame, gdf_b: gpd.GeoDataFrame, threshold: float = 0.70):
        pairs = SpatialCandidateGenerator.generate_candidate_pairs(gdf_a, gdf_b)
        matches = []

        for idx_a, idx_b in pairs:
            feats = FeatureEngineer.compute_pair_features(gdf_a.iloc[idx_a], gdf_b.iloc[idx_b])
            prob = self.model.predict_match_probability([[feats["iou"], feats["area_ratio"]]])[0]

            if prob >= threshold:
                matches.append({
                    "index_a": idx_a,
                    "index_b": idx_b,
                    "match_score": prob,
                })

        return matches