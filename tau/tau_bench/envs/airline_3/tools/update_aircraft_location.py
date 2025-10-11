# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAircraftLocation(Tool):
    """
    A tool to update aircraft location.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], aircraft_id: str, new_location: str) -> str:
        aircraft_list = list(data.get("aircraft", {}).values())
        airports = list(data.get("airports", {}).values())
        
        # Locate the aircraft.
        for aircraft in aircraft_list:
            if aircraft.get("aircraft_id") == aircraft_id:
                old_location = aircraft.get("location", {}).get("iata_code")
                
                # Locate the airport using its IATA code.
                airport_found = False
                for airport in airports:
                    if airport.get("iata_code") == new_location:
                        aircraft["location"] = {
                            "airport_id": airport.get("airport_id"),
                            "iata_code": new_location
                        }
                        aircraft["last_updated"] = datetime(2025, 9, 15, 0, 0, 0).isoformat().replace("+00:00", "Z")
                        airport_found = True
                        break
                
                if not airport_found:
                    return json.dumps({
                        "status": "Airport not found", 
                        "aircraft_id": aircraft_id,
                        "requested_location": new_location
                    })
                
                return json.dumps({
                    "aircraft_id": aircraft_id,
                    "old_location": old_location,
                    "new_location": new_location,
                    "updated_at": aircraft["last_updated"]
                })
        
        return json.dumps({"status": "Aircraft not found", "aircraft_id": aircraft_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_aircraft_location",
                "description": "Update aircraft location to a new airport by IATA code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {"type": "string", "description": "The aircraft ID."},
                        "new_location": {"type": "string", "description": "New airport IATA code for the aircraft location."}
                    },
                    "required": ["aircraft_id", "new_location"]
                }
            }
        }
