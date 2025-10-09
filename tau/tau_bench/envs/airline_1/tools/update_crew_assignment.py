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

class UpdateCrewAssignment(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        assignment_id: str,
        new_crew_member_id: str,
        new_crew_member_full_name: str,
    ) -> str:
        assignments = data.get("flight_crew_assignments", [])
        for assignment in assignments:
            if assignment.get("assignment_id") == assignment_id:
                assignment["crew_member"] = {
                    "crew_member_id": new_crew_member_id,
                    "full_name": new_crew_member_full_name,
                }
                payload = {
                    "status": "success",
                    "assignment_id": assignment_id,
                    "new_crew_member_id": new_crew_member_id,
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Assignment not found", "assignment_id": assignment_id}
        out = json.dumps(payload)
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCrewAssignment",
                "description": "Updates an existing flight crew assignment with a new crew member.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "assignment_id": {
                            "type": "string",
                            "description": "The unique ID of the assignment to update (e.g., 'AS001').",
                        },
                        "new_crew_member_id": {
                            "type": "string",
                            "description": "The unique ID of the new crew member.",
                        },
                        "new_crew_member_full_name": {
                            "type": "string",
                            "description": "The full name of the new crew member.",
                        },
                    },
                    "required": [
                        "assignment_id",
                        "new_crew_member_id",
                        "new_crew_member_full_name",
                    ],
                },
            },
        }
