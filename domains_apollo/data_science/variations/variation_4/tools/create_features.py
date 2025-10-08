from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateFeatures(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], input_csv_path: str = None) -> str:
        if not input_csv_path:
            payload = {"error": "input_csv_path is a required argument."}
            out = json.dumps(payload)
            return out

        features_id = "FEATURES_001"
        new_features_path = "/processed_data/features_001.csv"

        feature_entry = {
            "features_id": features_id,
            "source_csv_path": input_csv_path,
            "features_csv_path": new_features_path,
            "feature_names": [
                "precip_24h_mm",
                "tide_anomaly_6h_max_m",
                "pressure_drop_6h_hpa",
            ],
        }

        data.setdefault("features", []).append(feature_entry)
        payload = feature_entry
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createFeatures",
                "description": "Takes a path to a processed timeseries CSV and engineers a standard set of features required for modeling.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "input_csv_path": {
                            "type": "string",
                            "description": "The file path to the processed timeseries data.",
                        }
                    },
                    "required": ["input_csv_path"],
                },
            },
        }
