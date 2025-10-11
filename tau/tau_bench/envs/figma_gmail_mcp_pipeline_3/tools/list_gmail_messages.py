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

class list_gmail_messages(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        p = _params(data, kwargs)
        miss = _require(p, ["thread_id"])
        if miss: return miss
        rows = []
        messages = _ensure(data, "gmail_messages", [])
        for m in messages:
            if m.get("thread_id") == p["thread_id"]:
                rows.append({
                    "message_id": m.get("message_id"),
                    "sender_email": m.get("sender_email"),
                    "recipients": m.get("recipients", []),
                    "body_html": m.get("body_html"),
                    "timestamp": m.get("timestamp"),
                })
                break
        return _ok({"rows": rows})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"list_gmail_messages",
            "description":"List messages for a Gmail thread.",
            "parameters":{"type":"object","properties":{
                "thread_id":{"type":"string"}
            }}
        }}