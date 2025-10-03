from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any

class GetSessionDetailsById(Tool):
    """Retrieve complete details of a specific session by its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], session_id: str = None) -> str:
        try:
            sessions = data.get("sessions", [])
        except (KeyError, json.JSONDecodeError):
            sessions = []

        for session in sessions:
            if session.get("session_id") == session_id:
                payload = session
                out = json.dumps(payload)
                return out
        payload = {"error": f"Session with ID '{session_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSessionDetailsById",
                "description": "Retrieves the full details of a specific user session using its unique ID (e.g., 'S-028').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "session_id": {
                            "type": "string",
                            "description": "The unique ID of the session to retrieve.",
                        }
                    },
                    "required": ["session_id"],
                },
            },
        }
