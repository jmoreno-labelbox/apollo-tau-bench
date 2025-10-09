from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AddAccessCheck(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], check: dict = None) -> str:
        new_check = check or {}
        checks = data.get("access_checks", [])
        checks.append(new_check)
        data["access_checks"] = checks
        payload = {"added_check": new_check}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddAccessCheck",
                "description": "Add a new access check.",
                "parameters": {
                    "type": "object",
                    "properties": {"check": {"type": "object"}},
                    "required": ["check"],
                },
            },
        }
