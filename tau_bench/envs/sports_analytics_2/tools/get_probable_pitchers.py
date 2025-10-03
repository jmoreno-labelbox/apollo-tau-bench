from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetProbablePitchers(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        team_id = kwargs.get("team_id")
        #Deterministic stub: provide two pitchers for team 13, otherwise return empty
        if team_id == 13:
            payload = {"probable_pitcher_ids": [101, 102]}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"probable_pitcher_ids": []}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProbablePitchers",
                "description": "Returns opponent probable pitcher IDs.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }
