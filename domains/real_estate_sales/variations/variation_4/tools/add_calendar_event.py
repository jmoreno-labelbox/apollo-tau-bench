from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddCalendarEvent(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], title: str = None, start_time: str = None, end_time: str = None) -> str:
        payload = {
            "status": "success",
            "event_title": title,
            "start": start_time,
            "end": end_time,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addCalendarEvent",
                "description": "Adds a new event to the calendar.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "start_time": {"type": "string"},
                        "end_time": {"type": "string"},
                    },
                    "required": ["title", "start_time", "end_time"],
                },
            },
        }
