from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class CreateAccessRequestTool(Tool):
    """CreateAccessRequest"""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        request_id: str,
        user_id: str,
        resource_id: str,
        requested_role_id: str,
        justification: str
,
    submitted_at: Any = None,
    ) -> str:
        req = {
            "request_id": request_id,
            "user_id": user_id,
            "resource_id": resource_id,
            "role": requested_role_id,
            "requested_role_id": requested_role_id,
            "justification": justification,
            "submitted_at": _HARD_TS,
            "status": "PENDING",
            "reviewed_by": None,
            "decision_notes": None,
            "decision_at": None,
        }
        ar = data.setdefault("access_requests", [])
        existing = next(
            (r for r in ar if r.get("request_id") == req["request_id"]), None
        )
        if existing is None:
            ar.append(req)
            out = req
        else:
            out = existing
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAccessRequest",
                "description": "Append a new access request (status=PENDING).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "resource_id": {"type": "string"},
                        "requested_role_id": {"type": "string"},
                        "justification": {"type": "string"},
                        "submitted_at": {"type": "string"},
                    },
                    "required": [
                        "request_id",
                        "user_id",
                        "resource_id",
                        "requested_role_id",
                        "justification",
                        "submitted_at",
                    ],
                },
            },
        }
