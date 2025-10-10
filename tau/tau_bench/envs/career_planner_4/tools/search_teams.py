# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class search_teams(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], filters: dict) -> str:
        teams = data.get("teams", [])
        if "team_id" in filters:
            team = next(
                (t for t in teams if t.get("team_id") == filters["team_id"]), None
            )
            return (
                json.dumps(team, indent=2)
                if team
                else json.dumps({"error": "Team not found"}, indent=2)
            )
        return json.dumps({"teams": teams}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "search_teams",
                "description": "Search for teams by filters",
                "parameters": {
                    "type": "object",
                    "properties": {"filters": {"type": "object"}},
                    "required": ["filters"],
                },
            },
        }
