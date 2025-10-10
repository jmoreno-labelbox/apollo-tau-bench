# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateFlightStatus(Tool):
    """
    A tool to update the status of a flight on a specific date.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], flight_number: str, date: str, new_status: str) -> str:
        flights_data = list(data.get("flights", {}).values())
        new_status = new_status.upper()
        for flight_route in flights_data:
            if flight_route.get("flight_number") == flight_number:
                if date in flight_route.get("dates", {}):
                    flight_route["dates"][date]["status"] = new_status
                    return json.dumps({"flight_number": flight_number, "date": date, "new_status": new_status})
        return json.dumps({"error": "Flight not found", "flight_number": flight_number, "date": date})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_flight_status",
                "description": "Updates the status of a specific flight on a given date (e.g., 'cancelled', 'delayed').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string", "description": "The flight number."},
                        "date": {"type": "string", "description": "The flight date in YYYY-MM-DD format."},
                        "new_status": {"type": "string", "description": "The new status."}
                    },
                    "required": ["flight_number", "date", "new_status"]
                }
            }
        }
