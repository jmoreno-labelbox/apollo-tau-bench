# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _params
def _j(v):
    return v if isinstance(v, str) else json.dumps(v, separators=(",", ":"), ensure_ascii=False)

def _params(data: Dict[str, Any], kwargs: Dict[str, Any]) -> Dict[str, Any]:
    return kwargs or {}

def _ok(x):
    return _j(x)

def _ensure(data: Dict[str, Any], key: str, default):
    if key not in data or data[key] is None:
        data[key] = default
    return data[key]

class list_artifacts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        p = _params(data, kwargs)
        rows = []
        for a in _ensure(data, "figma_artifacts", []):
            if p.get("artifact_type") and a.get("artifact_type") != p["artifact_type"]:
                continue
            if p.get("owner_email") and a.get("owner_email") != p["owner_email"]:
                continue
            if p.get("figma_file_id") and a.get("figma_file_id") != p["figma_file_id"]:
                continue
            if p.get("tag"):
                tags = a.get("tags", [])
                if p["tag"] not in tags:
                    continue
            rows.append(a)
        return _ok({"rows": rows})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"list_artifacts",
            "description":"List Figma artifacts (files/pages/frames) with optional filters.",
            "parameters":{"type":"object","properties":{
                "artifact_type":{"type":"string"},
                "owner_email":{"type":"string"},
                "figma_file_id":{"type":"string"},
                "tag":{"type":"string"},
            }}
        }}