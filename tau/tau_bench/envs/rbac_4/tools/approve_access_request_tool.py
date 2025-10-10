# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ApproveAccessRequestTool(Tool):
    """Approve an access request."""

    @staticmethod  # <-- required to match base class definition
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rid = kwargs.get("request_id")
        reviewer = kwargs.get("reviewer_id")
        decision_at = kwargs.get("decision_at")  # <-- new required argument!
        for req in data.get("access_requests", []):
            if req["request_id"] == rid:
                req["status"] = "APPROVED"
                req["reviewed_by"] = reviewer
                req["decision_at"] = decision_at   # <-- use argument, NOT hardcoded!
                return json.dumps({"success": f"Request {rid} approved"}, indent=2)
        return json.dumps({"error": f"Request {rid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "approve_access_request",
                "description": "Approve a pending access request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "reviewer_id": {"type": "string"},
                        "decision_at": {"type": "string"},  # <-- Add to properties!
                    },
                    "required": ["request_id", "reviewer_id", "decision_at"],  # <-- Add to required!
                }
            }
        }
