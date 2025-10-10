# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteAd(Tool):
    """Deletes an ad."""

    @staticmethod
    def invoke(data: Dict[str, Any], ad_id) -> str:
        if not ad_id:
            return json.dumps({"error": "ad_id is a required parameter."})

        ads = list(data.get("ads", {}).values())
        for ad in ads:
            if ad.get("ad_id") == ad_id:
                data['ads'] = [d for d in data['ads'] if d['ad_id'] != ad_id]
                return json.dumps(
                    {
                        "status": "success",
                        "message": f"Ad with id {ad_id} deleted successfully",
                    }
                )

        return json.dumps({"error": f"Ad with ID '{ad_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_ad",
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
