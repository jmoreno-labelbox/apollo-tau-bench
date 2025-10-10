# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetModelConfig(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        config_id = "MODEL_CONFIG_001"

        config_entry = {
            "config_id": config_id,
            "classification_threshold_m": kwargs.get("classification_threshold_m"),
            "precip_24h_threshold_mm": kwargs.get("precip_24h_threshold_mm"),
            "test_split_fraction": kwargs.get("test_split_fraction"),
            "config_json_path": f"/configs/model_config_{config_id}.json",
        }

        data.setdefault("model_config", []).append(config_entry)
        return json.dumps(config_entry)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetModelConfig",
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
