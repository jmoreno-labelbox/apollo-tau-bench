from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetTeamByName(Tool):
    """Fetches a team using its name."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        teams = data.get("teams", [])
        for team in teams:
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
