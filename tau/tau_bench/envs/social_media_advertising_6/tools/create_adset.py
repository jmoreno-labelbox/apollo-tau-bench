# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool










def _require(kwargs: Dict[str, Any], names: List[str]) -> Optional[str]:
    for n in names:
        if n not in kwargs:
            return f"missing_arg:{n}"
    return None

def _next_numeric_id(rows: List[Dict[str, Any]], key: str) -> str:
    mx = 0
    for r in rows:
        v = str(r.get(key))
        if v.isdigit():
            mx = max(mx, int(v))
    return str(mx + 1)

def _fail(msg: str) -> str:
    return json.dumps({"error": msg})

def _assert_table(data: Dict[str, Any], key: str) -> List[Dict[str, Any]]:
    if key not in data:
        raise ValueError(f"missing_table:{key}")
    tbl = data[key]
    if not isinstance(tbl, list):
        raise ValueError(f"invalid_table:{key}")
    return tbl

class CreateAdset(Tool):
    """Create an adset with explicit created_at; requires campaign exists."""

    @staticmethod
    def invoke(data: Dict[str, Any], bid_amount, bid_strategy, campaign_id, created_at, daily_budget, end_date, name, start_date, status) -> str:
        req = ["campaign_id", "name", "daily_budget", "bid_strategy", "status", "created_at"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        _assert_table(data, "campaigns")  # verify the table's existence
        adsets = _assert_table(data, "adsets")
        new_id = _next_numeric_id(adsets, "adset_id")
        rec = {
            "adset_id": new_id,
            "campaign_id": str(campaign_id),
            "name": name,
            "daily_budget": float(daily_budget),
            "bid_strategy": bid_strategy,
            "bid_amount": bid_amount,
            "start_date": start_date,
            "end_date": end_date,
            "status": status,
            "updated_at": created_at,
        }
        adsets.append(rec)
        return json.dumps(rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_adset",
                                                 "description": "Create an adset (deterministic; explicit created_at).",
                                                 "parameters": {"type": "object",
                                                                "properties": {"campaign_id": {"type": "string"},
                                                                               "name": {"type": "string"},
                                                                               "daily_budget": {"type": "number"},
                                                                               "bid_strategy": {"type": "string"},
                                                                               "bid_amount": {
                                                                                   "type": ["number", "null"]},
                                                                               "start_date": {
                                                                                   "type": ["string", "null"]},
                                                                               "end_date": {"type": ["string", "null"]},
                                                                               "status": {"type": "string"},
                                                                               "created_at": {"type": "string"}},
                                                                "required": ["campaign_id", "name", "daily_budget",
                                                                             "bid_strategy", "status", "created_at"]}}}