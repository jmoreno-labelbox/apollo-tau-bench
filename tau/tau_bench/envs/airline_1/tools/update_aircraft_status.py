# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAircraftStatus(Tool):
    """
    A tool to update the operational status of an aircraft.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], aircraft_id: str, new_status: str) -> str:
        aircraft_list = list(data.get("aircraft", {}).values())
        for aircraft in aircraft_list:
            if aircraft.get("aircraft_id") == aircraft_id:
                aircraft["status"] = new_status
                return json.dumps(aircraft)
        return json.dumps({"error": "Aircraft not found", "aircraft_id": aircraft_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_aircraft_status",
                "description": "Updates the operational status of a specific aircraft.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {
                            "type": "string",
                            "description": "The unique ID of the aircraft to update."
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the aircraft (e.g., 'IN_MAINTENANCE', 'ACTIVE')."
                        }
                    },
                    "required": ["aircraft_id", "new_status"]
                }
            }
        }
