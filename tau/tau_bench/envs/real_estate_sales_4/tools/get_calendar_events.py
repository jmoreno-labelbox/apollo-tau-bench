# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCalendarEvents(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        date = kwargs.get("date")
        if date:
            return json.dumps({"date": date, "events": [{"title": "Meeting", "time": "10:00 AM"}, {"title": "Lunch", "time": "1:00 PM"}]}, indent=2)
        else:
            return json.dumps({"date": "today", "events": [{"title": "Team Sync", "time": "9:00 AM"}]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_calendar_events",
            "description":"Retrieves calendar events, optionally for a specific date.",
            "parameters":{"type":"object","properties":{"date": {"type":"string", "description": "The date for which to retrieve events (e.g., '2025-08-23')."}},"required":[]}
        }}
