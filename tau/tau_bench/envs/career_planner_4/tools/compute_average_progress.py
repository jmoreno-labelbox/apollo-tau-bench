from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ComputeAverageProgress(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        progress = data.get("user_course_progress", [])
        user_courses = [p for p in progress if p.get("user_id") == user_id]
        if not user_courses:
            payload = {"average_progress": 0}
            out = json.dumps(payload, indent=2)
            return out

        total_progress = sum(p.get("current_progress_percent", 0) for p in user_courses)
        average = total_progress / len(user_courses)
        payload = {"average_progress": average, "user_id": user_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "computeAverageProgress",
                "description": "Compute average course progress for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
