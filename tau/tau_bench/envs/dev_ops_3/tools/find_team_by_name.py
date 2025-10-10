# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class find_team_by_name(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], name: str) -> str:
        teams = data.get("teams", [])
        for team in teams:
            if team.get("name") == name:
                return json.dumps(team, indent=2)
        return json.dumps({"error": f"Team with name '{name}' not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "find_team_by_name", "description": "Finds a team by its exact name.", "parameters": { "type": "object", "properties": { "name": { "type": "string" } }, "required": ["name"] } } }
