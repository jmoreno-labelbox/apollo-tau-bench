# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAdsetBidStrategy(Tool):
    """Update bid_strategy and/or bid_amount; logs to strategy_changes."""

    @staticmethod
    def invoke(data: Dict[str, Any], adset_id, bid_amount, bid_strategy, request_id, timestamp) -> str:
        req = ["adset_id", "timestamp", "request_id"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        adsets = _assert_table(data, "adsets")
        row = next((r for r in adsets if str(r.get("adset_id")) == str(adset_id)), None)
        if not row: return _fail("adset_not_found")
        changes = []
        if "bid_strategy" in kwargs and bid_strategy != row.get("bid_strategy"):
            _assert_table(data, "strategy_changes").append(
                {"adset_id": str(adset_id), "old_bid_strategy": row.get("bid_strategy"),
                 "new_bid_strategy": bid_strategy, "changed_at": timestamp,
                 "request_id": request_id})
            row["bid_strategy"] = bid_strategy;
            row["updated_at"] = timestamp;
            changes.append("bid_strategy")
        if "bid_amount" in kwargs and bid_amount != row.get("bid_amount"):
            _assert_table(data, "strategy_changes").append(
                {"adset_id": str(adset_id), "old_bid_amount": row.get("bid_amount"),
                 "new_bid_amount": bid_amount, "changed_at": timestamp,
                 "request_id": request_id})
            row["bid_amount"] = bid_amount;
            row["updated_at"] = timestamp;
            changes.append("bid_amount")
        return json.dumps({"ok": True, "adset_id": str(adset_id), "updated": changes})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_adset_bid_strategy",
                                                 "description": "Update bid strategy/amount with logging.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"adset_id": {"type": "string"},
                                                                               "bid_strategy": {"type": "string"},
                                                                               "bid_amount": {
                                                                                   "type": ["number", "null"]},
                                                                               "timestamp": {"type": "string"},
                                                                               "request_id": {"type": "string"}},
                                                                "required": ["adset_id", "timestamp", "request_id"]}}}
