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

class FindCrewAssignments(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any], crew_member_id: str, flight_number: str | None = None
    ) -> str:
        assignments = data.get("flight_crew_assignments", [])
        results = [
            a
            for a in assignments
            if a["crew_member"]["crew_member_id"] == crew_member_id
        ]
        if flight_number:
            results = [
                a for a in results if a["flight"]["flight_number"] == flight_number
            ]
        payload = results
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCrewAssignments",
                "description": "Finds all flight assignments for a given crew member.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_member_id": {
                            "type": "string",
                            "description": "The unique ID of the crew member.",
                        },
                        "flight_number": {
                            "type": "string",
                            "description": "Optional: Filter assignments by a specific flight number.",
                        },
                    },
                    "required": ["crew_member_id"],
                },
            },
        }
