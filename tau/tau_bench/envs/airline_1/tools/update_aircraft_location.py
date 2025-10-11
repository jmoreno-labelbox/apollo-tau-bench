# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAircraftLocation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], aircraft_id: str, new_location_airport_id: str) -> str:
        aircraft_list = list(data.get("aircraft", {}).values())
        airports = list(data.get("airports", {}).values())

        target_airport = next((a for a in airports if a.get("airport_id") == new_location_airport_id), None)
        if not target_airport:
            return json.dumps({"error": "Destination airport not found", "airport_id": new_location_airport_id})

        target_aircraft = next((ac for ac in aircraft_list if ac.get("aircraft_id") == aircraft_id), None)
        if not target_aircraft:
            return json.dumps({"error": "Aircraft not found", "aircraft_id": aircraft_id})

        target_aircraft["location"] = {
            "airport_id": target_airport["airport_id"],
            "iata_code": target_airport["iata_code"]
        }

        return json.dumps(target_aircraft)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_aircraft_location",
                "description": "Updates the current physical location of a specific aircraft to a new airport.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {
                            "type": "string",
                            "description": "The unique ID of the aircraft to update."
                        },
                        "new_location_airport_id": {
                            "type": "string",
                            "description": "The unique airport ID of the aircraft's new location."
                        }
                    },
                    "required": ["aircraft_id", "new_location_airport_id"]
                }
            }
        }
