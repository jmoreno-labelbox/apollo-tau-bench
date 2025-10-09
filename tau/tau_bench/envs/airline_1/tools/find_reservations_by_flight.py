from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any

class FindReservationsByFlight(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], flight_number: str, date: str) -> str:
        reservations = data.get("reservations", [])
        matching_reservations = []
        for res in reservations:
            for flight in res.get("flights", []):
                if (
                    flight.get("flight_number") == flight_number
                    and flight.get("date") == date
                ):
                    matching_reservations.append(res)
                    break
        payload = matching_reservations
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindReservationsByFlight",
                "description": "Finds all reservations for a specific flight number on a given date.",
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
