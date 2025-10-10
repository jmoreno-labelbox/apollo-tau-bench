# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTeamById(Tool):
    """Retrieves a team by its ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        team_id = kwargs.get("id")
        teams = data.get("teams", [])
        for team in teams:
            if team.get("id") == team_id:
                return json.dumps(team)
        return json.dumps({"error": f"Team with ID '{team_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_team_by_id",
                "description": "Retrieves a team by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }
