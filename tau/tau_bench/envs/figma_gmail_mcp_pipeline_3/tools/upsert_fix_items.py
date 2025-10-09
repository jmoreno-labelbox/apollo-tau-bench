from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class upsert_fix_items(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str = None, items: list = None, timestamp: str = None, request_id: str = None) -> str:
        p = _params(data, {"plan_id": plan_id, "items": items})
        miss = _require(p, ["plan_id", "items"])
        if miss:
            return miss
        for pl in _ensure(data, "fix_plans", []):
            if pl.get("plan_id") == p["plan_id"]:
                by_id = {i["item_id"]: i for i in pl.get("items", []) if "item_id" in i}
                for i in p.get("items", []):
                    iid = i.get("item_id") or f"item_{len(by_id)+1:03d}"
                    i["item_id"] = iid
                    by_id[iid] = i
                pl["items"] = list(by_id)
                return _ok({"plan_id": pl["plan_id"], "items": pl["items"]})
        return _err("plan_not_found", {"plan_id": p["plan_id"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertFixItems",
                "description": "Insert or update fix items on a plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "items": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["plan_id", "items"],
                },
            },
        }
