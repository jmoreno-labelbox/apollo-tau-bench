from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateFlightStatus(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any], flight_number: str, date: str, new_status: str
    ) -> str:
        flights_data = data.get("flights", [])
        for flight_route in flights_data:
            if flight_route.get("flight_number") == flight_number:
                if date in flight_route.get("dates", {}):
                    flight_route["dates"][date]["status"] = new_status
                    payload = {
                        "flight_number": flight_number,
                        "date": date,
                        "new_status": new_status,
                    }
                    out = json.dumps(payload)
                    return out
        payload = {"error": "Flight not found", "flight_number": flight_number, "date": date}
        out = json.dumps(payload)
        return out
                    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateFlightStatus",
                "description": "Updates the status of a specific flight on a given date (e.g., 'cancelled', 'delayed').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {
                            "type": "string",
                            "description": "The flight number.",
                        },
                        "date": {
                            "type": "string",
                            "description": "The flight date in YYYY-MM-DD format.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status.",
                        },
                    },
                    "required": ["flight_number", "date", "new_status"],
                },
            },
        }
