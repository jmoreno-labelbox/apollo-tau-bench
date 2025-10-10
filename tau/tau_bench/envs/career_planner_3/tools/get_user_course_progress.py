# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserCourseProgress(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        progress_data = data.get("user_course_progress", [])

        user_progress = [p for p in progress_data if p.get("user_id") == user_id]

        return json.dumps(user_progress, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_course_progress",
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
