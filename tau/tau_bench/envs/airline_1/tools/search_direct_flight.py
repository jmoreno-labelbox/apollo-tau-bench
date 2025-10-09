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

class SearchDirectFlight(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], origin: str, destination: str, date: str) -> str:
        flights_data = data.get("flights", {}).values()
        results = []
        for flight_route in flights_data:
            if (
                flight_route.get("origin") == origin
                and flight_route.get("destination") == destination
            ):
                date_info = flight_route.get("dates", {}).values().get(date)
                if date_info and date_info.get("status") == "available":
                    flight_details = {
                        k: v for k, v in flight_route.items() if k != "dates"
                    }
                    flight_details.update(date_info)
                    flight_details["date"] = date
                    results.append(flight_details)
        payload = results
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchDirectFlight",
                "description": "Search for direct flights between two airports on a specific date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "origin": {
                            "type": "string",
                            "description": "The IATA code of the origin airport (e.g., 'JFK').",
                        },
                        "destination": {
                            "type": "string",
                            "description": "The IATA code of the destination airport (e.g., 'SEA').",
                        },
                        "date": {
                            "type": "string",
                            "description": "The date of the flight in YYYY-MM-DD format.",
                        },
                    },
                    "required": ["origin", "destination", "date"],
                },
            },
        }
