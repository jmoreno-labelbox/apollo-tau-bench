# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetModelMetrics(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], model_name) -> str:
        if not model_name:
            return json.dumps({"error": "Missing model_name"})
        for m in data.get("metrics", []):
            if m.get("model_name") == model_name:
                return json.dumps({
                    "model_name": model_name,
                    "auc": m.get("auc_nullable"),
                    "accuracy": m.get("accuracy_nullable")
                })
        return json.dumps({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_model_metrics",
                "description": "Return stored AUC/accuracy for a given model_name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"}
                    },
                    "required": ["model_name"]
                }
            }
        }
