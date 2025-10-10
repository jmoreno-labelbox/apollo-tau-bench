# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_team_id_by_name(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_name: str) -> str:
        teams = data.get("teams", [])
        team = next(
            (t for t in teams if t.get("team_name", "").lower() == team_name.lower()),
            None,
        )
        if team:
            return json.dumps({"team_id": team["team_id"]}, indent=2)
        return json.dumps(
            {"error": f"Team with name '{team_name}' not found"}, indent=2
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_team_id_by_name",
                "description": "Find a team ID by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_name": {"type": "string"}},
                    "required": ["team_name"],
                },
            },
        }
