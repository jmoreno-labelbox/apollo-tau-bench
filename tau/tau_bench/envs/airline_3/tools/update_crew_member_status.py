from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class UpdateCrewMemberStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], crew_member_id: str, new_status: str) -> str:
        crew_members = data.get("crew_members", [])
        for member in crew_members:
            if member.get("crew_member_id") == crew_member_id:
                member["status"] = new_status
                payload = member
                out = json.dumps(payload)
                return out
        payload = {"status": "not_found", "crew_member_id": crew_member_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCrewMemberStatus",
                "description": "Updates the operational status of a specific crew member.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_member_id": {
                            "type": "string",
                            "description": "The unique ID of the crew member to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the crew member.",
                        },
                    },
                    "required": ["crew_member_id", "new_status"],
                },
            },
        }
