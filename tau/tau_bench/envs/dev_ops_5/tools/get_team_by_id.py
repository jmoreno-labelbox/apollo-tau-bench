from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetTeamById(Tool):
    """Fetches a team using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None) -> str:
        team_id = id
        teams = data.get("teams", [])
        for team in teams:
            if team.get("id") == team_id:
                payload = team
                out = json.dumps(payload)
                return out
        payload = {"error": f"Team with ID '{team_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTeamById",
                "description": "Retrieves a team by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }
