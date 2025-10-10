# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetNameForAd(Tool):
    """Retrieves the name for a specific ad."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ad_id = kwargs.get("ad_id")
        ads = list(data.get("ads", {}).values())
        
        for ad in ads:
            if ad.get("ad_id") == ad_id:
                return json.dumps({"name": ad.get('name')})
        
        return json.dumps({"error": f"Ad with ID '{ad_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_name_for_ad",
                "description": "Retrieves the name for a specific ad.",
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
