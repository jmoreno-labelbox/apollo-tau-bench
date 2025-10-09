from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class EventsAtAirportOn(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], airport_id: str, date: str) -> str:
        out = []
        for e in data.get("operational_events", []):
            ap = (e.get("airport") or {}).get("airport_id")
            ts = e.get("event_timestamp_utc", "")
            if ap == airport_id and isinstance(ts, str) and ts[:10] == date:
                out.append(e)
        return _j(out)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EventsAtAirportOn",
                "description": "Return operational events at an airport on a date (UTC).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "airport_id": {"type": "string"},
                        "date": {"type": "string"},
                    },
                    "required": ["airport_id", "date"],
                },
            },
        }
