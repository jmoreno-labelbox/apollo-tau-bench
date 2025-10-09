from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any

class UpdateAircraftStatus(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], aircraft_id: str, new_status: str) -> str:
        aircraft_list = data.get("aircraft", [])
        for aircraft in aircraft_list:
            if aircraft.get("aircraft_id") == aircraft_id:
                aircraft["status"] = new_status
                payload = aircraft
                out = json.dumps(payload)
                return out
        payload = {"error": "Aircraft not found", "aircraft_id": aircraft_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAircraftStatus",
                "description": "Updates the operational status of a specific aircraft.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {
                            "type": "string",
                            "description": "The unique ID of the aircraft to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the aircraft (e.g., 'IN_MAINTENANCE', 'ACTIVE').",
                        },
                    },
                    "required": ["aircraft_id", "new_status"],
                },
            },
        }
