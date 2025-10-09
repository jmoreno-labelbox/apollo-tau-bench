from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetAircraftByTailNumber(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], tail_number: str) -> str:
        aircraft_list = data.get("aircraft", [])
        for aircraft in aircraft_list:
            if aircraft.get("tail_number") == tail_number:
                payload = aircraft
                out = json.dumps(payload)
                return out
        payload = {"error": "Aircraft not found", "tail_number": tail_number}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAircraftByTailNumber",
                "description": "Retrieves the full details of an aircraft using its unique tail number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tail_number": {
                            "type": "string",
                            "description": "The unique tail number of the aircraft (e.g., 'G-ZNKH').",
                        }
                    },
                    "required": ["tail_number"],
                },
            },
        }
