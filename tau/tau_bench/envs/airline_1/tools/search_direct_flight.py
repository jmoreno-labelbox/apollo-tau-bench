# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchDirectFlight(Tool):
    """
    A tool to search for available direct flights.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], origin: str, destination: str, date: str) -> str:
        flights_data = list(data.get("flights", {}).values())
        results = []
        for flight_route in flights_data:
            if flight_route.get("origin") == origin and flight_route.get("destination") == destination:
                date_info = flight_route.get("dates", {}).get(date)
                if date_info and date_info.get("status") == "available":
                    flight_details = {k: v for k, v in flight_route.items() if k != "dates"}
                    flight_details.update(date_info)
                    flight_details["date"] = date
                    results.append(flight_details)
        return json.dumps(results)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_direct_flight",
                "description": "Search for direct flights between two airports on a specific date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "origin": {"type": "string", "description": "The IATA code of the origin airport (e.g., 'JFK')."},
                        "destination": {"type": "string", "description": "The IATA code of the destination airport (e.g., 'SEA')."},
                        "date": {"type": "string", "description": "The date of the flight in YYYY-MM-DD format."}
                    },
                    "required": ["origin", "destination", "date"]
                }
            }
        }
