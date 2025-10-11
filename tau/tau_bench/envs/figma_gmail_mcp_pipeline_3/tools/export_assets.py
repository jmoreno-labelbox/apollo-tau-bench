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

def _export_ext_from_profile(profile: str) -> str:
    s = (profile or "").lower()
    if "png" in s: return "png"
    if "jpg" in s or "jpeg" in s: return "jpg"
    if "pdf" in s: return "pdf"
    return "png"

def _ensure(data: Dict[str, Any], key: str, default):
    if key not in data or data[key] is None:
        data[key] = default
    return data[key]

class export_assets(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        p = _params(data, kwargs)
        miss = _require(p, ["artifact_id","export_profile","request_id","timestamp"])
        if miss: return miss
        ext = _export_ext_from_profile(p["export_profile"])
        ymd = _ymd(p["timestamp"])
        export_id = f"exp-{p['artifact_id']}-{ymd}-{ext}-001"
        asset_id = f"asset_{p['request_id']}"
        asset = {"asset_id": asset_id, "export_id": export_id, "artifact_id": p["artifact_id"]}
        _ensure(data, "assets", []).append(asset)
        return _ok({"asset_id": asset_id, "export_id": export_id})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"export_assets",
            "description":"Export assets for an artifact using an export profile.",
            "parameters":{"type":"object","properties":{
                "artifact_id":{"type":"string"},
                "export_profile":{"type":"string"},
                "timestamp":{"type":"string"},
                "request_id":{"type":"string"}
            },"required":["artifact_id","export_profile","timestamp","request_id"]}
        }}