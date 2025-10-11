# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAccessRequestTool(Tool):
    """Fetch a single access request record by ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], request_id) -> str:
        if not request_id:
            return json.dumps({"error": "request_id is required"}, indent=2)

        requests: List[Dict[str, Any]] = data.get("access_requests", [])
        rec = next((r for r in requests if r.get("request_id") == request_id), None)
        if rec is None:
            return json.dumps(
                {"error": f"Access request {request_id} not found"}, indent=2
            )

        # standardize dimensions and ensure reliable defaults
        out = {
            "request_id": rec.get("request_id", request_id),
            "user_id": rec.get("user_id"),
            "resource_id": rec.get("resource_id"),
            "requested_role_id": rec.get("requested_role_id"),
            "justification": rec.get("justification"),
            "submitted_at": rec.get("submitted_at"),
            "status": rec.get("status"),
            "reviewed_by": rec.get("reviewed_by"),
            "decision_notes": rec.get("decision_notes"),
            "decision_at": rec.get("decision_at"),
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_access_request",
                "description": "Return a single access request by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": (
                                "Unique access request identifier (e.g., AR-008)"
                            ),
                        }
                    },
                    "required": ["request_id"],
                },
            },
        }
