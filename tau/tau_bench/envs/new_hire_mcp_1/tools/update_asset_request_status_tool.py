from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateAssetRequestStatusTool(Tool):
    """Refreshes the status and associated fields of an existing asset request."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        request_id: str,
        new_status: str,
        linked_message_id: str = None,
        assigned_asset_tag: str = None
    ) -> str:
        request = next(
            (
                r
                for r in data.get("asset_requests", {}).values()
                if r.get("request_id") == request_id
            ),
            None,
        )
        if not request:
            return _err(f"Request '{request_id}' not found", code="not_found")

        if new_status not in {"Pending", "Sent", "Reserved", "Completed"}:
            return _err("Invalid status.")

        request["status"] = new_status
        request["updated_ts"] = HARD_TS
        if linked_message_id is not None:
            request["email_message_id_nullable"] = linked_message_id
        if assigned_asset_tag is not None:
            request["asset_tag_nullable"] = assigned_asset_tag
            request["inventory_checked_flag"] = True
        payload = request
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAssetRequestStatus",
                "description": "Updates the status of an asset request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "new_status": {"type": "string"},
                        "linked_message_id": {"type": "string"},
                        "assigned_asset_tag": {"type": "string"},
                    },
                    "required": ["request_id", "new_status"],
                },
            },
        }
