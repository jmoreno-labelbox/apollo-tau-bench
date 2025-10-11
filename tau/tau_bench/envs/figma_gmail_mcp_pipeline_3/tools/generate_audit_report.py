# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _params, _require
def _j(v):
    return v if isinstance(v, str) else json.dumps(v, separators=(",", ":"), ensure_ascii=False)

def _err(msg: str) -> str:
    return json.dumps({'ok': False, 'error': msg}, indent=2)

def _ymd(ts: str) -> str:
    try:
        return datetime.fromisoformat(ts.replace("Z","+00:00")).strftime("%Y%m%d")
    except Exception:
        return datetime.utcnow().strftime("%Y%m%d")

def _require(p: Dict[str, Any], req: List[str]):
    missing = [k for k in req if p.get(k) in (None, "")]
    if missing:
        return _err("missing_params", {"missing": missing})
    return None

def _params(data: Dict[str, Any], kwargs: Dict[str, Any]) -> Dict[str, Any]:
    return kwargs or {}

def _ok(x):
    return _j(x)

def _export_ext_from_format(fmt: str) -> str:
    s = (fmt or "").lower()
    if "pdf" in s: return "pdf"
    if "png" in s: return "png"
    if "jpg" in s or "jpeg" in s: return "jpg"
    return "pdf"

def _ensure(data: Dict[str, Any], key: str, default):
    if key not in data or data[key] is None:
        data[key] = default
    return data[key]

class GenerateAuditReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], )->str:
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