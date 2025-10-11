# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _params, _require














def _require_write(p: Dict[str, Any]):
    miss = _require(p, ["timestamp", "request_id"])
    if miss:
        return miss
    ts = p.get("timestamp")
    if not isinstance(ts, str) or not _ISO8601Z.match(ts):
        return _err("invalid_timestamp_format")
    rid = p.get("request_id")
    if not isinstance(rid, str) or not rid:
        return _err("invalid_request_id")
    return None

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

class create_fix_plan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        p = _params(data, kwargs)
        miss = _require(p, ["audit_id","owner_email","delivery_method","timestamp","request_id"])
        if miss: return miss
        w = _require_write(p)
        if w: return w

        # Extract artifact_id from audit_id formatted as "aud-<artifact_id>-<YYYYMMDD>-<seq>"
        audit_id = p["audit_id"]
        m = re.match(r"^aud-(?P<art>[^-]+)-(?P<date>\d{8})-(?P<seq>\d+)$", audit_id)
        if not m:
            return _err("invalid_audit_id_format")
        artifact_id = m.group("art")

        # According to ID_RULE, the date is extracted from the timestamp.
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