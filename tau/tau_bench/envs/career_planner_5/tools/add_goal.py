from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AddGoal(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, goal: dict[str, Any]) -> str:
        """Add a new goal to a user's profile."""
        for entry in data.get("goals", []):
            if entry["user_id"] == user_id:
                entry["goals"].append(goal)
                break
        else:  # no current goal list available for this user
            data.setdefault("goals", []).append({"user_id": user_id, "goals": [goal]})
        payload = {"success": f"goal {goal['goal_id']} added for {user_id}"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addGoal",
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
