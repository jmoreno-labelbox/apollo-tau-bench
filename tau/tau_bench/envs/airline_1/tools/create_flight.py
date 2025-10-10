# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateFlight(Tool):
    """
    A tool to create a new flight route.
    """
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        flight_number: str,
        origin: str,
        destination: str,
        scheduled_departure_time_est: str,
        scheduled_arrival_time_est: str
    ) -> str:
        flights_data = list(data.get("flights", {}).values())

        if any(f.get("flight_number") == flight_number for f in flights_data):
            return json.dumps({"error": f"Flight number {flight_number} already exists."})

        new_flight_route = {
            "flight_number": flight_number,
            "origin": origin,
            "destination": destination,
            "scheduled_departure_time_est": scheduled_departure_time_est,
            "scheduled_arrival_time_est": scheduled_arrival_time_est,
            "dates": {}
        }

        flights_data.append(new_flight_route)
        return json.dumps(new_flight_route)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_flight",
                "description": "Creates a new flight route with a unique flight number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string", "description": "The unique flight number (e.g., 'HAT301')."},
                        "origin": {"type": "string", "description": "The IATA code for the origin airport."},
                        "destination": {"type": "string", "description": "The IATA code for the destination airport."},
                        "scheduled_departure_time_est": {"type": "string", "description": "Scheduled departure time in HH:MM:SS format."},
                        "scheduled_arrival_time_est": {"type": "string", "description": "Scheduled arrival time in HH:MM:SS format."}
                    },
                    "required": ["flight_number", "origin", "destination", "scheduled_departure_time_est", "scheduled_arrival_time_est"]
                }
            }
        }
