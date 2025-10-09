from tau_bench.envs.tool import Tool
import json
from typing import Any

class Aims(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], goal_count_per_player: int = 2) -> str:
        payload = {"player_goals": f"goals_per_player_{goal_count_per_player}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        pass
        #return result
        return {
            "type": "function",
            "function": {
                "name": "aimsplay",
                "description": "Creates personalized development goals for players.",
                "parameters": {
                    "type": "object",
                    "properties": {"goal_count_per_player": {"type": "integer"}},
                    "required": [],
                },
            },
        }
