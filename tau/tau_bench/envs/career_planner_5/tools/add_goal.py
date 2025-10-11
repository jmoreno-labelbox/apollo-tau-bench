# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class add_goal(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, goal: Dict[str, Any]) -> str:
        """Append a new goal to a user's record."""
        for entry in data.get("goals", []):
            if entry["user_id"] == user_id:
                entry["goals"].append(goal)
                break
        else:  # this user does not have a current goal list
            data.setdefault("goals", []).append({"user_id": user_id, "goals": [goal]})
        return json.dumps({"success": f"goal {goal['goal_id']} added for {user_id}"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_goal",
                "description": "Add a new goal object to the specified user.",
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
