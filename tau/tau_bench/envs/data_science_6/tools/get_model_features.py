from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetModelFeatures(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], model_name: str = None) -> str:
        if not model_name:
            payload = {"error": "Missing model_name"}
            out = json.dumps(payload)
            return out
        for rec in data.get("models", {}).values():
            if rec.get("model_name") == model_name:
                payload = {
                    "model_name": model_name,
                    "feature_names": rec.get("feature_names", []),
                }
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
                "name": "GetModelFeatures",
                "description": "Returns required feature_names for a model_name from models.",
                "parameters": {
                    "type": "object",
                    "properties": {"model_name": {"type": "string"}},
                    "required": ["model_name"],
                },
            },
        }
