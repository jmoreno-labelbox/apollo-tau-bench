# Sierra copyright.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _params, _require


class list_audit_findings_a11y(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs)->str:
        p = _params(data, kwargs)
        miss = _require(p, ["audit_id","violation_type"])
        if miss: return miss
        rows = []
        for a in _ensure(data, "audits", []):
            if a.get("audit_id") == p["audit_id"]:
                for f in a.get("a11y_findings", []):
                    if f.get("violation_type") == p["violation_type"]:
                        rows.append(f)
                break
        return _ok({"rows": rows})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"list_audit_findings_a11y",
            "description":"List accessibility findings for an audit by violation type.",
            "parameters":{"type":"object","properties":{
                "audit_id":{"type":"string"},
                "violation_type":{"type":"string"}
            },"required":["audit_id","violation_type"]}
        }}
