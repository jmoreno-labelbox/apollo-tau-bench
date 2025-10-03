from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetTeamDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        team_id = kwargs.get("team_id")
        team = next(
            (t for t in data.get("teams", []) if t.get("team_id") == team_id), None
        )
        payload = team or {}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTeamDetails",
                "description": "Gets details for a team id.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "integer"}},
                    "required": ["team_id"],
                },
            },
        }
