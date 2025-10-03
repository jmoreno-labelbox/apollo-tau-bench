from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class UpdateBidStrategyForAdSet(Tool):
    """Modifies the bid strategy of a specific ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, new_strategy: str = None, new_bid: float = None) -> str:
        adsets = data.get("adsets", [])
        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                old_strategy = adset["bid_strategy"]
                adset["bid_amount"]
                adset["bid_strategy"] = new_strategy
                adset["bid_amount"] = new_bid
                payload = {
                    "status": "success",
                    "message": f"Ad set bid strategy updated from '{old_strategy}' to '{new_strategy}' with bid {new_bid}",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad set {adset_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateBidStrategyForAdset",
                "description": "Updates the bid strategy for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "new_strategy": {"type": "string"},
                        "new_bid": {"type": "number"},
                    },
                    "required": ["adset_id", "new_strategy", "new_bid"],
                },
            },
        }
