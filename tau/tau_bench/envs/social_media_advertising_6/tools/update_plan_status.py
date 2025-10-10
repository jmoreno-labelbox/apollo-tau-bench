# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
