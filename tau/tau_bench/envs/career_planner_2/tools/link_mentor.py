from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class LinkMentor(Tool):
    """Connect a mentor with a mentee."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, mentor_id: str = None) -> str:
        uid = user_id
        mid = mentor_id
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
        payload = {"success": f"Mentor {mid} -> {uid}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LinkMentor",
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
