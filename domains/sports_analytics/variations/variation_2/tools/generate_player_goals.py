from tau_bench.envs.tool import Tool
import json
from typing import Any

class GeneratePlayerGoals(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        goal_count_per_player = kwargs.get("goal_count_per_player", 2)
        payload = {"player_goals": f"goals_per_player_{goal_count_per_player}"}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GeneratePlayerGoals",
                "description": "Generates personalized development goals for players.",
                "parameters": {
                    "type": "object",
                    "properties": {"goal_count_per_player": {"type": "integer"}},
                    "required": [],
                },
            },
        }
