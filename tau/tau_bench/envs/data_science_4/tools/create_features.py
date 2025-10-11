# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateFeatures(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], input_csv_path) -> str:
        input_path = input_csv_path
        if not input_path:
            return json.dumps({"error": "input_csv_path is a required argument."})

        features_id = "FEATURES_001"
        new_features_path = "/processed_data/features_001.csv"

        feature_entry = {
            "features_id": features_id,
            "source_csv_path": input_path,
            "features_csv_path": new_features_path,
            "feature_names": [
                "precip_24h_mm",
                "tide_anomaly_6h_max_m",
                "pressure_drop_6h_hpa",
            ],
        }

        data.setdefault("features", []).append(feature_entry)
        return json.dumps(feature_entry)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateFeatures",
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
