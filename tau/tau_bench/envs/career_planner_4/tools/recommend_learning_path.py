# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class recommend_learning_path(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        user_id: str,
        soft_skill: str,
        course_id: str,
        enroll_date: str,
        goal_id: str,
        progress_percent: int,
    ) -> str:
        # Record the suggestion.
        recommendation = {
            "user_id": user_id,
            "soft_skill": soft_skill,
            "course_id": course_id,
            "enroll_date": enroll_date,
            "goal_id": goal_id,
            "progress_percent": progress_percent,
        }
        data.setdefault("learning_path_recommendations", []).append(recommendation)
        return json.dumps(
            {"success": f"Learning path recommended for {user_id} in {soft_skill}"},
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "recommend_learning_path",
                "description": "Recommend a learning path for a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "soft_skill": {"type": "string"},
                        "course_id": {"type": "string"},
                        "enroll_date": {"type": "string"},
                        "goal_id": {"type": "string"},
                        "progress_percent": {"type": "integer"},
                    },
                    "required": [
                        "user_id",
                        "soft_skill",
                        "course_id",
                        "enroll_date",
                        "goal_id",
                        "progress_percent",
                    ],
                },
            },
        }
