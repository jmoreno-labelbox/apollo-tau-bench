from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ScanFlightsByDate(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        date: str,
        flight_numbers: list[str] | None = None,
        origin: str | None = None,
        destination: str | None = None,
        status: list[str] | None = None,
    ) -> str:
        out = []
        for f in data.get("flights", []):
            day = (f.get("dates") or {}).get(date)
            if not isinstance(day, dict):
                continue
            if origin and f.get("origin") != origin:
                continue
            if destination and f.get("destination") != destination:
                continue
            if status and day.get("status") not in set(status):
                continue
            if flight_numbers and f.get("flight_number") not in set(flight_numbers):
                continue
            out.append(
                {
                    "flight_number": f.get("flight_number"),
                    "origin": f.get("origin"),
                    "destination": f.get("destination"),
                    "date": date,
                    "status": day.get("status"),
                    "scheduled_departure_time_est": f.get(
                        "scheduled_departure_time_est"
                    ),
                }
            )
        # organize by scheduled time followed by flight number
        out.sort(
            key=lambda x: (
                x.get("scheduled_departure_time_est", ""),
                x.get("flight_number", ""),
            )
        )
        return _j(out)

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ScanFlightsByDate",
                "description": "Search flights by date with optional origin/destination/status filters; sorted by scheduled_departure_time_est.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {"type": "string"},
                        "flight_numbers": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "origin": {"type": "string"},
                        "destination": {"type": "string"},
                        "status": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["date"],
                },
            },
        }
