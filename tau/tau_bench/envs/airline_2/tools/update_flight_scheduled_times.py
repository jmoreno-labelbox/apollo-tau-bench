from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateFlightScheduledTimes(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        flight_number: str,
        scheduled_departure_time_est: str | None = None,
        scheduled_arrival_time_est: str | None = None,
    ) -> str:
        pass
        for f in data.get("flights", {}).values():
            if f.get("flight_number") != flight_number:
                continue
            #update solely the fields that are supplied
            if scheduled_departure_time_est is not None:
                f["scheduled_departure_time_est"] = scheduled_departure_time_est
            if scheduled_arrival_time_est is not None:
                f["scheduled_arrival_time_est"] = scheduled_arrival_time_est
            return _j(
                {
                    "flight_number": flight_number,
                    "scheduled_departure_time_est": f.get(
                        "scheduled_departure_time_est"
                    ),
                    "scheduled_arrival_time_est": f.get("scheduled_arrival_time_est"),
                }
            )
        return _j({"error": "flight_not_found", "flight_number": flight_number})

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateFlightScheduledTimes",
                "description": "Update the estimated scheduled departure/arrival times for a flight (top-level schedule fields).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "scheduled_departure_time_est": {
                            "type": "string",
                            "description": "Time-only (24-hour): HH:MM:SS",
                        },
                        "scheduled_arrival_time_est": {
                            "type": "string",
                            "description": "Time-only (24-hour): HH:MM:SS",
                        },
                    },
                    "required": ["flight_number"],
                },
            },
        }
