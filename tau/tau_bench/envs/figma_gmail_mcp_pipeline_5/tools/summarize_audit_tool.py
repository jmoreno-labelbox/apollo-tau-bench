# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SummarizeAuditTool(Tool):
    """Summarize DS and A11y finding counts for an audit."""

    @staticmethod
    def invoke(data: Dict[str, Any], audit_id) -> str:
        audit_id = _require_str(audit_id, "audit_id")
        if not audit_id:
            return json.dumps({"error":"audit_id is required"})

        ds = data.get("audit_findings_ds", [])
        a11y = data.get("audit_findings_a11y", [])
        ds_count = sum(1 for r in ds if r.get("audit_id") == audit_id)
        a11y_count = sum(1 for r in a11y if r.get("audit_id") == audit_id)
        return json.dumps({"audit_id": audit_id, "ds_findings": ds_count, "a11y_findings": a11y_count}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"summarize_audit",
            "description":"Return simple counts of design-system and accessibility findings for an audit.",
            "parameters":{"type":"object","properties":{
                "audit_id":{"type":"string"}
            },"required":["audit_id"]}
        }}
