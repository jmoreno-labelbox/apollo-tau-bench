from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class GetTeam(Tool):
    @staticmethod
    def invoke(data, team_id: str) -> str:
        for team in data.get("teams", []):
            if team.get("team_id") == team_id:
                payload = team
                out = json.dumps(payload, indent=2)
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
                "name": "getTeam",
                "description": "Fetch team details using the provided team_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }
