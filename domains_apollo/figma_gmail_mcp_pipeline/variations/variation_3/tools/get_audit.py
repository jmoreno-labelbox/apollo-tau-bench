from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class get_audit(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str = None) -> str:
        p = _params(data, {"audit_id": audit_id})
        miss = _require(p, ["audit_id"])
        if miss:
            return miss
        for a in _ensure(data, "audits", []):
            if a.get("audit_id") == p["audit_id"]:
                return _ok(a)
        return _err("audit_not_found", {"audit_id": p["audit_id"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAudit",
                "description": "Fetch a single audit by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"audit_id": {"type": "string"}},
                    "required": ["audit_id"],
                },
            },
        }
