from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class SearchAdSetsByBidStrategy(Tool):
    """Looks for ad sets that utilize a specific bid strategy."""

    @staticmethod
    def invoke(data: dict[str, Any], bid_strategy: str = None) -> str:
        adsets = data.get("adsets", [])
        matching_adsets = []

        for adset in adsets:
            if adset.get("bid_strategy") == bid_strategy:
                matching_adsets.append(adset.get("adset_id"))
        payload = {"adset_ids": matching_adsets}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchAdsetsByBidStrategy",
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
