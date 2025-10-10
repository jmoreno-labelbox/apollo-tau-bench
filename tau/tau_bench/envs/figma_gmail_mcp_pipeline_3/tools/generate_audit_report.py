# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _params, _require


class GenerateAuditReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs)->str:
        p = _params(data, kwargs)
        miss = _require(p, ["artifact_id","audit_id","format","timestamp","request_id"])
        if miss: return miss
        ext = _export_ext_from_format(p["format"])
        ymd = _ymd(p["timestamp"])
        asset_id = f"exp-{p['artifact_id']}-{ymd}-{ext}-001"
        _ensure(data, "assets", []).append({
            "asset_id": asset_id,
            "artifact_id": p["artifact_id"],
            "audit_id": p["audit_id"],
            "kind": "audit_report",
        })
        return _ok({"asset_id": asset_id})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"GenerateAuditReport",
            "description":"Generate an audit report asset for an artifact.",
            "parameters":{"type":"object","properties":{
                "artifact_id":{"type":"string"},
                "audit_id":{"type":"string"},
                "format":{"type":"string"},
                "timestamp":{"type":"string"},
                "request_id":{"type":"string"}
            },"required":["artifact_id","audit_id","format","timestamp","request_id"]}
        }}
