# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class add_team_member(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_id: str, user_id: str) -> str:
        teams = data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if team:
            team_members = team.setdefault("team_members", [])
            if user_id not in team_members:
                team_members.append(user_id)
                return json.dumps(
                    {"success": f"User {user_id} added to team {team_id}"}, indent=2
                )
            else:
                return json.dumps(
                    {"success": f"User {user_id} already in team {team_id}"}, indent=2
                )
        return json.dumps({"error": "Team not found"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "add_team_member",
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
