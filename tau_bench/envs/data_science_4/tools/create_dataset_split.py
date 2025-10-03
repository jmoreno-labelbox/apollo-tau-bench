from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateDatasetSplit(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], features_id: str = None, test_fraction: float = None) -> str:
        split_id = "SPLIT_001"

        split_entry = {
            "split_id": split_id,
            "features_id": features_id,
            "method": "time_based",
            "test_fraction": test_fraction,
            "split_summary_json_path": f"/processed_data/split_summary_{split_id}.json",
        }

        data.setdefault("dataset_split.json", []).append(split_entry)
        payload = split_entry
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createDatasetSplit",
                "description": "Creates a train/test split from the feature set based on the specified method.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "features_id": {
                            "type": "string",
                            "description": "The ID of the feature set to use.",
                        },
                        "test_fraction": {
                            "type": "number",
                            "description": "The fraction of data for the test set.",
                        },
                    },
                    "required": ["features_id", "test_fraction"],
                },
            },
        }
