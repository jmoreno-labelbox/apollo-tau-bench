# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPredictionsByModelName(Tool):
    """
    Retrieves predictions record by model_name.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], model_name: str) -> str:
        rows = data.get("predictions", [])
        for row in rows:
            if row.get("model_name") == model_name:
                return json.dumps(row)
        return json.dumps({"error": "predictions not found", "model_name": model_name})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_predictions_by_model_name",
                "description": "Retrieves predictions record by model_name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"}
                    },
                    "required": ["model_name"]
                }
            }
        }
