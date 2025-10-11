# Sierra Copyright

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

class UpdatePlanStatus(Tool):
    """Set a plan's status and applied_at timestamp explicitly."""

    @staticmethod
    def invoke(data: Dict[str, Any], applied_at, plan_id, status) -> str:
        err = _require(kwargs, ["plan_id", "status", "applied_at"])
        if err: return _fail(err)
        plans = _assert_table(data, "plans")
        row = next((p for p in plans if p.get("plan_id") == plan_id), None)
        if not row: return _fail("plan_not_found")
        row["status"] = status
        row["applied_at"] = applied_at
        return json.dumps({"ok": True, "plan_id": plan_id, "status": status})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_plan_status",
                                                 "description": "Mark plan as applied/aborted with explicit applied_at.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"plan_id": {"type": "string"},
                                                                               "status": {"type": "string"},
                                                                               "applied_at": {"type": "string"}},
                                                                "required": ["plan_id", "status", "applied_at"]}}}