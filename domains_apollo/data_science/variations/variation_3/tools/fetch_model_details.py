from tau_bench.envs.tool import Tool
import json
from typing import Any

class FetchModelDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], model_id: str = None, model_name: str = None) -> str:
        models = data.get("models", []) or []
        row = None
        if model_id is not None:
            row = next((m for m in models if str(m.get("model_id")) == str(model_id)), None)
        elif model_name:
            row = next((m for m in models if m.get("model_name") == model_name), None)
        payload = row or {"error": "Model not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetModelDetails",
                "description": "Read a model by id or by model_name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_id": {"type": "string"},
                        "model_name": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
