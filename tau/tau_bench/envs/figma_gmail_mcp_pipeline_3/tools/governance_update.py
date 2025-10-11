# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _params, _require












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

class governance_update(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs)->str:
        p = _params(data, kwargs)
        miss = _require(p, ["artifact_id","request_id"])
        if miss: return miss
        add = p.get("add_tags", [])
        rem = p.get("remove_tags", [])
        for a in _ensure(data, "figma_artifacts", []):
            if a.get("artifact_id") == p["artifact_id"]:
                tags = set(a.get("current_tags", []))
                for t in add: tags.add(t)
                for t in rem:
                    if t in tags: tags.remove(t)
                a["current_tags"] = list(tags)
                return _ok({"artifact_id": a["artifact_id"], "tags": a["current_tags"]})
        return _err("artifact_not_found", {"artifact_id": p["artifact_id"]})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"governance_update",
            "description":"Add/remove tags on an artifact.",
            "parameters":{"type":"object","properties":{
                "artifact_id":{"type":"string"},
                "add_tags":{"type":"array","items":{"type":"string"}},
                "remove_tags":{"type":"array","items":{"type":"string"}},
                "timestamp":{"type":"string"},
                "request_id":{"type":"string"}
            },"required":["artifact_id","request_id"]}
        }}