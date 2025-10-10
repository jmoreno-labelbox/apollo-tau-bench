# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSessionDetailsById(Tool):
    """Get the full details of a specific session using its ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], session_id) -> str:
        try:
            sessions = data.get('sessions', [])
        except (KeyError, json.JSONDecodeError):
            sessions = []

        for session in sessions:
            if session.get("session_id") == session_id:
                return json.dumps(session)

        return json.dumps({"error": f"Session with ID '{session_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_session_details_by_id",
                "description": "Retrieves the full details of a specific user session using its unique ID (e.g., 'S-028').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "session_id": {
                            "type": "string",
                            "description": "The unique ID of the session to retrieve."
                        }
                    },
                    "required": ["session_id"]
                }
            }
        }
