from tau_bench.envs.tool import Tool
import json
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
        for c in data.get("crew_members", []):
            if c.get("crew_member_id") == crew_member_id:
                c["status"] = new_status
                return _j(c)
        return _j({"error": "crew_member_not_found", "crew_member_id": crew_member_id})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCrewMemberStatus",
                "description": "Set status on a crew member deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_member_id": {"type": "string"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["crew_member_id", "new_status"],
                },
            },
        }
