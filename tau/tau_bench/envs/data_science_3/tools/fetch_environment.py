from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FetchEnvironment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        env = data.get("environment", {}).values() or {}
        payload = env
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getEnvironment",
                "description": "Read environment variables/secrets map.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
