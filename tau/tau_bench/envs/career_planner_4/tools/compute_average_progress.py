# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class compute_average_progress(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        progress = data.get("user_course_progress", [])
        user_courses = [p for p in progress if p.get("user_id") == user_id]
        if not user_courses:
            return json.dumps({"average_progress": 0}, indent=2)

        total_progress = sum(p.get("current_progress_percent", 0) for p in user_courses)
        average = total_progress / len(user_courses)
        return json.dumps({"average_progress": average, "user_id": user_id}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "compute_average_progress",
                "description": "Compute average course progress for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
