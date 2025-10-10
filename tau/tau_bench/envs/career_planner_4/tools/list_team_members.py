# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class list_team_members(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_id: str) -> str:
        teams = data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if team:
            members = team.get("members", [])
            return json.dumps({"members": members}, indent=2)
        return json.dumps({"error": "Team not found"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_team_members",
                "description": "List all members of a team",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }
