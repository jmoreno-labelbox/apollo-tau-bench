# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchOnestopFlight(Tool):
    """
    A tool to search for available one-stop flight itineraries.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], origin: str, destination: str, date: str) -> str:
        flights_data = list(data.get("flights", {}).values())
        results = []

        for flight1 in flights_data:
            if flight1.get("origin") == origin:
                date_info1 = flight1.get("dates", {}).get(date)
                if date_info1 and date_info1.get("status") == "available":
                    for flight2 in flights_data:
                        if flight2.get("destination") == destination and flight2.get("origin") == flight1.get("destination"):
                            try:
                                arrival_time1 = datetime.strptime(flight1.get("scheduled_arrival_time_est", "").split('+')[0], "%H:%M:%S").time()
                                departure_time2 = datetime.strptime(flight2.get("scheduled_departure_time_est", "").split('+')[0], "%H:%M:%S").time()

                                date2 = date
                                if arrival_time1 < departure_time2:
                                    date_info2 = flight2.get("dates", {}).get(date2)
                                    if date_info2 and date_info2.get("status") == "available":
                                        leg1 = {k: v for k, v in flight1.items() if k != "dates"}
                                        leg1.update(date_info1)
                                        leg1["date"] = date

                                        leg2 = {k: v for k, v in flight2.items() if k != "dates"}
                                        leg2.update(date_info2)
                                        leg2["date"] = date2

                                        results.append([leg1, leg2])
                            except ValueError:
                                continue
        return json.dumps(results)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_onestop_flight",
                "description": "Search for one-stop connecting flights between two airports on a specific date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "origin": {"type": "string", "description": "The IATA code of the origin airport (e.g., 'JFK')."},
                        "destination": {"type": "string", "description": "The IATA code of the destination airport (e.g., 'SEA')."},
                        "date": {"type": "string", "description": "The date of the first flight in YYYY-MM-DD format."}
                    },
                    "required": ["origin", "destination", "date"]
                }
            }
        }
