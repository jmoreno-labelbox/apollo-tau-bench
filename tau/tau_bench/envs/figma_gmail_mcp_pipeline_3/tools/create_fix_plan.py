from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class create_fix_plan(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        audit_id: str = None,
        delivery_method: str = None,
        owner_email: str = None,
        request_id: str = None,
        timestamp: str = None
    ) -> str:
        p = _params(data, {
            "audit_id": audit_id,
            "owner_email": owner_email,
            "delivery_method": delivery_method,
            "timestamp": timestamp,
            "request_id": request_id
        })
        miss = _require(
            p, ["audit_id", "owner_email", "delivery_method", "timestamp", "request_id"]
        )
        if miss:
            return miss
        w = _require_write(p)
        if w:
            return w

        # Obtain artifact_id from audit_id "aud-<artifact_id>-<YYYYMMDD>-<seq>"
        audit_id = p["audit_id"]
        m = re.match(r"^aud-(?P<art>[^-]+)-(?P<date>\d{8})-(?P<seq>\d+)$", audit_id)
        if not m:
            return _err("invalid_audit_id_format")
        artifact_id = m.group("art")

        # According to ID_RULE: date is based on timestamp
        yyyymmdd = p["timestamp"][0:10].replace("-", "")
        plan_id = f"fp-{artifact_id}-{yyyymmdd}-001"
        plan = {
            "plan_id": plan_id,
            "audit_id": audit_id,
            "owner_email": p["owner_email"],
            "delivery_method": p["delivery_method"],
            "status": "DRAFTED",
            "created_ts": p["timestamp"],
        }
        _ensure(data, "fix_plans", []).append(plan)
        return _ok(plan)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateFixPlan",
                "description": "Create a fix plan for an audit (deterministic id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "owner_email": {"type": "string"},
                        "delivery_method": {
                            "type": "string",
                            "enum": ["COMMENTS", "TICKETS", "PDF", "EMAIL"],
                        },
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": [
                        "audit_id",
                        "owner_email",
                        "delivery_method",
                        "timestamp",
                        "request_id",
                    ],
                },
            },
        }
