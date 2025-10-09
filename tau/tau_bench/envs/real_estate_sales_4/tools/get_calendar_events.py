from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetCalendarEvents(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], date: str = None) -> str:
        if date:
            payload = {
                "date": date,
                "events": [
                    {"title": "Meeting", "time": "10:00 AM"},
                    {"title": "Lunch", "time": "1:00 PM"},
                ],
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {
                "date": "today",
                "events": [{"title": "Team Sync", "time": "9:00 AM"}],
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
                "name": "getCalendarEvents",
                "description": "Retrieves calendar events, optionally for a specific date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "The date for which to retrieve events (e.g., '2025-08-23').",
                        }
                    },
                    "required": [],
                },
            },
        }
