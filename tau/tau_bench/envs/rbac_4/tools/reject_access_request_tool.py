# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RejectAccessRequestTool(Tool):
    """Reject an access request."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rid = kwargs.get("request_id")
        reviewer = kwargs.get("reviewer_id")
        decision_at = kwargs.get("decision_at")
        for req in data.get("access_requests", []):
            if req["request_id"] == rid:
                req["status"] = "REJECTED"
                req["reviewed_by"] = reviewer
                req["decision_at"] = decision_at
                return json.dumps({"success": f"Request {rid} rejected"}, indent=2)
        return json.dumps({"error": f"Request {rid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reject_access_request",
                "description": "Reject a pending access request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "reviewer_id": {"type": "string"},
                        "decision_at": {"type": "string"}
                    },
                    "required": ["request_id", "reviewer_id", "decision_at"]
                }
            }
        }
