from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ReadSystemConfigTool(Tool):
    """Retrieve a configuration by key and return restricted fields (avoid large blobs)."""

    @staticmethod
    def invoke(data: dict[str, Any], config_key: str = None) -> str:
        config_key = _require_str(config_key, "config_key")
        if not config_key:
            payload = {"error": "config_key is required"}
            out = json.dumps(payload)
            return out

        rows = data.get("system_config", [])
        for r in rows:
            if r.get("config_key") == config_key:
                payload = {
                    "config_key": r.get("config_key"),
                    "sample": (r.get("config_value_json") or "")[:200],
                }
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"config_key {config_key} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReadSystemConfig",
                "description": "Return a preview of the config value by key (first 200 chars).",
                "parameters": {
                    "type": "object",
                    "properties": {"config_key": {"type": "string"}},
                    "required": ["config_key"],
                },
            },
        }
