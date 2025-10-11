# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _params, _require
def _j(v):
    return v if isinstance(v, str) else json.dumps(v, separators=(",", ":"), ensure_ascii=False)

def _err(msg: str) -> str:
    return json.dumps({'ok': False, 'error': msg}, indent=2)

def _require(p: Dict[str, Any], req: List[str]):
    missing = [k for k in req if p.get(k) in (None, "")]
    if missing:
        return _err("missing_params", {"missing": missing})
    return None

def _params(data: Dict[str, Any], kwargs: Dict[str, Any]) -> Dict[str, Any]:
    return kwargs or {}

def _ok(x):
    return _j(x)

def _ensure(data: Dict[str, Any], key: str, default):
    if key not in data or data[key] is None:
        data[key] = default
    return data[key]

class get_review_cycle(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any],**kwargs)->str:
        p = _params(data, kwargs)
        miss = _require(p, ["cycle_id"])
        if miss: return miss
        for c in _ensure(data, "review_cycles", []):
            if c.get("cycle_id") == p["cycle_id"]:
                return _ok(c)
        return _ok({"cycle_id": p["cycle_id"], "status":"", "thread_id_nullable": None})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"get_review_cycle",
            "description":"Fetch a review cycle summary.",
            "parameters":{"type":"object","properties":{
                "cycle_id":{"type":"string"},
                "request_id":{"type":"string"}
            },"required":["cycle_id"]}
        }}