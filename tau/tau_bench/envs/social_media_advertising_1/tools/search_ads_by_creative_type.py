# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchAdsByCreativeType(Tool):
    """Searches for ads with a specific creative type."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        creative_type = kwargs.get("creative_type")
        ads = list(data.get("ads", {}).values())
        matching_ads = []
        
        for ad in ads:
            if ad.get("creative_type") == creative_type:
                matching_ads.append(ad.get("ad_id"))
        
        return json.dumps({"ad_ids": matching_ads})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_ads_by_creative_type",
                "description": "Searches for ads with a specific creative type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "creative_type": {
                            "type": "string",
                            "description": "The creative type to search for (e.g., image, video, carousel).",
                        }
                    },
                    "required": ["creative_type"],
                },
            },
        }
