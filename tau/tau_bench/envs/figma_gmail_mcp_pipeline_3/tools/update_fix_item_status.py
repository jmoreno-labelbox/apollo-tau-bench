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

class update_fix_item_status(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs)->str:
        p = _params(data, kwargs)
        miss = _require(p, ["plan_id","item_id","status"])
        if miss: return miss
        for pl in _ensure(data, "fix_plans", []):
            if pl.get("plan_id") == p["plan_id"]:
                for it in pl.get("items", []):
                    if it.get("item_id") == p["item_id"]:
                        it["status"] = p["status"]
                        return _ok({"plan_id": pl["plan_id"], "item_id": p["item_id"], "status": p["status"]})
        return _err("item_not_found", {"plan_id": p.get("plan_id"), "item_id": p.get("item_id")})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"update_fix_item_status",
            "description":"Update the status of a single fix item.",
            "parameters":{"type":"object","properties":{
                "plan_id":{"type":"string"},
                "item_id":{"type":"string"},
                "status":{"type":"string"}
            },"required":["plan_id","item_id","status"]}
        }}