from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddTeamMember(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], team_id: str, user_id: str) -> str:
        teams = data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if team:
            team_members = team.setdefault("team_members", [])
            if user_id not in team_members:
                team_members.append(user_id)
                payload = {"success": f"User {user_id} added to team {team_id}"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            else:
                payload = {"success": f"User {user_id} already in team {team_id}"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": "Team not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "addTeamMember",
                "description": "Add a team member to a team",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "user_id": {"type": "string"},
                    },
                    "required": ["team_id", "user_id"],
                },
            },
        }
