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

class GetAdsetAllocationFromPlan(Tool):
    """Return the allocation entry for a given adset_id inside a plan_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], adset_id, plan_id) -> str:
        err = _require(kwargs, ["plan_id", "adset_id"])
        if err: return _fail(err)
        plans = _assert_table(data, "plans")
        pid = plan_id
        aid = str(adset_id)
        for p in plans:
            if p.get("plan_id") == pid:
                for row in p.get("allocations", []):
                    if str(row.get("adset_id")) == aid:
                        return json.dumps(row)
                return _fail("allocation_not_found")
        return _fail("plan_not_found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_adset_allocation_from_plan",
                                                 "description": "Get the planned allocation for an adset in a plan.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"plan_id": {"type": "string"},
                                                                               "adset_id": {"type": "string"}},
                                                                "required": ["plan_id", "adset_id"]}}}