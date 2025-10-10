# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignCourse(Tool):
    """Enroll user in course."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        cid = kwargs.get("course_id")
        log = data.setdefault("user_course_progress", [])
        log[:] = [r for r in log if not (r["user_id"] == uid and r["course_id"] == cid)]
        log.append(
            {
                "user_id": uid,
                "course_id": cid,
                "enrolled_date": datetime.utcnow().date().isoformat(),
                "progress_percent": 0,
            }
        )
        return json.dumps({"success": f"{uid} enrolled in {cid}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_course",
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
