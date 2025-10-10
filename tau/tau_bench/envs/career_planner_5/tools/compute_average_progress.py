# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class compute_average_progress(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        """Return the average completion percentage across all courses for a user."""
        records = [
            rec
            for rec in data.get("user_course_progress", [])
            if rec["user_id"] == user_id
        ]
        if not records:
            return json.dumps({"average_progress": 0})
        total, count = 0, 0
        for rec in records:
            if rec.get("status") == "Completed":
                total += 100
            else:
                total += rec.get("current_progress_percent", 0)
            count += 1
        avg = round(total / count, 2)
        return json.dumps({"average_progress": avg})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compute_average_progress",
                "description": "Calculate a user's average course completion percentage across all enrollments.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
