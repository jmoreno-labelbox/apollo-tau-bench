# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCrew(Tool):
    """
    A tool to update basic crew information.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], crew_id: str, first_name: str = None, last_name: str = None, role: str = None, status: str = None) -> str:
        crew_list = data.get("crew_members", [])
        for crew in crew_list:
            if crew.get("crew_member_id") == crew_id:
                if first_name:
                    crew["first_name"] = first_name
                if last_name:
                    crew["last_name"] = last_name
                if role:
                    crew["role"] = role
                if status:
                    crew["status"] = status
                return json.dumps(crew)
        return json.dumps({"status": "Crew not found", "crew_id": crew_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_crew",
                "description": "Update basic crew information.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_id": {"type": "string", "description": "The crew ID."},
                        "first_name": {"type": "string", "description": "First name of the crew member."},
                        "last_name": {"type": "string", "description": "Last name of the crew member."},
                        "role": {"type": "string", "description": "Role of the crew member."},
                        "status": {"type": "string", "description": "Status of the crew member."}
                    },
                    "required": ["crew_id"]
                }
            }
        }
