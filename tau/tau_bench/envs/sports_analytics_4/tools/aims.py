# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class Aims(Tool):
    @staticmethod
        # main invoke function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        goal_count_per_player = kwargs.get("goal_count_per_player", 2)
        # return result
        return json.dumps({"player_goals": f"goals_per_player_{goal_count_per_player}"}, indent=2)

    @staticmethod
        # info metadata
    def get_info() -> Dict[str, Any]:
        # return result
        return {"type": "function", "function": {"name": "aimsplay", "description": "Creates personalized development goals for players.", "parameters": {"type": "object", "properties": {"goal_count_per_player": {"type": "integer"}}, "required": []}}}
