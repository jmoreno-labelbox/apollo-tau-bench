from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ApproveAccessRequestTool(Tool):
    """Authorize an access request."""

    @staticmethod  #<-- necessary to align with base class definition
    def invoke(data: dict[str, Any], request_id: str, reviewer_id: str, decision_at: str) -> str:
        rid = request_id
        reviewer = reviewer_id
        decision_at = decision_at  #<-- additional mandatory argument!
        for req in data.get("access_requests", {}).values():
            if req["request_id"] == rid:
                req["status"] = "APPROVED"
                req["reviewed_by"] = reviewer
                req["decision_at"] = decision_at  #<-- utilize argument, AVOID hardcoding!
                payload = {"success": f"Request {rid} approved"}
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
                "name": "ApproveAccessRequest",
                "description": "Approve a pending access request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "reviewer_id": {"type": "string"},
                        "decision_at": {"type": "string"},  #<-- Include in properties!
                    },
                    "required": [
                        "request_id",
                        "reviewer_id",
                        "decision_at",
                    ],  #<-- Include in required!
                },
            },
        }
