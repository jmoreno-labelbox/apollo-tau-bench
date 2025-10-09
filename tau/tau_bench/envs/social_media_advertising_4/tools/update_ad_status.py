from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateAdStatus(Tool):
    """Modifies the status of a single ad."""

    @staticmethod
    def invoke(data: dict[str, Any], ad_id: str = None, status: str = None, request_id: Any = None,
    timestamp: Any = None,
    ) -> str:
        for ad in data.get("ads", []):
            if ad.get("ad_id") == ad_id:
                ad["status"] = status
                payload = ad
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad ID '{ad_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAdStatus",
                "description": "Updates the status of a single ad (e.g., 'active', 'paused').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["ad_id", "status"],
                },
            },
        }
