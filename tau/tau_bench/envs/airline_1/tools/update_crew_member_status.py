# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCrewMemberStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], crew_member_id: str, new_status: str) -> str:
        crew_members = list(data.get("crew_members", {}).values())
        new_status = new_status.upper()
        for member in crew_members:
            if member.get("crew_member_id") == crew_member_id:
                member["status"] = new_status
                return json.dumps(member)
        return json.dumps({"error": "Crew member not found", "crew_member_id": crew_member_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_crew_member_status",
                "description": "Updates the operational status of a specific crew member (e.g., to 'ON_SICK_LEAVE').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_member_id": {
                            "type": "string",
                            "description": "The unique ID of the crew member to update."
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the crew member."
                        }
                    },
                    "required": ["crew_member_id", "new_status"]
                }
            }
        }
