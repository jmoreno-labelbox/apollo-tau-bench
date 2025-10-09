from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any

class UpdateAircraftLocation(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        aircraft_id: str, 
        new_location_airport_id: str
    ) -> str:
        aircraft_list = data.get("aircraft", [])
        airports = data.get("airports", [])
        
        target_airport = next(
            (a for a in airports if a.get("airport_id") == new_location_airport_id),
            None,
        )
        if not target_airport:
            payload = {
                "error": "Destination airport not found",
                "airport_id": new_location_airport_id,
            }
            out = json.dumps(payload)
            return out

        target_aircraft = next(
            (ac for ac in aircraft_list if ac.get("aircraft_id") == aircraft_id), None
        )
        if not target_aircraft:
            payload = {"error": "Aircraft not found", "aircraft_id": aircraft_id}
            out = json.dumps(payload)
            return out

        target_aircraft["location"] = {
            "airport_id": target_airport["airport_id"],
            "iata_code": target_airport["iata_code"],
        }
        payload = target_aircraft
        out = json.dumps(payload)
        return out
           

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAircraftLocation",
                "description": "Updates the current physical location of a specific aircraft to a new airport.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {
                            "type": "string",
                            "description": "The unique ID of the aircraft to update.",
                        },
                        "new_location_airport_id": {
                            "type": "string",
                            "description": "The unique airport ID of the aircraft's new location.",
                        },
                    },
                    "required": ["aircraft_id", "new_location_airport_id"],
                },
            },
        }
