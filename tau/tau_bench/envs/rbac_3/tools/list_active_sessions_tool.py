# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListActiveSessionsTool(Tool):
    """Return sessions with end_time == null (active sessions). Optional user_id filter. Echo user_id for chaining."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        sessions = data.get("sessions", [])
        active = [s for s in sessions if not s.get("end_time")]
        if user_id:
            active = [s for s in active if s.get("user_id") == user_id]
        return json.dumps({"user_id": user_id, "sessions": active}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_active_sessions",
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
