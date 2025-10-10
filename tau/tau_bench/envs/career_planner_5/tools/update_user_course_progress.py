# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_user_course_progress(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], user_id: str, course_id: str, updates: Dict[str, Any]
    ) -> str:
        rec = next(
            (
                r
                for r in data.get("user_course_progress", [])
                if r["user_id"] == user_id and r["course_id"] == course_id
            ),
            None,
        )
        if rec:
            rec.update(updates)
            return json.dumps({"success": "course progress updated"})
        return json.dumps({"error": "course enrollment not found"})

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "update_user_course_progress",
                "description": "Update an existing course-progress record for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "course_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["user_id", "course_id", "updates"],
                },
            },
        }
