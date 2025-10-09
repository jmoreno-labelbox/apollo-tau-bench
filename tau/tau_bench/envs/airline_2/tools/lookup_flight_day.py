from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class LookupFlightDay(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], date: str, flight_number: str | None = None
    ) -> str:
        for f in data.get("flights", {}).values():
            if flight_number and f.get("flight_number") != flight_number:
                continue
            day = (f.get("dates") or {}).get(date)
            if day is not None:
                # merge the main schedule with daily status and times
                out = {
                    "flight_number": f.get("flight_number"),
                    "origin": f.get("origin"),
                    "destination": f.get("destination"),
                    "scheduled_departure_time_est": f.get(
                        "scheduled_departure_time_est"
                    ),
                    "scheduled_arrival_time_est": f.get("scheduled_arrival_time_est"),
                    "date": date,
                    "day": day,
                }
                return _j(out)
        return _j({})


    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LookupFlightDay",
                "description": "Return combined schedule + per-day status for a flight_number on a specific date (YYYY-MM-DD).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {"type": "string"},
                        "flight_number": {"type": "string"},
                    },
                    "required": ["date"],
                },
            },
        }
