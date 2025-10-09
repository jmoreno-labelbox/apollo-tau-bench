from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class list_audit_findings_ds(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str = None, finding_type: str = None) -> str:
        p = _params(data, {"audit_id": audit_id, "finding_type": finding_type})
        miss = _require(p, ["audit_id", "finding_type"])
        if miss:
            return miss
        rows = []
        for a in _ensure(data, "audits", []):
            if a.get("audit_id") == p["audit_id"]:
                for f in a.get("ds_findings", []):
                    if f.get("finding_type") == p["finding_type"]:
                        rows.append(f)
                break
        return _ok({"rows": rows})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAuditFindingsDs",
                "description": "List design-system findings for an audit by type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "finding_type": {"type": "string"},
                    },
                    "required": ["audit_id", "finding_type"],
                },
            },
        }
