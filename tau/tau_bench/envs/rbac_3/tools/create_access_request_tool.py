# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAccessRequestTool(Tool):
    """create_access_request"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = {
            "request_id": kwargs["request_id"],
            "user_id": kwargs["user_id"],
            "resource_id": kwargs["resource_id"],
            "role": kwargs["requested_role_id"],
            "requested_role_id": kwargs["requested_role_id"],
            "justification": kwargs["justification"],
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
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_access_request",
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
