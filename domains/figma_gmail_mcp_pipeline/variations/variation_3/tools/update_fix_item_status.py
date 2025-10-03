from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class update_fix_item_status(Tool):
    def invoke(
        data: dict[str, Any],
        item_id: str = None,
        plan_id: str = None,
        status: str = None
    ) -> str:
        p = {"plan_id": plan_id, "item_id": item_id, "status": status}
        miss = _require(p, ["plan_id", "item_id", "status"])
        if miss:
            return miss
        for pl in _ensure(data, "fix_plans", []):
            if pl.get("plan_id") == p["plan_id"]:
                for it in pl.get("items", []):
                    if it.get("item_id") == p["item_id"]:
                        it["status"] = p["status"]
                        return _ok(
                            {
                                "plan_id": pl["plan_id"],
                                "item_id": p["item_id"],
                                "status": p["status"],
                            }
                        )
        return _err(
            "item_not_found", {"plan_id": p.get("plan_id"), "item_id": p.get("item_id")}
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateFixItemStatus",
                "description": "Update the status of a single fix item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "item_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["plan_id", "item_id", "status"],
                },
            },
        }
