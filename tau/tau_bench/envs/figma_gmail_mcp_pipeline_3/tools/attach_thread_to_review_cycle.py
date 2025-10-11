# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _params, _require


class attach_thread_to_review_cycle(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs)->str:
        p = _params(data, kwargs)
        miss = _require(p, ["cycle_id","thread_id"])
        if miss: return miss
        for c in _ensure(data, "review_cycles", []):
            if c.get("cycle_id") == p["cycle_id"]:
                c["thread_id_nullable"] = p["thread_id"]
                return _ok({"cycle_id": c["cycle_id"], "thread_id": p["thread_id"]})
        return _err("cycle_not_found", {"cycle_id": p["cycle_id"]})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"attach_thread_to_review_cycle",
            "description":"Attach an email thread to a review cycle.",
            "parameters":{"type":"object","properties":{
                "cycle_id":{"type":"string"},
                "thread_id":{"type":"string"}
            },"required":["cycle_id","thread_id"]}
        }}
