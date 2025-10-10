# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTeamMembers(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_id) -> str:
        teams = data.get("teams", [])

        for t in teams:
            if t["team_id"] == team_id:
                return json.dumps({"user_ids": t.get("team_members", [])}, indent=2)

        return json.dumps(
            {
                "error": "Team not found",
                "team_id": team_id,
                "available_teams": [t["team_id"] for t in teams],
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_team_members",
                "description": "Returns a list of user IDs belonging to a specific team.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {
                            "type": "string",
                            "description": "The team ID to search for.",
                        }
                    },
                    "required": ["team_id"],
                },
            },
        }
