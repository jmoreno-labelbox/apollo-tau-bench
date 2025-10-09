from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetTeamDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], team_name: str = None, team_id: str = None) -> str:
        if not team_name and not team_id:
            payload = {"error": "Either team_name or team_id is required"}
            out = json.dumps(payload)
            return out

        teams = data.get("teams", [])

        for team in teams:
            if (team_id and team.get("team_id") == team_id) or (
                team_name and team.get("team_name") == team_name
            ):
                payload = team
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Team not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTeamDetails",
                "description": "Get details of a specific team",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_name": {"type": "string", "description": "Team name"},
                        "team_id": {"type": "string", "description": "Team ID"},
                    },
                },
            },
        }
