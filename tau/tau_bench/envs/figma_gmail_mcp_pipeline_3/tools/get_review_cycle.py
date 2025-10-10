# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_review_cycle(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs)->str:
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
