from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RemoveAccessCheck(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], check_id: str = None) -> str:
        checks = data.get("access_checks", {}).values()
        data["access_checks"] = [c for c in checks.values() if c.get("check_id") != check_id]
        payload = {"removed_check_id": check_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveAccessCheck",
                "description": "Remove an access check by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"check_id": {"type": "string"}},
                    "required": ["check_id"],
                },
            },
        }
