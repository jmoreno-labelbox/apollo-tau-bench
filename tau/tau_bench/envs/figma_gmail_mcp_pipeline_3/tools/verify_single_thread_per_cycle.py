# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class verify_single_thread_per_cycle(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs)->str:
        p = _params(data, kwargs)
        miss = _require(p, ["cycle_id"])
        if miss: return miss
        for c in _ensure(data, "review_cycles", []):
            if c.get("cycle_id") == p["cycle_id"]:
                ok = c.get("thread_id_nullable") is not None
                return _ok({"ok": ok, "cycle_id": c["cycle_id"]})
        return _ok({"ok": False, "cycle_id": p["cycle_id"]})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"verify_single_thread_per_cycle",
            "description":"Verify each cycle has exactly one attached thread (simplified).",
            "parameters":{"type":"object","properties":{
                "cycle_id":{"type":"string"}
            },"required":["cycle_id"]}
        }}
