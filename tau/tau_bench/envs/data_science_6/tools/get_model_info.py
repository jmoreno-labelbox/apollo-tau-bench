from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetModelInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], model_name: str = None) -> str:
        if not model_name:
            payload = {"error": "Missing model_name"}
            out = json.dumps(payload)
            return out
        for rec in data.get("models", []):
            if rec.get("model_name") == model_name:
                payload = {"model_name": model_name, "model_path": rec.get("model_path")}
                out = json.dumps(payload)
                return out
        payload = {}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetModelInfo",
                "description": "Returns model artifact info such as model_path for a model_name.",
                "parameters": {
                    "type": "object",
                    "properties": {"model_name": {"type": "string"}},
                    "required": ["model_name"],
                },
            },
        }
