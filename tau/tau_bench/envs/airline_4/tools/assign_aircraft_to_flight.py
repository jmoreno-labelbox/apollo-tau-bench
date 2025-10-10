# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignAircraftToFlight(Tool):
    """
    A tool to assign a specific aircraft to a flight on a given date.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], flight_number: str, date: str, new_aircraft_id: str) -> str:
        flights_data = list(data.get("flights", {}).values())
        for flight in flights_data:
            if flight.get("flight_number") == flight_number:
                if date in flight.get("dates", {}):
                    flight["dates"][date]["notes"] = f"Aircraft reassigned to {new_aircraft_id}"
                    return json.dumps({"status": "success",
                                       "flight_number": flight_number,
                                       "date": date,
                                       "new_aircraft_id": new_aircraft_id})
        return json.dumps({"error": "Flight not found on the specified date."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_aircraft_to_flight",
                "description": "Assigns a new aircraft to a specific flight instance.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "date": {"type": "string", "description": "Date in YYYY-MM-DD format."},
                        "new_aircraft_id": {"type": "string", "description": "The ID of the new aircraft."}
                    },
                    "required": ["flight_number", "date", "new_aircraft_id"]
                }
            }
        }
