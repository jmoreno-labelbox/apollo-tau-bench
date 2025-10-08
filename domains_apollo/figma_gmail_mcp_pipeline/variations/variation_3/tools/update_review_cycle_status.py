from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class update_review_cycle_status(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        cycle_id: str = None,
        request_id: str = None,
        status: str = None,
        updated_at: str = None,
        timestamp: str = None
    ) -> str:
        p = _params(data, {"cycle_id": cycle_id, "status": status, "request_id": request_id, "updated_at": updated_at})
        miss = _require(p, ["cycle_id", "status", "request_id"])
        if miss:
            return miss
        for c in _ensure(data, "review_cycles", []):
            if c.get("cycle_id") == p["cycle_id"]:
                c["status"] = p["status"]
                c["updated_at"] = p.get("updated_at")
                return _ok(
                    {
                        "cycle_id": c["cycle_id"],
                        "status": c["status"],
                        "updated_at": c.get("updated_at"),
                    }
                )
        return _err("cycle_not_found", {"cycle_id": p["cycle_id"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReviewCycleStatus",
                "description": "Update the status of a review cycle.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "status": {"type": "string"},
                        "updated_at": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["cycle_id", "status", "request_id"],
                },
            },
        }
