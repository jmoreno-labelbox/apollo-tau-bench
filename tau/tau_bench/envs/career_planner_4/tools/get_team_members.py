from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetTeamMembers(Tool):
    @staticmethod
    def invoke(data, team_id: str) -> str:
        for team in data.get("teams", {}).values():
            if team.get("team_id") == team_id:
                payload = {"team_members": team.get("team_members", [])}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": "Team not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getTeamMembers",
                "description": "Return the list of team members for a given team_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }
