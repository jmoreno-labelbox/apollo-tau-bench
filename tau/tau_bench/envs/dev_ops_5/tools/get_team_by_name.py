# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTeamByName(Tool):
    """Retrieves a team by its name."""
    @staticmethod
    def invoke(data: Dict[str, Any], name) -> str:
        teams = data.get("teams", [])
        for team in teams:
            if team.get("name") == name:
                return json.dumps(team)
        return json.dumps({"error": f"Team with name '{name}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_team_by_name",
                "description": "Retrieves a team by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
