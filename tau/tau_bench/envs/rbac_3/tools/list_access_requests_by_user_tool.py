from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListAccessRequestsByUserTool(Tool):
    """ListAccessRequestsByUser"""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        out = [
            r for r in data.get("access_requests", []) if r.get("user_id") == user_id
        ]
        out = sorted(
            out, key=lambda r: (r.get("submitted_at") or "", r.get("request_id") or "")
        )
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAccessRequestsByUser",
                "description": "Filter access_requests by user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
