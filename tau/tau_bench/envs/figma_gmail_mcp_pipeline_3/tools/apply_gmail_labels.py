# Sierra copyright ownership

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _params, _require
def _j(v):
    return v if isinstance(v, str) else json.dumps(v, separators=(",", ":"), ensure_ascii=False)

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

class apply_gmail_labels(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        p = _params(data, kwargs)
        miss = _require(p, ["thread_id","add_labels","request_id"])
        if miss: return miss
        threads = _ensure(data, "gmail_threads", [])
        for t in threads:
            if t.get("thread_id") == p["thread_id"]:
                labels = set(t.get("labels", []))
                for lab in p.get("add_labels", []):
                    labels.add(lab)
                t["labels"] = list(labels)
                return _ok({"labels": t["labels"]})
        return _err("thread_not_found", {"thread_id": p["thread_id"]})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"apply_gmail_labels",
            "description":"Apply one or more labels to a Gmail thread.",
            "parameters":{"type":"object","properties":{
                "thread_id":{"type":"string"},
                "add_labels":{"type":"array","items":{"type":"string"}},
                "timestamp":{"type":"string"},
                "request_id":{"type":"string"}
            },"required":["thread_id","add_labels","request_id"]}
        }}