# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _err(msg: str, code: str = "bad_request", ) -> str:
    """Creates a JSON error message."""
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)

class UpdateAssetRequestStatusTool(Tool):
    """Updates an existing asset request's status and related fields."""

    @staticmethod
    def invoke(data: Dict[str, Any], assigned_asset_tag, linked_message_id, new_status, request_id) -> str:

        request = next((r for r in data.get("asset_requests", []) if r.get("request_id") == request_id), None)
        if not request:
            return _err(f"Request '{request_id}' not found", code="not_found")

        if new_status not in {"Pending", "Sent", "Reserved", "Completed"}:
            return _err("Invalid status.")

        request["status"] = new_status
        request["updated_ts"] = HARD_TS
        if "linked_message_id" in kwargs:
            request["email_message_id_nullable"] = linked_message_id
        if "assigned_asset_tag" in kwargs:
            request["asset_tag_nullable"] = assigned_asset_tag
            request["inventory_checked_flag"] = True

        return json.dumps(request, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {"name": "update_asset_request_status",
            "description": "Updates the status of an asset request.",
            "parameters": {"type": "object", "properties": {
                "request_id": {"type": "string"}, "new_status": {"type": "string"},
                "linked_message_id": {"type": "string"}, "assigned_asset_tag": {"type": "string"}
            }, "required": ["request_id", "new_status"]}}}