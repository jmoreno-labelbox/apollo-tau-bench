from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class get_review_cycle(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cycle_id: str = None) -> str:
        p = _params(data, {"cycle_id": cycle_id})
        miss = _require(p, ["cycle_id"])
        if miss:
            return miss
        for c in _ensure(data, "review_cycles", []):
            if c.get("cycle_id") == p["cycle_id"]:
                return _ok(c)
        return _ok(
            {"cycle_id": p["cycle_id"], "status": "", "thread_id_nullable": None}
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReviewCycle",
                "description": "Fetch a review cycle summary.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["cycle_id"],
                },
            },
        }
