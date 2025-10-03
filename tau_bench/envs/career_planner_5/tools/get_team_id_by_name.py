from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetTeamIdByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], team_name: str) -> str:
        _team_nameL = team_name or ''.lower()
        pass
        teams = data.get("teams", [])
        team = next(
            (t for t in teams if t.get("team_name", "").lower() == team_name.lower()),
            None,
        )
        if team:
            payload = {"team_id": team["team_id"]}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": f"Team with name '{team_name}' not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getTeamIdByName",
                "description": "Find a team ID by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_name": {"type": "string"}},
                    "required": ["team_name"],
                },
            },
        }
