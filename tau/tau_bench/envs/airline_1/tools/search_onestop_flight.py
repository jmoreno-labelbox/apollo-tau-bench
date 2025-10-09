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

class SearchOnestopFlight(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], origin: str, destination: str, date: str) -> str:
        flights_data = data.get("flights", {}).values()
        results = []

        for flight1 in flights_data:
            if flight1.get("origin") == origin:
                date_info1 = flight1.get("dates", {}).values().get(date)
                if date_info1 and date_info1.get("status") == "available":
                    for flight2 in flights_data:
                        if flight2.get("destination") == destination and flight2.get(
                            "origin"
                        ) == flight1.get("destination"):
                            try:
                                arrival_time1 = datetime.strptime(
                                    flight1.get("scheduled_arrival_time_est", "").split(
                                        "+"
                                    )[0],
                                    "%H:%M:%S",
                                ).time()
                                departure_time2 = datetime.strptime(
                                    flight2.get(
                                        "scheduled_departure_time_est", ""
                                    ).split("+")[0],
                                    "%H:%M:%S",
                                ).time()

                                date2 = date
                                if arrival_time1 < departure_time2:
                                    date_info2 = flight2.get("dates", {}).values().get(date2)
                                    if (
                                        date_info2
                                        and date_info2.get("status") == "available"
                                    ):
                                        leg1 = {
                                            k: v
                                            for k, v in flight1.items()
                                            if k != "dates"
                                        }
                                        leg1.update(date_info1)
                                        leg1["date"] = date

                                        leg2 = {
                                            k: v
                                            for k, v in flight2.items()
                                            if k != "dates"
                                        }
                                        leg2.update(date_info2)
                                        leg2["date"] = date2

                                        results.append([leg1, leg2])
                            except ValueError:
                                continue
        payload = results
        out = json.dumps(payload)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchOnestopFlight",
                "description": "Search for one-stop connecting flights between two airports on a specific date.",
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
                            "description": "The date of the first flight in YYYY-MM-DD format.",
                        },
                    },
                    "required": ["origin", "destination", "date"],
                },
            },
        }
