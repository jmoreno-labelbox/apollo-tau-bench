# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCrewAssignment(Tool):
    """
    A tool to update an existing flight crew assignment with a new crew member.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], assignment_id: str, new_crew_member_id: str, new_crew_member_full_name: str) -> str:
        assignments = data.get("flight_crew_assignments", [])
        for assignment in assignments:
            if assignment.get("assignment_id") == assignment_id:
                assignment["crew_member"] = {
                    "crew_member_id": new_crew_member_id,
                    "full_name": new_crew_member_full_name
                }
                return json.dumps({"status": "success", "assignment_id": assignment_id, "new_crew_member_id": new_crew_member_id})
        return json.dumps({"error": "Assignment not found", "assignment_id": assignment_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_crew_assignment",
                "description": "Updates an existing flight crew assignment with a new crew member.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "assignment_id": {
                            "type": "string",
                            "description": "The unique ID of the assignment to update (e.g., 'AS001')."
                        },
                        "new_crew_member_id": {
                            "type": "string",
                            "description": "The unique ID of the new crew member."
                        },
                        "new_crew_member_full_name": {
                            "type": "string",
                            "description": "The full name of the new crew member."
                        }
                    },
                    "required": ["assignment_id", "new_crew_member_id", "new_crew_member_full_name"]
                }
            }
        }
