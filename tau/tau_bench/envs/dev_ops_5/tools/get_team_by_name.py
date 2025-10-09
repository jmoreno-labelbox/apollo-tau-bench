from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetTeamByName(Tool):
    """Fetches a team using its name."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        teams = data.get("teams", {}).values()
        for team in teams.values():
            if team.get("name") == name:
                payload = team
                out = json.dumps(payload)
                return out
        payload = {"error": f"Team with name '{name}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTeamByName",
                "description": "Retrieves a team by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
