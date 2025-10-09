from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListSessionsTool(Tool):
    """Display user sessions with optional filtering."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, active_only: bool = None) -> str:
        sessions = data.get("sessions", [])
        results = []
        for s in sessions:
            if user_id and s["user_id"] != user_id:
                continue
            if active_only and s.get("end_time") is not None:
                continue
            results.append(s)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListSessions",
                "description": "List login sessions with optional user_id and active_only flag",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "active_only": {"type": "boolean"},
                    },
                },
            },
        }
