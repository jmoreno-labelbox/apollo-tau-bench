# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchAdSetsByBidStrategy(Tool):
    """Searches for ad sets with a specific bid strategy."""

    @staticmethod
    def invoke(data: Dict[str, Any], bid_strategy) -> str:
        adsets = list(data.get("adsets", {}).values())
        matching_adsets = []
        
        for adset in adsets:
            if adset.get("bid_strategy") == bid_strategy:
                matching_adsets.append(adset.get("adset_id"))
        
        return json.dumps({"adset_ids": matching_adsets})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_adsets_by_bid_strategy",
                "description": "Searches for ad sets with a specific bid strategy.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "bid_strategy": {
                            "type": "string",
                            "description": "The bid strategy to search for (e.g., cost_cap, lowest_cost).",
                        }
                    },
                    "required": ["bid_strategy"],
                },
            },
        }
