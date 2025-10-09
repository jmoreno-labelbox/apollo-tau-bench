from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class RejectAccessRequestTool(Tool):
    """Deny an access request."""

    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None, reviewer_id: str = None, decision_at: str = None,
    reason: Any = None,
    ) -> str:
        rid = request_id
        reviewer = reviewer_id
        decision_at = decision_at
        for req in data.get("access_requests", []):
            if req["request_id"] == rid:
                req["status"] = "REJECTED"
                req["reviewed_by"] = reviewer
                req["decision_at"] = decision_at
                payload = {"success": f"Request {rid} rejected"}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Request {rid} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RejectAccessRequest",
                "description": "Reject a pending access request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "reviewer_id": {"type": "string"},
                        "decision_at": {"type": "string"},
                    },
                    "required": ["request_id", "reviewer_id", "decision_at"],
                },
            },
        }
