from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class UpdatePlanStatus(Tool):
    """Explicitly set a plan's status and applied_at timestamp."""

    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str, status: str, applied_at: str) -> str:
        err = _require({"plan_id": plan_id, "status": status, "applied_at": applied_at}, ["plan_id", "status", "applied_at"])
        if err:
            return _fail(err)
        plans = _assert_table(data, "plans")
        row = next((p for p in plans if p.get("plan_id") == plan_id), None)
        if not row:
            return _fail("plan_not_found")
        row["status"] = status
        row["applied_at"] = applied_at
        payload = {"ok": True, "plan_id": plan_id, "status": status}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdatePlanStatus",
                "description": "Mark plan as applied/aborted with explicit applied_at.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "status": {"type": "string"},
                        "applied_at": {"type": "string"},
                    },
                    "required": ["plan_id", "status", "applied_at"],
                },
            },
        }
