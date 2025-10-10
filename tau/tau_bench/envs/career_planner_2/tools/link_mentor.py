# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LinkMentor(Tool):
    """Link mentor to mentee."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        mid = kwargs.get("mentor_id")
        rel = data.setdefault("user_mentorship_relationships", [])
        rel[:] = [
            r for r in rel if not (r["mentee_id"] == uid and r["mentor_id"] == mid)
        ]
        rel.append(
            {
                "mentee_id": uid,
                "mentor_id": mid,
                "start_date": datetime.utcnow().date().isoformat(),
                "status": "Active",
            }
        )
        return json.dumps({"success": f"Mentor {mid} -> {uid}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "link_mentor",
                "description": "Link mentor.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "mentor_id": {"type": "string"},
                    },
                    "required": ["user_id", "mentor_id"],
                },
            },
        }
