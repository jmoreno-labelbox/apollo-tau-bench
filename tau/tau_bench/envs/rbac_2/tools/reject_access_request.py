from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class RejectAccessRequest(Tool):
    """Deny an access request and document the reason."""

    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None, reviewer_id: str = None, timestamp: str = None, rejection_reason: str = None,
    reason: Any = None,
    ) -> str:
        request_id_to_find = request_id

        try:
            access_requests = data.get("access_requests", [])
        except:
            access_requests = []

        request_found = False
        for request in access_requests:
            if request.get("request_id") == request_id_to_find:
                request["status"] = "REJECTED"
                request["reviewed_by"] = reviewer_id
                request["decision_at"] = timestamp
                request["rejection_reason"] = rejection_reason
                request_found = True
                break

        if not request_found:
            payload = {"error": f"Access request with ID '{request_id_to_find}' not found."}
            out = json.dumps(payload)
            return out

        data["access_requests"] = access_requests
        payload = {
            "message": "Access request rejected successfully.",
            "request_id": request_id_to_find,
            "new_status": "REJECTED",
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RejectAccessRequest",
                "description": "Rejects a pending access request and records the reason for the rejection.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "The unique ID of the access request to be rejected.",
                        },
                        "reviewer_id": {
                            "type": "string",
                            "description": "The user ID of the manager who is rejecting the request.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp for the decision record.",
                        },
                        "rejection_reason": {
                            "type": "string",
                            "description": "A brief, clear reason for why the request is being rejected.",
                        },
                    },
                    "required": [
                        "request_id",
                        "reviewer_id",
                        "timestamp",
                        "rejection_reason",
                    ],
                },
            },
        }
