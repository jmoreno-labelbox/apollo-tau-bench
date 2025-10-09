from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class AssignCourse(Tool):
    """Register a user in a course."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, course_id: str = None) -> str:
        uid = user_id
        cid = course_id
        log = data.setdefault("user_course_progress", [])
        log[:] = [r for r in log.values() if not (r["user_id"] == uid and r["course_id"] == cid)]
        log.append(
            {
                "user_id": uid,
                "course_id": cid,
                "enrolled_date": datetime.utcnow().date().isoformat(),
                "progress_percent": 0,
            }
        )
        payload = {"success": f"{uid} enrolled in {cid}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignCourse",
                "description": "Enroll user in course.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "course_id": {"type": "string"},
                    },
                    "required": ["user_id", "course_id"],
                },
            },
        }
