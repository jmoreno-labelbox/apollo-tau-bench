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
        payload = {"error": "Crew member not found", "crew_member_id": crew_member_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCrewMemberStatus",
                "description": "Updates the operational status of a specific crew member (e.g., to 'ON_SICK_LEAVE').",
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
