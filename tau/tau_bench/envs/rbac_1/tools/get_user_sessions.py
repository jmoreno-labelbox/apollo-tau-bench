from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetUserSessions(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        user_sessions = [
            s for s in data.get("sessions", []) if s.get("user_id") == user_id
        ]
        user_sessions.sort(key=lambda x: x["start_time"], reverse=True)
        payload = {"sessions": user_sessions}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserSessions",
                "description": "Retrieves recent session information for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
