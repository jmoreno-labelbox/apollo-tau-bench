from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetAccessRequestTool(Tool):
    """Retrieve a single access request entry using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None) -> str:
        if not request_id:
            payload = {"error": "request_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        requests: list[dict[str, Any]] = data.get("access_requests", {}).values()
        rec = next((r for r in requests if r.get("request_id") == request_id), None)
        if rec is None:
            payload = {"error": f"Access request {request_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #standardize structure and ensure reliable defaults
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAccessRequest",
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
