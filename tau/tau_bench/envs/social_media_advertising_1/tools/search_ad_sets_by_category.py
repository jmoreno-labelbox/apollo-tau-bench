# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchAdSetsByCategory(Tool):
    """Searches for ad sets with a specific category."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        category = kwargs.get("category")
        adsets = list(data.get("adsets", {}).values())
        matching_adsets = []
        
        for adset in adsets:
            if adset.get("category") == category:
                matching_adsets.append(adset.get("adset_id"))
        
        return json.dumps({"adset_ids": matching_adsets})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_adsets_by_category",
                "description": "Searches for ad sets with a specific category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "The category to search for (e.g., Electronics, Apparel, Home).",
                        }
                    },
                    "required": ["category"],
                },
            },
        }
