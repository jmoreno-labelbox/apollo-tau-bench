# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetFlightByNumber(Tool):
    """
    A tool to retrieve flight details by flight number and date.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], flight_number: str, date: str) -> str:
        flights_data = list(data.get("flights", {}).values())
        for flight in flights_data:
            if flight.get("flight_number") == flight_number and date in flight["dates"]:
                result = flight.copy()
                result["date_info"] = result["dates"][date]
                del result["dates"]
                return json.dumps(result)
        return json.dumps({"error": "Flight not found", "flight_number": flight_number, "date": date})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_flight_by_number",
                "description": "Retrieves the full details of a specific flight on a given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {
                            "type": "string",
                            "description": "The flight number (e.g., 'HAT170')."
                        },
                        "date": {
                            "type": "string",
                            "description": "The date of the flight in YYYY-MM-DD format."
                        }
                    },
                    "required": ["flight_number", "date"]
                }
            }
        }
