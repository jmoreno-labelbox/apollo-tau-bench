from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class attach_thread_to_review_cycle(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cycle_id: str = None, thread_id: str = None, updated_at: str = None, timestamp: str = None, request_id: str = None) -> str:
        p = _params(data, {"cycle_id": cycle_id, "thread_id": thread_id})
        miss = _require(p, ["cycle_id", "thread_id"])
        if miss:
            return miss
        for c in _ensure(data, "review_cycles", []):
            if c.get("cycle_id") == p["cycle_id"]:
                c["thread_id_nullable"] = p["thread_id"]
                return _ok({"cycle_id": c["cycle_id"], "thread_id": p["thread_id"]})
        return _err("cycle_not_found", {"cycle_id": p["cycle_id"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AttachThreadToReviewCycle",
                "description": "Attach an email thread to a review cycle.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "thread_id": {"type": "string"},
                    },
                    "required": ["cycle_id", "thread_id"],
                },
            },
        }
