# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCrashEventById(Tool):
    """Retrieves a crash event by its ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], id) -> str:
        crash_id = id
        crashes = data.get("crash_events", [])
        for crash in crashes:
            if crash.get("id") == crash_id:
                return json.dumps(crash)
        return json.dumps({"error": f"Crash event with ID '{crash_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_crash_event_by_id",
                "description": "Retrieves a crash event by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }
