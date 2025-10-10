# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetPerformanceGoal(Tool):
    """Add a performance goal."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        goal = kwargs.get("goal")
        tbl = data.setdefault("goals", [])
        tbl.append({"user_id": uid, "goals": [goal]})
        return json.dumps({"success": f"Goal set for {uid}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_performance_goal",
                "description": "Set performance goal.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "goal": {"type": "object"},
                    },
                    "required": ["user_id", "goal"],
                },
            },
        }
