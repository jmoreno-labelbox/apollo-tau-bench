# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class TrainModel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], config_id, features_id, model_name, model_type, split_id) -> str:
        model_id = f"MODEL_{model_name}"
        predictions_id = "PRED_001"

        model_entry = {
            "model_id": model_id,
            "model_name": model_name,
            "model_type": model_type,
            "features_id": features_id,
            "config_id": config_id,
            "split_id": split_id,
            "model_path": f"/models/{model_id}.joblib",
        }

        predictions_entry = {
            "predictions_id": predictions_id,
            "model_id": model_id,
            "predictions_csv_path": f"/predictions/PRED_{model_id}.csv",
        }

        data.setdefault("models.json", []).append(model_entry)
        data.setdefault("predictions.json", []).append(predictions_entry)

        return json.dumps(predictions_entry)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "TrainModel",
                "description": "Trains a simple logistic regression model using the specified features, configuration, and data split.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {
                            "type": "string",
                            "description": "A descriptive name for the model.",
                        },
                        "features_id": {
                            "type": "string",
                            "description": "The ID of the feature set.",
                        },
                        "config_id": {
                            "type": "string",
                            "description": "The ID of the model configuration.",
                        },
                        "split_id": {
                            "type": "string",
                            "description": "The ID of the dataset split.",
                        },
                    },
                    "required": ["model_name", "features_id", "config_id", "split_id"],
                },
            },
        }
