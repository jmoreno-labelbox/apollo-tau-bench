from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateAdStatus(Tool):
    """Modifies the status of a specific ad."""

    @staticmethod
    def invoke(data: dict[str, Any], ad_id: str = None, new_status: str = None,
    timestamp: Any = None,
    ) -> str:
        ads = data.get("ads", {}).values()
        for ad in ads.values():
            if ad.get("ad_id") == ad_id:
                old_status = ad["status"]
                ad["status"] = new_status
                payload = {
                    "status": "success",
                    "message": f"Ad status updated from '{old_status}' to '{new_status}'",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad {ad_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAdStatus",
                "description": "Updates the status for a specific ad.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {"type": "string"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["ad_id", "new_status"],
                },
            },
        }
