# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool








def _require(kwargs: Dict[str, Any], names: List[str]) -> Optional[str]:
    for n in names:
        if n not in kwargs:
            return f"missing_arg:{n}"
    return None

def _fail(msg: str) -> str:
    return json.dumps({"error": msg})

def _assert_table(data: Dict[str, Any], key: str) -> List[Dict[str, Any]]:
    if key not in data:
        raise ValueError(f"missing_table:{key}")
    tbl = data[key]
    if not isinstance(tbl, list):
        raise ValueError(f"invalid_table:{key}")
    return tbl

class UpdateAdsetBudget(Tool):
    """Update daily_budget with explicit timestamp & request_id; logs to budget_changes."""

    @staticmethod
    def invoke(data: Dict[str, Any], adset_id, new_budget, request_id, timestamp, reason = "manual") -> str:
        req = ["adset_id", "new_budget", "timestamp", "request_id"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        adsets = _assert_table(data, "adsets")
        row = next((r for r in adsets if str(r.get("adset_id")) == str(adset_id)), None)
        if not row: return _fail("adset_not_found")
        old = float(row.get("daily_budget", 0.0))
        new = float(new_budget)
        if new != old:
            row["daily_budget"] = new
            row["updated_at"] = timestamp
            _assert_table(data, "budget_changes").append(
                {"adset_id": str(adset_id), "old_budget": old, "new_budget": new,
                 "changed_at": timestamp, "reason": reason,
                 "request_id": request_id})
        return json.dumps({"ok": True, "adset_id": str(adset_id), "old_budget": old, "new_budget": new})

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