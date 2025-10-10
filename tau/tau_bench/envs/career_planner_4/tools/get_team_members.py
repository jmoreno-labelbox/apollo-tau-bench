# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_team_members(Tool):
    @staticmethod
    def invoke(data, team_id: str) -> str:
        for team in data.get("teams", []):
            if team.get("team_id") == team_id:
                return json.dumps(
                    {"team_members": team.get("team_members", [])}, indent=2
                )
        return json.dumps({"error": "Team not found"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_team_members",
                "description": "Return the list of team members for a given team_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }
