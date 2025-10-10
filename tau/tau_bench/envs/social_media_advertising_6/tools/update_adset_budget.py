# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAdsetBudget(Tool):
    """Update daily_budget with explicit timestamp & request_id; logs to budget_changes."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["adset_id", "new_budget", "timestamp", "request_id"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        adsets = _assert_table(data, "adsets")
        row = next((r for r in adsets if str(r.get("adset_id")) == str(kwargs["adset_id"])), None)
        if not row: return _fail("adset_not_found")
        old = float(row.get("daily_budget", 0.0))
        new = float(kwargs["new_budget"])
        if new != old:
            row["daily_budget"] = new
            row["updated_at"] = kwargs["timestamp"]
            _assert_table(data, "budget_changes").append(
                {"adset_id": str(kwargs["adset_id"]), "old_budget": old, "new_budget": new,
                 "changed_at": kwargs["timestamp"], "reason": kwargs.get("reason", "manual"),
                 "request_id": kwargs["request_id"]})
        return json.dumps({"ok": True, "adset_id": str(kwargs["adset_id"]), "old_budget": old, "new_budget": new})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "update_adset_budget", "description": "Write a budget change and log it.",
                             "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"},
                                                                             "new_budget": {"type": "number"},
                                                                             "timestamp": {"type": "string"},
                                                                             "request_id": {"type": "string"},
                                                                             "reason": {"type": "string"}},
                                            "required": ["adset_id", "new_budget", "timestamp", "request_id"]}}}
