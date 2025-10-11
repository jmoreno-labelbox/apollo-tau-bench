# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddCalendarEvent(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], end_time, start_time, title) -> str:
        return json.dumps({"status": "success", "event_title": title, "start": start_time, "end": end_time}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"add_calendar_event",
            "description":"Adds a new event to the calendar.",
            "parameters":{"type":"object","properties":{"title": {"type":"string"}, "start_time": {"type":"string"}, "end_time": {"type":"string"}},"required":["title", "start_time", "end_time"]}
        }}
