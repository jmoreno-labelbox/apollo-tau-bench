# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindReservationsByFlight(Tool):
    """
    A tool to find all reservations for a specific flight on a given date.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], flight_number: str, date: str) -> str:
        reservations = list(data.get("reservations", {}).values())
        matching_reservations = []
        for res in reservations:
            for flight in res.get("flights", []):
                if flight.get("flight_number") == flight_number and flight.get("date") == date:
                    matching_reservations.append(res)
                    break
        return json.dumps(matching_reservations)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_reservations_by_flight",
                "description": "Finds all reservations for a specific flight number on a given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string", "description": "The flight number (e.g., 'HAT170')."},
                        "date": {"type": "string", "description": "The date of the flight in YYYY-MM-DD format."}
                    },
                    "required": ["flight_number", "date"]
                }
            }
        }
