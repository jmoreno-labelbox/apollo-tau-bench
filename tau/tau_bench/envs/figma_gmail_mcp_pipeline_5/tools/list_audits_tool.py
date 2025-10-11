# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _small_fields(row: Dict[str, Any], fields: List[str]) -> Dict[str, Any]:
    """Return selected fields only (simple outputs)."""
    return {k: row.get(k) for k in fields}

class ListAuditsTool(Tool):
    """List audit sessions filtered by artifact or status."""

    @staticmethod
    def invoke(data: Dict[str, Any], artifact_id, status) -> str:

        audits = data.get("audits", [])
        out = []
        for a in audits:
            if artifact_id and a.get("artifact_id") != artifact_id:
                continue
            if status and a.get("status") != status:
                continue
            out.append(_small_fields(a, ["audit_id","artifact_id","audit_type","status","created_ts"]))
        out.sort(key=lambda r: r.get("audit_id",""))
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"list_audits",
            "description":"List audits filtered by artifact_id and/or status.",
            "parameters":{"type":"object","properties":{
                "artifact_id":{"type":"string"},
                "status":{"type":"string"}
            }}
        }}