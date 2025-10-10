# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class EvaluateModel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        metrics_id = "METRICS_001"
        predictions_id = kwargs.get("predictions_id")
        if not predictions_id:
            predictions_id = "PRED_001"
        metrics_entry = {
            "model_id": kwargs.get("model_id"),
            "metrics_id": metrics_id,
            "predictions_id": predictions_id,
            "auc": 0.87,
            "accuracy": 0.91,
            "metrics_json_path": f"/metrics/metrics_{metrics_id}.json",
        }

        data.setdefault("metrics.json", []).append(metrics_entry)
        return json.dumps(metrics_entry)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EvaluateModel",
                "description": "Calculates performance metrics (AUC and accuracy) for a trained model based on its predictions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "predictions_id": {
                            "type": "string",
                            "description": "The ID of the predictions to evaluate.",
                        }
                    },
                    "required": ["predictions_id"],
                },
            },
        }
