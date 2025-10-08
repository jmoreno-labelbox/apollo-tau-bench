from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateModel(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], model_config_id: str = None, model_name: str = None, model_type: str = None, features_id: list[str] = None) -> str:
        model_id = f"MODEL_{model_name}"
        model_entry = {
            "model_id": model_id,
            "model_name": model_name,
            "config_id": model_config_id,
            "model_path": f"/models/{model_id}.joblib",
            "model_type": model_type,
            "feature_names": features_id,
            "train_metrics_json_path_nullable": f"/metrics/{model_id}_train_metrics.json",
        }
        data.setdefault("models", []).append(model_entry)
        payload = model_entry
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createModel",
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
