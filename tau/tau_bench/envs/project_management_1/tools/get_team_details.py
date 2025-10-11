# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTeamDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_id, team_name) -> str:

        if not team_name and not team_id:
            return json.dumps({"error": "Either team_name or team_id is required"})

        teams = data.get("teams", [])

        for team in teams:
            if (team_id and team.get("team_id") == team_id) or (
                team_name and team.get("team_name") == team_name
            ):
                return json.dumps(team, indent=2)

        return json.dumps({"error": f"Team not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_team_details",
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
