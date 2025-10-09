from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateAccessRequest(Tool):
    """Modifies an existing access request, utilized for rerouting or adjustments."""

    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None, new_reviewer_id: str = None, new_status: str = None, timestamp: str = None) -> str:
        for req in data.get("access_requests", []):
            if req.get("request_id") == request_id:
                if new_reviewer_id:
                    req["reviewer_id"] = new_reviewer_id
                if new_status:
                    req["status"] = new_status
                req["decision_at"] = timestamp
                payload = {"status": "success", "updated_request_id": request_id}
                out = json.dumps(payload)
                return out
        payload = {"status": "error", "message": "Request not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAccessRequest",
                "description": "Updates an existing access request. Primarily used to reroute a request to a new approver by changing the reviewer_id and resetting the status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "The ID of the access request to update.",
                        },
                        "new_reviewer_id": {
                            "type": "string",
                            "description": "The user_id of the new approver to assign the request to.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the request, e.g., 'PENDING'.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The timestamp of the update action.",
                        },
                    },
                    "required": ["request_id"],
                },
            },
        }
