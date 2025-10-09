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

class CreateFlight(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        flight_number: str,
        origin: str,
        destination: str,
        scheduled_departure_time_est: str,
        scheduled_arrival_time_est: str,
    ) -> str:
        flights_data = data.get("flights", {}).values()

        if any(f.get("flight_number") == flight_number for f in flights_data.values()):
            payload = {"error": f"Flight number {flight_number} already exists."}
            out = json.dumps(payload)
            return out

        new_flight_route = {
            "flight_number": flight_number,
            "origin": origin,
            "destination": destination,
            "scheduled_departure_time_est": scheduled_departure_time_est,
            "scheduled_arrival_time_est": scheduled_arrival_time_est,
            "dates": {},
        }

        data["flights"][new_flight_route["flight_id"]] = new_flight_route
        payload = new_flight_route
        out = json.dumps(payload)
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateFlight",
                "description": "Creates a new flight route with a unique flight number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {
                            "type": "string",
                            "description": "The unique flight number (e.g., 'HAT301').",
                        },
                        "origin": {
                            "type": "string",
                            "description": "The IATA code for the origin airport.",
                        },
                        "destination": {
                            "type": "string",
                            "description": "The IATA code for the destination airport.",
                        },
                        "scheduled_departure_time_est": {
                            "type": "string",
                            "description": "Scheduled departure time in HH:MM:SS format.",
                        },
                        "scheduled_arrival_time_est": {
                            "type": "string",
                            "description": "Scheduled arrival time in HH:MM:SS format.",
                        },
                    },
                    "required": [
                        "flight_number",
                        "origin",
                        "destination",
                        "scheduled_departure_time_est",
                        "scheduled_arrival_time_est",
                    ],
                },
            },
        }
