from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class list_audit_findings_a11y(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str = None, violation_type: str = None) -> str:
        p = _params(data, {"audit_id": audit_id, "violation_type": violation_type})
        miss = _require(p, ["audit_id", "violation_type"])
        if miss:
            return miss
        rows = []
        for a in _ensure(data, "audits", []):
            if a.get("audit_id") == p["audit_id"]:
                for f in a.get("a11y_findings", []):
                    if f.get("violation_type") == p["violation_type"]:
                        rows.append(f)
                break
        return _ok({"rows": rows})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAuditFindingsA11y",
                "description": "List accessibility findings for an audit by violation type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "violation_type": {"type": "string"},
                    },
                    "required": ["audit_id", "violation_type"],
                },
            },
        }
