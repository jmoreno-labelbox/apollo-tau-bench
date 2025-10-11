# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _params, _require












def _require(p: Dict[str, Any], req: List[str]):
    missing = [k for k in req if p.get(k) in (None, "")]
    if missing:
        return _err("missing_params", {"missing": missing})
    return None

def _params(data: Dict[str, Any], kwargs: Dict[str, Any]) -> Dict[str, Any]:
    return kwargs or {}

def _ok(x):
    return _j(x)

def _err(code, extra=None):
    payload = {"error": code}
    if isinstance(extra, dict):
        payload.update(extra)
    return _j(payload)

def _ensure(data: Dict[str, Any], key: str, default):
    if key not in data or data[key] is None:
        data[key] = default
    return data[key]

class get_release_diff(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs)->str:
        p = _params(data, kwargs)
        miss = _require(p, ["release_id"])
        if miss: return miss
        for r in _ensure(data, "releases", []):
            if r.get("release_id") == p["release_id"]:
                return _ok({"release_id": r["release_id"], "diff": r.get("diff", {})})
        return _err("release_not_found", {"release_id": p["release_id"]})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"get_release_diff",
            "description":"Fetch a release diff summary.",
            "parameters":{"type":"object","properties":{
                "release_id":{"type":"string"}
            },"required":["release_id"]}
        }}