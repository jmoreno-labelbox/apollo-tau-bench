from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateCrew(Tool):
    """
    A tool for updating fundamental crew information.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        crew_id: str,
        first_name: str = None,
        last_name: str = None,
        role: str = None,
        status: str = None,
    ) -> str:
        crew_list = data.get("crew_members", {}).values()
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
                payload = crew
                out = json.dumps(payload)
                return out
        payload = {"status": "Crew not found", "crew_id": crew_id}
        out = json.dumps(payload)
        return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCrew",
                "description": "Update basic crew information.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_id": {"type": "string", "description": "The crew ID."},
                        "first_name": {
                            "type": "string",
                            "description": "First name of the crew member.",
                        },
                        "last_name": {
                            "type": "string",
                            "description": "Last name of the crew member.",
                        },
                        "role": {
                            "type": "string",
                            "description": "Role of the crew member.",
                        },
                        "status": {
                            "type": "string",
                            "description": "Status of the crew member.",
                        },
                    },
                    "required": ["crew_id"],
                },
            },
        }
