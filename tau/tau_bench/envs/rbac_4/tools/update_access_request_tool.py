from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateAccessRequestTool(Tool):
    """Fundamental: modify an access request's status and metadata (no side effects)."""

    _ALLOWED = {"PENDING", "APPROVED", "REJECTED", "DEFERRED"}

    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None, status: str = None, updated_on: str = None, updated_by: str = None) -> str:
        # Mandatory parameters
        params_dict = {k: v for k, v in locals().items() if k != "data"}
        missing = [
            k
            for k in ("request_id", "status", "updated_on", "updated_by")
            if params_dict.get(k) is None
        ]
        if missing:
            payload = {"error": f"Missing: {', '.join(missing)}"}
            out = json.dumps(payload, indent=2)
            return out

        # Simple status verification
        if status not in UpdateAccessRequestTool._ALLOWED:
            payload = {
                    "error": f"Invalid status '{status}'. Allowed: {sorted(UpdateAccessRequestTool._ALLOWED)}"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Import tables
        access_requests = data.get("access_requests", [])
        users = data.get("users", [])

        # References
        req = next(
            (r for r in access_requests if r.get("request_id") == request_id), None
        )
        if not req:
            payload = {"error": f"Unknown request_id '{request_id}'"}
            out = json.dumps(payload, indent=2)
            return out

        if not any(u.get("user_id") == updated_by for u in users):
            payload = {"error": f"Unknown updated_by '{updated_by}'"}
            out = json.dumps(payload, indent=2)
            return out

        # Modify in place (basic)
        req["status"] = status
        req["updated_on"] = updated_on
        req["updated_by"] = updated_by
        payload = req
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAccessRequest",
                "description": "Basic update of an access request's status and metadata (no side effects).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string", "description": "e.g., AR-007"},
                        "status": {
                            "type": "string",
                            "enum": ["PENDING", "APPROVED", "REJECTED", "DEFERRED"],
                        },
                        "updated_on": {
                            "type": "string",
                            "description": "ISO 8601 timestamp",
                        },
                        "updated_by": {
                            "type": "string",
                            "description": "User ID performing the update",
                        },
                    },
                    "required": ["request_id", "status", "updated_on", "updated_by"],
                },
            },
        }
