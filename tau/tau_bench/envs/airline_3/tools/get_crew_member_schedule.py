from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetCrewMemberSchedule(Tool):
    """
    A straightforward tool for retrieving a crew member's flight schedule.
    """

    @staticmethod
    def invoke(data: dict[str, Any], crew_id: str) -> str:
        crew_members = data.get("crew_members", {}).values()
        for crew in crew_members:
            if crew.get("crew_member_id") == crew_id:
                flight_log = crew.get("flight_log", [])
                payload = {
                    "crew_id": crew_id,
                    "name": f"{crew.get('first_name')} {crew.get('last_name')}",
                    "schedule": flight_log,
                }
                out = json.dumps(payload)
                return out
        payload = {"status": "Crew member not found", "crew_id": crew_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCrewMemberSchedule",
                "description": "Get a crew member's flight schedule and history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_id": {
                            "type": "string",
                            "description": "The crew member ID (e.g., CM001).",
                        }
                    },
                    "required": ["crew_id"],
                },
            },
        }
