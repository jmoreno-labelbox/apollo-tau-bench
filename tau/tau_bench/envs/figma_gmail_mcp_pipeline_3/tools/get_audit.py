# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_audit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs)->str:
        p = _params(data, kwargs)
        miss = _require(p, ["audit_id"])
        if miss: return miss
        for a in _ensure(data, "audits", []):
            if a.get("audit_id") == p["audit_id"]:
                return _ok(a)
        return _err("audit_not_found", {"audit_id": p["audit_id"]})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"get_audit",
            "description":"Fetch a single audit by id.",
            "parameters":{"type":"object","properties":{
                "audit_id":{"type":"string"}
            },"required":["audit_id"]}
        }}
