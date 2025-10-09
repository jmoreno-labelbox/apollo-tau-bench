from tau_bench.envs.tool import Tool
import json
from typing import Any

class SaveModelConfig(Tool):
    """Adds a model_config record."""

    @staticmethod
    def invoke(data: dict[str, Any], saved_json_path: str = None, created_ts: str = None) -> str:
        record = {"saved_json_path": saved_json_path, "created_ts": created_ts}
        req = {"saved_json_path", "created_ts"}
        if not req.issubset(set(record.keys())):
            payload = {"error": "missing required fields"}
            out = json.dumps(payload)
            return out
        data.setdefault("model_config", []).append(record)
        payload = {"status": "inserted", "saved_json_path": record.get("saved_json_path")}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "saveModelConfig",
                "description": "Appends a model_config record.",
                "parameters": {
                    "type": "object",
                    "properties": {"record": {"type": "object"}},
                    "required": ["record"],
                },
            },
        }
