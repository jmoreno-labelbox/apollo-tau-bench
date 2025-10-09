from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListPolicyExceptionsTool(Tool):
    """Display exceptions to policies."""

    @staticmethod
    def invoke(data: dict[str, Any], status: str = None, user_id: str = None, completed_on: Any = None,
    permission_id: Any = None,
    ) -> str:
        exes = data.get("policy_exceptions", [])
        results = []
        for e in exes:
            if status and e["status"] != status:
                continue
            if user_id and e["user_id"] != user_id:
                continue
            results.append(e)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListPolicyExceptions",
                "description": "List policy exceptions optionally filtered by status or user_id",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {"type": "string"},
                        "user_id": {"type": "string"},
                    },
                },
            },
        }
