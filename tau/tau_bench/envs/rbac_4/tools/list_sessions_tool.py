# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListSessionsTool(Tool):
    """List user sessions with optional filters."""

    @staticmethod
    def invoke(data: Dict[str, Any], active_only, user_id) -> str:
        uid = user_id
        sessions = data.get("sessions", [])
        results = []
        for s in sessions:
            if uid and s["user_id"] != uid:
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
                "name": "list_sessions",
                "description": "List login sessions with optional user_id and active_only flag",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "active_only": {"type": "boolean"}
                    }
                }
            }
        }
