# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAircraftStatus(Tool):
    """
    A tool to update aircraft status.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], aircraft_id: str, new_status: str) -> str:
        aircraft_list = list(data.get("aircraft", {}).values())
        for aircraft in aircraft_list:
            if aircraft.get("aircraft_id") == aircraft_id:
                aircraft["status"] = new_status
                return json.dumps(aircraft)
        return json.dumps({"status": "Aircraft not found", "aircraft_id": aircraft_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_aircraft_status",
                "description": "Update aircraft status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {"type": "string", "description": "The aircraft ID."},
                        "new_status": {"type": "string", "description": "New status for the aircraft."}
                    },
                    "required": ["aircraft_id", "new_status"]
                }
            }
        }
