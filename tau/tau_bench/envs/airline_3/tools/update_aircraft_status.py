from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateAircraftStatus(Tool):
    """
    A tool for updating the status of an aircraft.
    """

    @staticmethod
    def invoke(data: dict[str, Any], aircraft_id: str, new_status: str) -> str:
        aircraft_list = data.get("aircraft", [])
        for aircraft in aircraft_list:
            if aircraft.get("aircraft_id") == aircraft_id:
                aircraft["status"] = new_status
                payload = aircraft
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
                "name": "UpdateAircraftStatus",
                "description": "Update aircraft status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {
                            "type": "string",
                            "description": "The aircraft ID.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status for the aircraft.",
                        },
                    },
                    "required": ["aircraft_id", "new_status"],
                },
            },
        }
