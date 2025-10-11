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

class record_automation_run(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], )->str:
        p = _params(data, kwargs)
        miss = _require(p, ["task_name","status","request_id"])
        if miss: return miss
        run_id = f"run_{p['request_id']}"
        _ensure(data, "automation_runs", []).append({
            "run_id": run_id,
            "task_name": p["task_name"],
            "status": p["status"],
            "started_at": p.get("started_at"),
            "ended_at": p.get("ended_at"),
            "timestamp": p.get("timestamp"),
        })
        return _ok({"run_id": run_id, "status": p["status"]})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"record_automation_run",
            "description":"Record a deterministic automation run.",
            "parameters":{"type":"object","properties":{
                "task_name":{"type":"string"},
                "status":{"type":"string"},
                "started_at":{"type":"string"},
                "ended_at":{"type":"string"},
                "timestamp":{"type":"string"},
                "request_id":{"type":"string"}
            },"required":["task_name","status","request_id"]}
        }}