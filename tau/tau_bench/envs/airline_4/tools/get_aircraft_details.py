from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetAircraftDetails(Tool):
    """API tool for obtaining complete aircraft details from 'aircraft.json' using the aircraft ID."""

    @staticmethod
    def invoke(data: dict[str, Any], aircraft_id: str) -> str:
        pass
        aircraft_list = data.get("aircraft", {}).values()
        for aircraft in aircraft_list.values():
            if aircraft.get("aircraft_id") == aircraft_id:
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
                "name": "GetAircraftDetails",
                "description": "Get full aircraft details using the aircraft ID from 'aircraft.json'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {
                            "type": "string",
                            "description": "Aircraft ID (e.g., 'AC001').",
                        }
                    },
                    "required": ["aircraft_id"],
                },
            },
        }
