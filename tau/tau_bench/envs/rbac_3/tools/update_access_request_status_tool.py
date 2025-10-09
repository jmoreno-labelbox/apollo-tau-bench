from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class UpdateAccessRequestStatusTool(Tool):
    """update_access_request_status: authorize/deny with comments and audit."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        status: str = None, 
        request_id: str = None, 
        reviewer_id: str = None, 
        approve: bool = None, 
        notes: str = None,
        decision_at: str = None
    ) -> str:
        # allow for either approval/notes or a clear status
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
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAccessRequestStatus",
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
