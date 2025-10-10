# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class conditional_enroll_or_list(Tool):
    @staticmethod
    def invoke(
        data,
        user_id: str,
        course_id: str,
        goal_id: str,
        threshold: int,
        enroll_date: str,
    ) -> str:
        # Placeholder condition: if the numeric component of user_id is odd, emulate enrollment.
        if int(user_id[1:]) % 2 == 1:
            # Emulate user enrollment and goal modification.
            # (In a practical application, we would verify the ongoing status using data.)
            return json.dumps(
                {
                    "result": f"User {user_id} enrolled in {course_id} and goal {goal_id} updated to {threshold}%."
                },
                indent=2,
            )
        else:
            # Alternatively, mimic the retrieval of a list of active enrollments.
            return json.dumps(
                {
                    "result": f"User {user_id} already meets threshold; enrollments listed."
                },
                indent=2,
            )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "conditional_enroll_or_list",
                "description": "Conditionally enroll a user in a course if their goal progress is below a threshold; otherwise, list current enrollments.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "course_id": {"type": "string"},
                        "goal_id": {"type": "string"},
                        "threshold": {"type": "integer"},
                        "enroll_date": {"type": "string"},
                    },
                    "required": [
                        "user_id",
                        "course_id",
                        "goal_id",
                        "threshold",
                        "enroll_date",
                    ],
                },
            },
        }
