from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetCreativeTypeForAd(Tool):
    """Fetches the creative type of a specific ad."""

    @staticmethod
    def invoke(data: dict[str, Any], ad_id: str = None) -> str:
        ads = data.get("ads", [])

        for ad in ads:
            if ad.get("ad_id") == ad_id:
                payload = {"creative_type": ad.get("creative_type")}
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
                "name": "GetCreativeTypeForAd",
                "description": "Retrieves the creative_type for a specific ad.",
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
