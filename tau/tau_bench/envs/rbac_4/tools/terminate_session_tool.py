from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class TerminateSessionTool(Tool):
    """End a particular user session."""

    @staticmethod
    def invoke(data: dict[str, Any], session_id: str = None, terminated_on: str = None) -> str:
        sid = session_id
        term_time = terminated_on
        for s in data.get("sessions", []):
            if s["session_id"] == sid:
                s["end_time"] = term_time
                payload = {"success": f"Session {sid} terminated"}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Session {sid} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "TerminateSession",
                "description": "Force terminate a session by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "session_id": {"type": "string"},
                        "terminated_on": {"type": "string"},
                    },
                    "required": ["session_id", "terminated_on"],
                },
            },
        }
