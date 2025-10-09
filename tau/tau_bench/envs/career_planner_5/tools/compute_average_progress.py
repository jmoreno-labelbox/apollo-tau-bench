from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ComputeAverageProgress(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        """Provide the average completion rate for all courses associated with a user."""
        records = [
            rec
            for rec in data.get("user_course_progress", {}).values()
            if rec["user_id"] == user_id
        ]
        if not records:
            payload = {"average_progress": 0}
            out = json.dumps(payload)
            return out
        total, count = 0, 0
        for rec in records:
            if rec.get("status") == "Completed":
                total += 100
            else:
                total += rec.get("current_progress_percent", 0)
            count += 1
        avg = round(total / count, 2)
        payload = {"average_progress": avg}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "computeAverageProgress",
                "description": "Calculate a user's average course completion percentage across all enrollments.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
