# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_audit_status(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs)->str:
        p = _params(data, kwargs)
        miss = _require(p, ["audit_id","status","request_id"])
        if miss: return miss
        for a in _ensure(data, "audits", []):
            if a.get("audit_id") == p["audit_id"]:
                a["status"] = p["status"]
                a["updated_at"] = p.get("updated_at")
                return _ok({"audit_id": a["audit_id"], "status": a["status"]})
        return _err("audit_not_found", {"audit_id": p["audit_id"]})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"update_audit_status",
            "description":"Update an audit's status deterministically.",
            "parameters":{"type":"object","properties":{
                "audit_id":{"type":"string"},
                "status":{"type":"string"},
                "updated_at":{"type":"string"},
                "timestamp":{"type":"string"},
                "request_id":{"type":"string"}
            },"required":["audit_id","status","request_id"]}
        }}
