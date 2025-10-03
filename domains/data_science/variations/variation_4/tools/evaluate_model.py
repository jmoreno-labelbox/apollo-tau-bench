from tau_bench.envs.tool import Tool
import json
from typing import Any

class EvaluateModel(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], model_id: str = None, predictions_id: str = None) -> str:
        metrics_id = "METRICS_001"
        if not predictions_id:
            predictions_id = "PRED_001"
        metrics_entry = {
            "model_id": model_id,
            "metrics_id": metrics_id,
            "predictions_id": predictions_id,
            "auc": 0.87,
            "accuracy": 0.91,
            "metrics_json_path": f"/metrics/metrics_{metrics_id}.json",
        }

        data.setdefault("metrics.json", []).append(metrics_entry)
        payload = metrics_entry
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "evaluateModel",
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
