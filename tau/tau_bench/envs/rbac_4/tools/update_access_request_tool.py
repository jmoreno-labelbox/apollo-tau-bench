# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAccessRequestTool(Tool):
    """Basic: update an access request's status and metadata (no side effects)."""

    _ALLOWED = {"PENDING", "APPROVED", "REJECTED", "DEFERRED"}

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id")
        status = kwargs.get("status")
        updated_on = kwargs.get("updated_on")
        updated_by = kwargs.get("updated_by")

        # Necessary parameters
        missing = [k for k in ("request_id","status","updated_on","updated_by") if kwargs.get(k) is None]
        if missing:
            return json.dumps({"error": f"Missing: {', '.join(missing)}"}, indent=2)

        # Fundamental status verification
        if status not in UpdateAccessRequestTool._ALLOWED:
            return json.dumps({"error": f"Invalid status '{status}'. Allowed: {sorted(UpdateAccessRequestTool._ALLOWED)}"}, indent=2)

        # Import tables
        access_requests = data.get("access_requests", [])
        users = list(data.get("users", {}).values())

        # Reference points
        req = next((r for r in access_requests if r.get("request_id") == request_id), None)
        if not req:
            return json.dumps({"error": f"Unknown request_id '{request_id}'"}, indent=2)

        if not any(u.get("user_id") == updated_by for u in users):
            return json.dumps({"error": f"Unknown updated_by '{updated_by}'"}, indent=2)

        # In-place update (simple)
        req["status"] = status
        req["updated_on"] = updated_on
        req["updated_by"] = updated_by

        return json.dumps(req, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_access_request",
                "description": "Basic update of an access request's status and metadata (no side effects).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string", "description": "e.g., AR-007"},
                        "status": {"type": "string", "enum": ["PENDING","APPROVED","REJECTED","DEFERRED"]},
                        "updated_on": {"type": "string", "description": "ISO 8601 timestamp"},
                        "updated_by": {"type": "string", "description": "User ID performing the update"}
                    },
                    "required": ["request_id","status","updated_on","updated_by"]
                }
            }
        }
