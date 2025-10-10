# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchAdsByName(Tool):
    """Searches for ads with names containing the specified text."""

    @staticmethod
    def invoke(data: Dict[str, Any], name_query) -> str:
        ads = list(data.get("ads", {}).values())
        matching_ads = []
        
        for ad in ads:
            if name_query.lower() in ad.get("name", "").lower():
                matching_ads.append(ad.get("ad_id"))
        
        return json.dumps({"ad_ids": matching_ads})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_ads_by_name",
                "description": "Searches for ads with names containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_query": {
                            "type": "string",
                            "description": "The text to search for in ad names.",
                        }
                    },
                    "required": ["name_query"],
                },
            },
        }
