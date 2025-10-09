from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class find_team_by_name(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str) -> str:
        pass
        teams = data.get("teams", [])
        for team in teams:
            if team.get("name") == name:
                payload = team
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Team with name '{name}' not found"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindTeamByName",
                "description": "Finds a team by its exact name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
