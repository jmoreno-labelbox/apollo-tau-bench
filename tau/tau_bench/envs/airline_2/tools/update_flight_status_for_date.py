from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateFlightStatusForDate(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        flight_numbers: list[str] | None,
        date: str,
        new_status: str,
    ) -> str:
        _new_statusL = new_status or ''.lower()
        for f in data.get("flights", []):
            if f.get("flight_number") not in set(flight_numbers):
                continue
            day = (f.get("dates") or {}).get(date)
            if not isinstance(day, dict):
                return _j(
                    {
                        "error": "date_not_found",
                        "flight_number": flight_numbers,
                        "date": date,
                    }
                )
            day["status"] = new_status.lower()
            return _j(
                {
                    "flight_numbers": flight_numbers,
                    "date": date,
                    "status": new_status.lower(),
                }
            )
        return _j({"error": "flight_not_found", "flight_number": flight_numbers})
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateFlightStatusForDate",
                "description": "Set per-day status on a flight_number's date entry deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_numbers": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "date": {"type": "string"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["flight_numbers", "date", "new_status"],
                },
            },
        }
