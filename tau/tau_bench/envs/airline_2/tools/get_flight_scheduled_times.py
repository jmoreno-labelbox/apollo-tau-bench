from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetFlightScheduledTimes(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], flight_number: str) -> str:
        for f in data.get("flights", []):
            if f.get("flight_number") == flight_number:
                return _j(
                    {
                        "flight_number": flight_number,
                        "scheduled_departure_time_est": f.get(
                            "scheduled_departure_time_est"
                        ),
                        "scheduled_arrival_time_est": f.get(
                            "scheduled_arrival_time_est"
                        ),
                    }
                )
        return _j({"error": "flight_not_found", "flight_number": flight_number})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFlightScheduledTimes",
                "description": "Return the estimated scheduled departure/arrival times for a flight.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                    },
                    "required": ["flight_number"],
                },
            },
        }
