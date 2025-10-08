from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class UpdateAircraftLocation(Tool):
    """
    A tool for updating the location of an aircraft.
    """

    @staticmethod
    def invoke(data: dict[str, Any], aircraft_id: str, new_location: str) -> str:
        aircraft_list = data.get("aircraft", [])
        airports = data.get("airports", [])

        # Locate the aircraft
        for aircraft in aircraft_list:
            if aircraft.get("aircraft_id") == aircraft_id:
                old_location = aircraft.get("location", {}).get("iata_code")

                # Locate the airport using the IATA code
                airport_found = False
                for airport in airports:
                    if airport.get("iata_code") == new_location:
                        aircraft["location"] = {
                            "airport_id": airport.get("airport_id"),
                            "iata_code": new_location,
                        }
                        aircraft["last_updated"] = datetime.now().isoformat()
                        airport_found = True
                        break

                if not airport_found:
                    payload = {
                        "status": "Airport not found",
                        "aircraft_id": aircraft_id,
                        "requested_location": new_location,
                    }
                    out = json.dumps(payload)
                    return out
                payload = {
                    "aircraft_id": aircraft_id,
                    "old_location": old_location,
                    "new_location": new_location,
                    "updated_at": aircraft["last_updated"],
                }
                out = json.dumps(payload)
                return out
        payload = {"status": "Aircraft not found", "aircraft_id": aircraft_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateAircraftLocation",
                "description": "Update aircraft location to a new airport by IATA code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {
                            "type": "string",
                            "description": "The aircraft ID.",
                        },
                        "new_location": {
                            "type": "string",
                            "description": "New airport IATA code for the aircraft location.",
                        },
                    },
                    "required": ["aircraft_id", "new_location"],
                },
            },
        }
