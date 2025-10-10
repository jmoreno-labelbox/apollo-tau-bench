# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _params, _require


class create_fix_plan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        p = _params(data, kwargs)
        miss = _require(p, ["audit_id","owner_email","delivery_method","timestamp","request_id"])
        if miss: return miss
        w = _require_write(p)
        if w: return w

        # Derive artifact_id from audit_id "aud-<artifact_id>-<YYYYMMDD>-<seq>"
        audit_id = p["audit_id"]
        m = re.match(r"^aud-(?P<art>[^-]+)-(?P<date>\d{8})-(?P<seq>\d+)$", audit_id)
        if not m:
            return _err("invalid_audit_id_format")
        artifact_id = m.group("art")

        # Per ID_RULE: date derives from timestamp
        yyyymmdd = p["timestamp"][0:10].replace("-", "")
        plan_id = f"fp-{artifact_id}-{yyyymmdd}-001"
        plan = {
            "plan_id": plan_id,
            "audit_id": audit_id,
            "owner_email": p["owner_email"],
            "delivery_method": p["delivery_method"],
            "status": "DRAFTED",
            "created_ts": p["timestamp"],
        }
        _ensure(data, "fix_plans", []).append(plan)
        return _ok(plan)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"create_fix_plan",
            "description":"Create a fix plan for an audit (deterministic id).",
            "parameters":{"type":"object","properties":{
                "audit_id":{"type":"string"},
                "owner_email":{"type":"string"},
                "delivery_method":{"type":"string","enum":["COMMENTS","TICKETS","PDF","EMAIL"]},
                "timestamp":{"type":"string"},
                "request_id":{"type":"string"}
            },"required":["audit_id","owner_email","delivery_method","timestamp","request_id"]}
        }}
