from tau_bench.envs.tool import Tool
import json
from typing import Any

class Pitchers(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], team_id: int = None) -> str:
        #Deterministic placeholder: provide two pitchers for team 13, otherwise return empty
        if team_id == 13:
            payload = {"probable_pitcher_ids": [101, 102]}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"probable_pitcher_ids": []}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        pass
        #return result
        return {
            "type": "function",
            "function": {
                "name": "findPitch",
                "description": "Provides opponent probable pitcher IDs.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }
