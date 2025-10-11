# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAccessRequestStatusTool(Tool):
    """update_access_request_status: approve/reject with notes and audit."""

    @staticmethod
    def invoke(data: Dict[str, Any], approve, notes, request_id, reviewer_id, status) -> str:
        if status is not None and approve is None:
            approve = True if str(status).upper() == "APPROVED" else False
        return ReviewAccessRequestTool.invoke(
            data,
            request_id=request_id,
            reviewer_id=reviewer_id,
            approve=approve,
            notes=notes,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_access_request_status",
                "description": (
                    "Approve or reject an access request with reviewer notes and audit."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "reviewer_id": {"type": "string"},
                        "approve": {"type": "boolean"},
                        "status": {"type": "string"},
                        "notes": {"type": "string"},
                    },
                    "required": ["request_id", "reviewer_id"],
                },
            },
        }
