# © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class Aims(Tool):
    @staticmethod
        # primary execution function
    def invoke(data: Dict[str, Any], goal_count_per_player = 2) -> str:
        # return output
        return json.dumps({"player_goals": f"goals_per_player_{goal_count_per_player}"}, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # return outcome
        return {"type": "function", "function": {"name": "aimsplay", "description": "Creates personalized development goals for players.", "parameters": {"type": "object", "properties": {"goal_count_per_player": {"type": "integer"}}, "required": []}}}
