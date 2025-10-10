# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindCrewMember(Tool):
    """
    A tool to find a crew member by name, employee code, or crew member ID.
    """

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        employee_code: Optional[str] = None,
        crew_member_id: Optional[str] = None
    ) -> str:
        crew_members = list(data.get("crew_members", {}).values())

        if employee_code:
            for crew_member in crew_members:
                if crew_member.get("employee_code") == employee_code:
                    return json.dumps(crew_member)
            return json.dumps({"error": "Crew member not found", "employee_code": employee_code})

        if crew_member_id:
            for crew_member in crew_members:
                if crew_member.get("crew_member_id") == crew_member_id:
                    return json.dumps(crew_member)
            return json.dumps({"error": "Crew member not found", "crew_member_id": crew_member_id})

        if first_name and last_name:
            results = [
                c for c in crew_members
                if c.get("first_name") == first_name and c.get("last_name") == last_name
            ]
            return json.dumps(results)

        return json.dumps({"error": "Insufficient search parameters. Provide either employee_code, crew_member_id, or both first_name and last_name."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_crew_member",
                "description": "Finds a crew member by employee code, crew member ID, or full name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_code": {
                            "type": "string",
                            "description": "The unique employee code of the crew member."
                        },
                        "crew_member_id": {
                            "type": "string",
                            "description": "The unique crew member ID."
                        },
                        "first_name": {
                            "type": "string",
                            "description": "The first name of the crew member."
                        },
                        "last_name": {
                            "type": "string",
                            "description": "The last name of the crew member."
                        }
                    },
                    "required": [],
                }
            }
        }
