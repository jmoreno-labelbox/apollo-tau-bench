# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetMetricsByModelName(Tool):
    """
    Retrieves metrics record by model_name.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], model_name: str) -> str:
        rows = list(data.get("metrics", {}).values())
        for row in rows:
            if row.get("model_name") == model_name:
                return json.dumps(row)
        return json.dumps({"error": "metrics not found", "model_name": model_name})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_metrics_by_model_name",
                "description": "Retrieves metrics record by model_name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"}
                    },
                    "required": ["model_name"]
                }
            }
        }
