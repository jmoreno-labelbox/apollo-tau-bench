from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class update_review_approval(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        approved_ts_nullable: str = None,
        approver_email: str = None,
        cycle_id: str = None,
        request_id: str = None,
        timestamp: str = None
    ) -> str:
        p = {
            "cycle_id": cycle_id,
            "approver_email": approver_email,
            "approved_ts_nullable": approved_ts_nullable,
            "request_id": request_id,
            "timestamp": timestamp
        }
        miss = _require(
            p, ["cycle_id", "approver_email", "approved_ts_nullable", "request_id"]
        )
        if miss:
            return miss
        for c in _ensure(data, "review_cycles", []):
            if c.get("cycle_id") == p["cycle_id"]:
                c.setdefault("approvals", {}).values()[p["approver_email"]] = p[
                    "approved_ts_nullable"
                ]
                return _ok(
                    {
                        "cycle_id": p["cycle_id"],
                        "approver_email": p["approver_email"],
                        "approved_ts_nullable": p["approved_ts_nullable"],
                        "approval_comment_ref_nullable": None,
                        "updated_ts": p.get("timestamp"),
                    }
                )
        return _err("cycle_not_found", {"cycle_id": p["cycle_id"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReviewApproval",
                "description": "Set/Update approval timestamp for a reviewer in a cycle.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "approver_email": {"type": "string"},
                        "approved_ts_nullable": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": [
                        "cycle_id",
                        "approver_email",
                        "approved_ts_nullable",
                        "request_id",
                    ],
                },
            },
        }
