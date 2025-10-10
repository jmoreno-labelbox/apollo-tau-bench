# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class list_review_approvals(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs)->str:
        p = _params(data, kwargs)
        miss = _require(p, ["cycle_id"])
        if miss: return miss
        rows = []
        for c in _ensure(data, "review_cycles", []):
            if c.get("cycle_id") == p["cycle_id"]:
                for email, ts in c.get("approvals", {}).items():
                    rows.append({"approver_email": email, "approved_ts_nullable": ts})
                break
        return _ok({"rows": rows})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"list_review_approvals",
            "description":"List approvals for a review cycle.",
            "parameters":{"type":"object","properties":{
                "cycle_id":{"type":"string"}
            },"required":["cycle_id"]}
        }}
