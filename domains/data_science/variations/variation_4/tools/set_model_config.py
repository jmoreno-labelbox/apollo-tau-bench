from tau_bench.envs.tool import Tool
import json
from typing import Any

class SetModelConfig(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        classification_threshold_m: float = None, 
        precip_24h_threshold_mm: float = None, 
        test_split_fraction: float = None
    ) -> str:
        config_id = "MODEL_CONFIG_001"

        config_entry = {
            "config_id": config_id,
            "classification_threshold_m": classification_threshold_m,
            "precip_24h_threshold_mm": precip_24h_threshold_mm,
            "test_split_fraction": test_split_fraction,
            "config_json_path": f"/configs/model_config_{config_id}.json",
        }

        data.setdefault("model_config", []).append(config_entry)
        payload = config_entry
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setModelConfig",
                "description": "Creates a configuration record for the modeling process with specified parameters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "classification_threshold_m": {
                            "type": "number",
                            "description": "The threshold in meters for classifying high-risk events.",
                        },
                        "precip_24h_threshold_mm": {
                            "type": "number",
                            "description": "The precipitation threshold in millimeters.",
                        },
                        "test_split_fraction": {
                            "type": "number",
                            "description": "The fraction of data for the test set.",
                        },
                    },
                    "required": [],
                },
            },
        }
