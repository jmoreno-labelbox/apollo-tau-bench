from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindFlightCrew(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], flight_number: str) -> str:
        assignments = data.get("flight_crew_assignments", {}).values()
        crew_results = [
            a.get("crew_member")
            for a in assignments.values() if a.get("flight", {}).values().get("flight_number") == flight_number
        ]
        payload = list({v["crew_member_id"]: v for v in crew_results}.values())
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindFlightCrew",
                "description": "Finds all crew members assigned to a flight, identified by its flight number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {
                            "type": "string",
                            "description": "The flight number to search for (e.g., 'HAT004').",
                        }
                    },
                    "required": ["flight_number"],
                },
            },
        }
