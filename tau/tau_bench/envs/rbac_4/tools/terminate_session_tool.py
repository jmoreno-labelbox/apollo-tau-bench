# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class TerminateSessionTool(Tool):
    """Terminate a specific user session."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sid = kwargs.get("session_id")
        term_time = kwargs.get("terminated_on")
        for s in data.get("sessions", []):
            if s["session_id"] == sid:
                s["end_time"] = term_time
                return json.dumps({"success": f"Session {sid} terminated"}, indent=2)
        return json.dumps({"error": f"Session {sid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "terminate_session",
                "description": "Force terminate a session by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "session_id": {"type": "string"},
                        "terminated_on": {"type": "string"}
                    },
                    "required": ["session_id", "terminated_on"]
                }
            }
        }
