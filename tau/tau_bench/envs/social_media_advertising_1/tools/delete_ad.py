from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class DeleteAd(Tool):
    """Removes an ad."""

    @staticmethod
    def invoke(data: dict[str, Any], ad_id: str = None) -> str:
        if not ad_id:
            payload = {"error": "ad_id is a required parameter."}
            out = json.dumps(payload)
            return out

        ads = data.get("ads", [])
        for ad in ads:
            if ad.get("ad_id") == ad_id:
                data["ads"] = [d for d in data["ads"] if d["ad_id"] != ad_id]
                payload = {
                    "status": "success",
                    "message": f"Ad with id {ad_id} deleted successfully",
                }
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
                "name": "deleteAd",
                "description": "Deletes an ad.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {
                            "type": "string",
                            "description": "The unique ID of the ad to delete.",
                        },
                    },
                    "required": ["ad_id"],
                },
            },
        }
