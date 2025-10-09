from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListUsersTool(Tool):
    """Display users with optional filtering."""

    @staticmethod
    def invoke(data: dict[str, Any], department: str = None, status: str = None, mfa_enabled: bool = None) -> str:
        users = data.get("users", [])

        results = []
        for u in users:
            if department and u["department"] != department:
                continue
            if status and u["status"] != status:
                continue
            if mfa_enabled is not None and u["mfa_enabled"] != mfa_enabled:
                continue
            results.append(u)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListUsers",
                "description": "List users with optional filters",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {"type": "string"},
                        "status": {"type": "string"},
                        "mfa_enabled": {"type": "boolean"},
                    },
                },
            },
        }
