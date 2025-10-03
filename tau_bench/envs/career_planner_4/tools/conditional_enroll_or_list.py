from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class ConditionalEnrollOrList(Tool):
    @staticmethod
    def invoke(
        data,
        user_id: str,
        course_id: str,
        goal_id: str,
        threshold: int,
        enroll_date: str,
    ) -> str:
        pass
        #Placeholder condition: if the numeric portion of user_id is odd, mimic enrollment.
        if int(user_id[1:]) % 2 == 1:
            payload = {
                    "result": f"User {user_id} enrolled in {course_id} and goal {goal_id} updated to {threshold}%."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {
                    "result": f"User {user_id} already meets threshold; enrollments listed."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "conditionalEnrollOrList",
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
