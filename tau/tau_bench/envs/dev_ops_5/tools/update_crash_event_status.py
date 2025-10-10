# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCrashEventStatus(Tool):
    """Updates the status of a crash event."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        crash_id = kwargs.get("id")
        new_status = kwargs.get("status")
        crashes = data.get("crash_events", [])
        for crash in crashes:
            if crash.get("id") == crash_id:
                crash["status"] = new_status
                return json.dumps({"status": "success", "message": f"Status for crash '{crash_id}' updated to '{new_status}'."})
        return json.dumps({"error": f"Crash with ID '{crash_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_crash_event_status",
                "description": "Updates the status of a crash event.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "status": {"type": "string"}
                    },
                    "required": ["id", "status"],
                },
            },
        }
