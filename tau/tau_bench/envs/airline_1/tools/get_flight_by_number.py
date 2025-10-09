from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetFlightByNumber(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], flight_number: str, date: str) -> str:
        flights_data = data.get("flights", {}).values()
        for flight in flights_data:
            if flight.get("flight_number") == flight_number and date in flight["dates"]:
                result = flight.copy()
                result["date_info"] = result["dates"][date]
                del result["dates"]
                payload = result
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
                "name": "GetFlightByNumber",
                "description": "Retrieves the full details of a specific flight on a given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {
                            "type": "string",
                            "description": "The flight number (e.g., 'HAT170').",
                        },
                        "date": {
                            "type": "string",
                            "description": "The date of the flight in YYYY-MM-DD format.",
                        },
                    },
                    "required": ["flight_number", "date"],
                },
            },
        }
