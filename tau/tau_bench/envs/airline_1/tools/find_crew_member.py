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

class FindCrewMember(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        first_name: str | None = None,
        last_name: str | None = None,
        employee_code: str | None = None,
        crew_member_id: str | None = None,
    ) -> str:
        crew_members = data.get("crew_members", {}).values()

        if employee_code:
            for crew_member in crew_members:
                if crew_member.get("employee_code") == employee_code:
                    payload = crew_member
                    out = json.dumps(payload)
                    return out
            payload = {"error": "Crew member not found", "employee_code": employee_code}
            out = json.dumps(payload)
            return out

        if crew_member_id:
            for crew_member in crew_members:
                if crew_member.get("crew_member_id") == crew_member_id:
                    payload = crew_member
                    out = json.dumps(payload)
                    return out
            payload = {"error": "Crew member not found", "crew_member_id": crew_member_id}
            out = json.dumps(payload)
            return out

        if first_name and last_name:
            results = [
                c
                for c in crew_members.values() if c.get("first_name") == first_name and c.get("last_name") == last_name
            ]
            payload = results
            out = json.dumps(payload)
            return out
        payload = {
            "error": "Insufficient search parameters. Provide either employee_code, crew_member_id, or both first_name and last_name."
        }
        out = json.dumps(payload)
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCrewMember",
                "description": "Finds a crew member by employee code, crew member ID, or full name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_code": {
                            "type": "string",
                            "description": "The unique employee code of the crew member.",
                        },
                        "crew_member_id": {
                            "type": "string",
                            "description": "The unique crew member ID.",
                        },
                        "first_name": {
                            "type": "string",
                            "description": "The first name of the crew member.",
                        },
                        "last_name": {
                            "type": "string",
                            "description": "The last name of the crew member.",
                        },
                    },
                    "required": [],
                },
            },
        }
