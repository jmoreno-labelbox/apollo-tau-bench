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

class AssignAircraftToFlight(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any], flight_number: str, date: str, new_aircraft_id: str
    ) -> str:
        flights_data = data.get("flights", {}).values()
        for flight in flights_data:
            if flight.get("flight_number") == flight_number:
                if date in flight.get("dates", {}).values():
                    flight["dates"][date][
                        "notes"
                    ] = f"Aircraft reassigned to {new_aircraft_id}"
                    payload = {
                        "status": "success",
                        "flight_number": flight_number,
                        "date": date,
                        "new_aircraft_id": new_aircraft_id,
                    }
                    out = json.dumps(payload)
                    return out
        payload = {"error": "Flight not found on the specified date."}
        out = json.dumps(payload)
        return out
      

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignAircraftToFlight",
                "description": "Assigns a new aircraft to a specific flight instance.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "date": {
                            "type": "string",
                            "description": "Date in YYYY-MM-DD format.",
                        },
                        "new_aircraft_id": {
                            "type": "string",
                            "description": "The ID of the new aircraft.",
                        },
                    },
                    "required": ["flight_number", "date", "new_aircraft_id"],
                },
            },
        }
