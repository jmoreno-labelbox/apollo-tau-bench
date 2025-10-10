# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_team(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_id: str) -> str:
        teams = data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)
        return (
            json.dumps(team, indent=2)
            if team
            else json.dumps({"error": "Team not found"}, indent=2)
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_team",
                "description": "Get team details by team ID",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }
