# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _params, _require


class list_audit_findings_ds(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs)->str:
        p = _params(data, kwargs)
        miss = _require(p, ["audit_id","finding_type"])
        if miss: return miss
        rows = []
        for a in _ensure(data, "audits", []):
            if a.get("audit_id") == p["audit_id"]:
                for f in a.get("ds_findings", []):
                    if f.get("finding_type") == p["finding_type"]:
                        rows.append(f)
                break
        return _ok({"rows": rows})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"list_audit_findings_ds",
            "description":"List design-system findings for an audit by type.",
            "parameters":{"type":"object","properties":{
                "audit_id":{"type":"string"},
                "finding_type":{"type":"string"}
            },"required":["audit_id","finding_type"]}
        }}
