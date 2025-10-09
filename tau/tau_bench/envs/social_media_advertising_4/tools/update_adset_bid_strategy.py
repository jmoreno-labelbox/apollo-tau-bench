from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateAdsetBidStrategy(Tool):
    """Alters the bid strategy of an ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, bid_strategy: str = None, bid_amount: float = None) -> str:
        for adset in data.get("adsets", {}).values():
            if adset.get("adset_id") == adset_id:
                adset["bid_strategy"] = bid_strategy
                adset["bid_amount"] = bid_amount
                payload = adset
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad set ID '{adset_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAdsetBidStrategy",
                "description": "Updates the bidding strategy and bid amount for a given ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "bid_strategy": {"type": "string"},
                        "bid_amount": {"type": "number"},
                    },
                    "required": ["adset_id", "bid_strategy"],
                },
            },
        }
