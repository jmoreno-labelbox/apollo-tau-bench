from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class deliver_fix_plan(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str = None, request_id: str = None, method: str = None, timestamp: str = None, recipients: list = None) -> str:
        p = _params(data, {"plan_id": plan_id, "request_id": request_id})
        miss = _require(p, ["plan_id", "request_id"])
        if miss:
            return miss
        for pl in _ensure(data, "fix_plans", []):
            if pl.get("plan_id") == p["plan_id"]:
                pl["status"] = "DELIVERED"
                return _ok({"plan_id": pl["plan_id"], "status": pl["status"]})
        return _err("plan_not_found", {"plan_id": p["plan_id"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeliverFixPlan",
                "description": "Mark a fix plan as delivered.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["plan_id", "request_id"],
                },
            },
        }
