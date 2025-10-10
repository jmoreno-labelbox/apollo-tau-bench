# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateBidStrategyForAdSet(Tool):
    """Updates the bid strategy for a specific ad set."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        new_strategy = kwargs.get("new_strategy")
        new_bid = kwargs.get("new_bid")
        
        adsets = list(data.get("adsets", {}).values())
        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                old_strategy = adset['bid_strategy']
                old_bid = adset['bid_amount']
                adset['bid_strategy'] = new_strategy
                adset['bid_amount'] = new_bid
                return json.dumps({
                    "status": "success",
                    "message": f"Ad set bid strategy updated from '{old_strategy}' to '{new_strategy}' with bid {new_bid}"
                })

        return json.dumps({"error": f"Ad set {adset_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_bid_strategy_for_adset",
                "description": "Updates the bid strategy for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "new_strategy": {"type": "string"},
                        "new_bid": {"type": "number"}
                    },
                    "required": ["adset_id", "new_strategy", "new_bid"]
                }
            }
        }
