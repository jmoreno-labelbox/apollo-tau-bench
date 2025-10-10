# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchAdsByAdSet(Tool):
    """Searches for ads belonging to a specific ad set."""

    @staticmethod
    def invoke(data: Dict[str, Any], adset_id) -> str:
        ads = list(data.get("ads", {}).values())
        matching_ads = []
        
        for ad in ads:
            if ad.get("adset_id") == adset_id:
                matching_ads.append(ad.get("ad_id"))
        
        return json.dumps({"ad_ids": matching_ads})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_ads_by_adset",
                "description": "Searches for ads belonging to a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ad set ID to search for ads.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }
