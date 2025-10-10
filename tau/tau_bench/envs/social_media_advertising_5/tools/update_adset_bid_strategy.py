# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAdsetBidStrategy(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], adset_id, bid_amount, bid_strategy, updated_at) -> str:
        aid = adset_id
        bs = bid_strategy
        ba = bid_amount
        for a in list(data.get("adsets", {}).values()):
            if a.get("adset_id") == aid:
                a["bid_strategy"] = bs
                a["bid_amount"] = ba
                a["updated_at"] = updated_at
                return json.dumps(a)
        return json.dumps({"error": f"adset {aid} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "update_adset_bid_strategy", "description": "Updates bid strategy and bid amount.",
                             "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"},
                                                                             "bid_strategy": {"type": "string"},
                                                                             "bid_amount": {"type": ["number", "null"]},
                                                                             "updated_at": {"type": "string"}},
                                            "required": ["adset_id", "bid_strategy", "updated_at"]}}}
