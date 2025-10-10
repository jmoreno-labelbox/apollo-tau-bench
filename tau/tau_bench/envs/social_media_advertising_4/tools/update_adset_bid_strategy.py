# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAdsetBidStrategy(Tool):
    """Modifies the bid strategy for an ad set."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        for adset in data.get('adsets', []):
            if adset.get('adset_id') == adset_id:
                adset['bid_strategy'] = kwargs.get("bid_strategy")
                adset['bid_amount'] = kwargs.get("bid_amount")
                return json.dumps(adset)
        return json.dumps({"error": f"Ad set ID '{adset_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_adset_bid_strategy", "description": "Updates the bidding strategy and bid amount for a given ad set.", "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"}, "bid_strategy": {"type": "string"}, "bid_amount": {"type": "number"}}, "required": ["adset_id", "bid_strategy"]}}}
