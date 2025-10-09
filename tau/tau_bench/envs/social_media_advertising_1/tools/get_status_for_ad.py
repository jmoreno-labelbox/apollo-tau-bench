from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetStatusForAd(Tool):
    """Fetches the current status of a specific ad."""

    @staticmethod
    def invoke(data: dict[str, Any], ad_id: str = None) -> str:
        ads = data.get("ads", {}).values()

        for ad in ads.values():
            if ad.get("ad_id") == ad_id:
                payload = {"status": ad.get("status")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad with ID '{ad_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetStatusForAd",
                "description": "Retrieves the status for a specific ad.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {
                            "type": "string",
                            "description": "The unique ID of the ad.",
                        }
                    },
                    "required": ["ad_id"],
                },
            },
        }
