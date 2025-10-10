# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _params, _require


class deliver_fix_plan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs)->str:
        p = _params(data, kwargs)
        miss = _require(p, ["plan_id","request_id"])
        if miss: return miss
        for pl in _ensure(data, "fix_plans", []):
            if pl.get("plan_id") == p["plan_id"]:
                pl["status"] = "DELIVERED"
                return _ok({"plan_id": pl["plan_id"], "status": pl["status"]})
        return _err("plan_not_found", {"plan_id": p["plan_id"]})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"deliver_fix_plan",
            "description":"Mark a fix plan as delivered.",
            "parameters":{"type":"object","properties":{
                "plan_id":{"type":"string"},
                "request_id":{"type":"string"}
            },"required":["plan_id","request_id"]}
        }}
