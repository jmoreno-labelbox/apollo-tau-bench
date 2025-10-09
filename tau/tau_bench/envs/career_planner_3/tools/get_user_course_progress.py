from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetUserCourseProgress(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        progress_data = data.get("user_course_progress", [])

        user_progress = [p for p in progress_data if p.get("user_id") == user_id]
        payload = user_progress
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getUserCourseProgress",
                "description": "Retrieves the course progress for a given user, including completed, in-progress, and assigned courses.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
