from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class SetPerformanceGoal(Tool):
    """Introduce a performance objective."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, goal: str = None) -> str:
        tbl = data.setdefault("goals", [])
        tbl.append({"user_id": user_id, "goals": [goal]})
        payload = {"success": f"Goal set for {user_id}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetPerformanceGoal",
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
