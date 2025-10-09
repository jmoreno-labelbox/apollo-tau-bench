from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class update_audit_status(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        audit_id: str = None,
        request_id: str = None,
        status: str = None,
        updated_at: str = None,
        timestamp: str = None
    ) -> str:
        p = {
            "audit_id": audit_id,
            "status": status,
            "request_id": request_id,
            "updated_at": updated_at
        }
        miss = _require(p, ["audit_id", "status", "request_id"])
        if miss:
            return miss
        for a in _ensure(data, "audits", []):
            if a.get("audit_id") == p["audit_id"]:
                a["status"] = p["status"]
                a["updated_at"] = p.get("updated_at")
                return _ok({"audit_id": a["audit_id"], "status": a["status"]})
        return _err("audit_not_found", {"audit_id": p["audit_id"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAuditStatus",
                "description": "Update an audit's status deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "status": {"type": "string"},
                        "updated_at": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["audit_id", "status", "request_id"],
                },
            },
        }
