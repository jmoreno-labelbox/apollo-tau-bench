from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListActiveSessionsTool(Tool):
    """Provide sessions where end_time == null (active sessions). Optional user_id filter. Echo user_id for chaining."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, param1: str = None, param2: str = None) -> str:
        # Support param1 as alias for user_id
        user_id = user_id or param1
        sessions = data.get("sessions", {}).values()
        active = [s for s in sessions.values() if not s.get("end_time")]
        if user_id:
            active = [s for s in active.values() if s.get("user_id") == user_id]
        payload = {"user_id": user_id, "sessions": active}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listActiveSessions",
                "description": (
                    "List active sessions where end_time is null; optionally filter by user_id."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Optional user filter (e.g., U-030)",
                        }
                    },
                    "required": [],
                },
            },
        }
