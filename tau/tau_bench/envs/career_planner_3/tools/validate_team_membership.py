# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ValidateTeamMembership(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        team_id = kwargs.get("team_id")
        teams = data.get("teams", [])

        for team in teams:
            if team["team_id"] == team_id:
                members = team.get("team_members", [])
                if user_id in members:
                    return json.dumps(
                        {"valid": True, "team_name": team.get("team_name")}, indent=2
                    )
                else:
                    return json.dumps(
                        {"valid": False, "reason": "User not in team"}, indent=2
                    )

        return json.dumps({"valid": False, "reason": "Team not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "validate_team_membership",
                "description": "Validates that a user is a member of a specific team.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user to validate.",
                        },
                        "team_id": {
                            "type": "string",
                            "description": "The team to check membership in.",
                        },
                    },
                    "required": ["user_id", "team_id"],
                },
            },
        }
