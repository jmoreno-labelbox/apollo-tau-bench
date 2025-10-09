from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ModifyAssetRequest(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], updates: dict[str, Any] = None, request_id: str = None) -> str:
        updates = updates or {}
        requests = data.get("asset_requests", {}).values()
        for r in requests.values():
            if r.get("request_id") == request_id:
                r.update(updates)
                r["updated_at"] = _fixed_now_iso()
        payload = {"updated_request_id": request_id, "updates": updates}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAssetRequest",
                "description": "Update an asset request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["request_id", "updates"],
                },
            },
        }
