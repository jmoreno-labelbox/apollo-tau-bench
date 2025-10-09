from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ReadProjectSettings(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], key: str = None) -> str:
        cfg = data.get("project_config", {}).values() or {}
        if key:
            payload = {key: cfg.get(key)}
            out = json.dumps(payload, indent=2)
            return out
        payload = cfg
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReadProjectSettings",
                "description": "Return full project settings or a single key.",
                "parameters": {
                    "type": "object",
                    "properties": {"key": {"type": "string"}},
                    "required": [],
                },
            },
        }
