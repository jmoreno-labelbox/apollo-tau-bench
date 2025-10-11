# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_crash_event_details(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], crash_id: str) -> str:
        crash_events = data.get("crash_events", [])
        for event in crash_events:
            if event.get("id") == crash_id:
                return json.dumps(event, indent=2)
        return json.dumps({"error": f"Crash event with id '{crash_id}' not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "get_crash_event_details", "description": "Retrieves the full details for a given crash event.", "parameters": { "type": "object", "properties": { "crash_id": { "type": "string" } }, "required": ["crash_id"] } } }
