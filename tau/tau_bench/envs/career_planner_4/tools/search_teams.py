from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class SearchTeams(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        filters: Any = None,
        team_id: str = None
    ) -> str:
        teams = data.get("teams", [])
        if team_id is not None:
            team = next(
                (t for t in teams if t.get("team_id") == team_id), None
            )
            return (
                json.dumps(team, indent=2)
                if team
                else json.dumps({"error": "Team not found"}, indent=2)
            )
        payload = {"teams": teams}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "searchTeams",
                "description": "Search for teams by filters",
                "parameters": {
                    "type": "object",
                    "properties": {"filters": {"type": "object"}},
                    "required": ["filters"],
                },
            },
        }
