# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GeneratePlayerGoals(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], goal_count_per_player = 2) -> str:
        return json.dumps({"player_goals": f"goals_per_player_{goal_count_per_player}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "generate_player_goals", "description": "Generates personalized development goals for players.", "parameters": {"type": "object", "properties": {"goal_count_per_player": {"type": "integer"}}, "required": []}}}
