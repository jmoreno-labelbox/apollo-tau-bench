from tau_bench.envs.tool import Tool
import json
from typing import Any

class ValidateTeamMembership(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, team_id: str = None) -> str:
        teams = data.get("teams", [])

        for team in teams:
            if team["team_id"] == team_id:
                members = team.get("team_members", [])
                if user_id in members:
                    payload = {"valid": True, "team_name": team.get("team_name")}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
                else:
                    payload = {"valid": False, "reason": "User not in team"}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
        payload = {"valid": False, "reason": "Team not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ValidateTeamMembership",
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
