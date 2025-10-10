# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTeamDetailsById(Tool):
    """Fetch a team record by its team_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        team_id = kwargs.get("team_id")

        # 1) Validate
        if team_id is None:
            return json.dumps({"error": "Missing required field: team_id"}, indent=2)

        # 2) Get DB from passed-in data
        teams = data.get("teams", [])

        # 3) Exact match lookup
        for team in teams:
            if team.get("team_id") == team_id:
                return json.dumps(team, indent=2)

        return json.dumps({"error": f"No team found with ID {team_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_team_details_by_id",
                "description": "Fetch a single team's full details by its team_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {
                            "type": "integer",
                            "description": "Exact team ID to retrieve."
                        }
                    },
                    "required": ["team_id"]
                }
            }
        }
