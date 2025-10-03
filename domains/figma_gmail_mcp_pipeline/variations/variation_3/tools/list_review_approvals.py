from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class list_review_approvals(Tool):
    def invoke(data: dict[str, Any], cycle_id: str = None) -> str:
        p = _params(data, {"cycle_id": cycle_id})
        miss = _require(p, ["cycle_id"])
        if miss:
            return miss
        rows = []
        for c in _ensure(data, "review_cycles", []):
            if c.get("cycle_id") == p["cycle_id"]:
                for email, ts in c.get("approvals", {}).items():
                    rows.append({"approver_email": email, "approved_ts_nullable": ts})
                break
        return _ok({"rows": rows})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listReviewApprovals",
                "description": "List approvals for a review cycle.",
                "parameters": {
                    "type": "object",
                    "properties": {"cycle_id": {"type": "string"}},
                    "required": ["cycle_id"],
                },
            },
        }
