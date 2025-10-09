from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListUserGoals(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        goals_data = data.get("goals", {}).values()
        user_goals = next((g for g in goals_data.values() if g.get("user_id") == user_id), {}).values()
        goals = user_goals.get("goals", [])
        payload = {"user_id": user_id, "goals": goals}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListUserGoals",
                "description": "List all goals for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
