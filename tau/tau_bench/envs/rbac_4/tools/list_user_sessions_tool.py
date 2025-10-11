# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListUserSessionsTool(Tool):
    """List sessions for a specific user with optional active-only filter (read operation, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], user_id, active_only = False) -> str:
        sessions = data.get("sessions", [])
        if not isinstance(sessions, list):
            return json.dumps({"error": "sessions must be a list"}, indent=2)

        if not isinstance(user_id, str) or not user_id.strip():
            return json.dumps({"error": "user_id must be a non-empty string"}, indent=2)

        if active_only not in (True, False):
            return json.dumps({"error": "active_only must be a boolean if provided"}, indent=2)

        results = []
        for s in sessions:
            if s.get("user_id") != user_id:
                continue
            if active_only and s.get("end_time") is not None:
                continue
            results.append(s)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_user_sessions",
                "description": "List sessions for a user; optionally filter to only active sessions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Target user_id"},
                        "active_only": {"type": "boolean", "description": "If true, only return sessions without end_time"}
                    },
                    "required": ["user_id"]
                }
            }
        }
