from tau_bench.envs.tool import Tool
import json
from typing import Any

class SaveModelRecord(Tool):
    """Adds a models record."""

    @staticmethod
    def invoke(data: dict[str, Any], record: dict[str, Any]) -> str:
        req = {
            "model_name",
            "model_type",
            "training_ts",
            "model_path",
            "feature_names",
            "target_name",
        }
        if not req.issubset(set(record.keys())):
            payload = {"error": "missing required fields"}
            out = json.dumps(payload)
            return out
        data.setdefault("models", []).append(record)
        payload = {"status": "inserted", "model_name": record.get("model_name")}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "saveModelRecord",
                "description": "Appends a models record.",
                "parameters": {
                    "type": "object",
                    "properties": {"record": {"type": "object"}},
                    "required": ["record"],
                },
            },
        }
