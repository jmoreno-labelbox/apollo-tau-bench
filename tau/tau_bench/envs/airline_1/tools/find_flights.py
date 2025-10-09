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

class FindFlights(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        departure_date: str,
        status: list[str],
        origin: str | None = None,
        destination: str | None = None,
    ) -> str:
        flights_data = data.get("flights", [])
        results = []

        for flight_route in flights_data:
            route_match = True
            if origin and flight_route.get("origin") != origin:
                route_match = False
            if destination and flight_route.get("destination") != destination:
                route_match = False

            if route_match:
                date_info = flight_route.get("dates", {}).get(departure_date)
                if date_info and date_info.get("status") in status:
                    flight_info = {
                        "flight_number": flight_route.get("flight_number"),
                        "origin": flight_route.get("origin"),
                        "destination": flight_route.get("destination"),
                        "date": departure_date,
                        "scheduled_departure_time_est": flight_route.get(
                            "scheduled_departure_time_est"
                        ),
                        "scheduled_arrival_time_est": flight_route.get(
                            "scheduled_arrival_time_est"
                        ),
                        "status": date_info.get("status"),
                        "available_seats": date_info.get("available_seats"),
                        "prices": date_info.get("prices"),
                    }
                    results.append(flight_info)
        payload = results
        out = json.dumps(payload)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindFlights",
                "description": "Finds flights based on origin, destination, departure date, and status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "departure_date": {
                            "type": "string",
                            "description": "The departure date in YYYY-MM-DD format.",
                        },
                        "status": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of flight statuses to search for (e.g., ['available']).",
                        },
                        "origin": {
                            "type": "string",
                            "description": "The IATA code of the origin airport.",
                        },
                        "destination": {
                            "type": "string",
                            "description": "The IATA code of the destination airport.",
                        },
                    },
                    "required": ["departure_date", "status"],
                },
            },
        }
