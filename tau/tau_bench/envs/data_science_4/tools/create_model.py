# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateModel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        config_id = kwargs.get("model_config_id")
        model_name = kwargs.get("model_name")
        model_id = f"MODEL_{model_name}"
        model_entry = {
            "model_id": model_id,
            "model_name": model_name,
            "config_id": config_id,
            "model_path": f"/models/{model_id}.joblib",
            "model_type": kwargs.get("model_type"),
            "feature_names": kwargs.get("features_id"),
            "train_metrics_json_path_nullable": f"/metrics/{model_id}_train_metrics.json",
        }
        data.setdefault("models", []).append(model_entry)
        return json.dumps(model_entry)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateModel",
                "description": "Creates a model entry, linking a configuration, model type, and feature set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_config_id": {
                            "type": "string",
                            "description": "The ID of the model configuration.",
                        },
                        "model_type": {
                            "type": "string",
                            "description": "The type of model to train, e.g., 'logistic_regression'.",
                        },
                        "features_id": {
                            "type": "string",
                            "description": "The ID of the feature set to be used by the model.",
                        },
                    },
                    "required": ["model_config_id", "model_type", "features_id"],
                },
            },
        }
