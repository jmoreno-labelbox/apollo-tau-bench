# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAdsetBidStrategy(Tool):
    """Update bid_strategy and/or bid_amount; logs to strategy_changes."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["adset_id", "timestamp", "request_id"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        adsets = _assert_table(data, "adsets")
        row = next((r for r in adsets if str(r.get("adset_id")) == str(kwargs["adset_id"])), None)
        if not row: return _fail("adset_not_found")
        changes = []
        if "bid_strategy" in kwargs and kwargs["bid_strategy"] != row.get("bid_strategy"):
            _assert_table(data, "strategy_changes").append(
                {"adset_id": str(kwargs["adset_id"]), "old_bid_strategy": row.get("bid_strategy"),
                 "new_bid_strategy": kwargs["bid_strategy"], "changed_at": kwargs["timestamp"],
                 "request_id": kwargs["request_id"]})
            row["bid_strategy"] = kwargs["bid_strategy"];
            row["updated_at"] = kwargs["timestamp"];
            changes.append("bid_strategy")
        if "bid_amount" in kwargs and kwargs["bid_amount"] != row.get("bid_amount"):
            _assert_table(data, "strategy_changes").append(
                {"adset_id": str(kwargs["adset_id"]), "old_bid_amount": row.get("bid_amount"),
                 "new_bid_amount": kwargs["bid_amount"], "changed_at": kwargs["timestamp"],
                 "request_id": kwargs["request_id"]})
            row["bid_amount"] = kwargs["bid_amount"];
            row["updated_at"] = kwargs["timestamp"];
            changes.append("bid_amount")
        return json.dumps({"ok": True, "adset_id": str(kwargs["adset_id"]), "updated": changes})

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
