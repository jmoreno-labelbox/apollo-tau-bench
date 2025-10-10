# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class record_automation_run(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs)->str:
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
