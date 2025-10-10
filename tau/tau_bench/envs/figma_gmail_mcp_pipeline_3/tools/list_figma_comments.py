# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _params


class list_figma_comments(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        p = _params(data, kwargs)
        rows = []
        for c in _ensure(data, "figma_comments", []):
            if p.get("artifact_id") and c.get("artifact_id") != p["artifact_id"]:
                continue
            if "resolved_flag" in p and bool(c.get("resolved_flag", False)) != bool(p["resolved_flag"]):
                continue
            rows.append(c)
        return _ok({"rows": rows})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"list_figma_comments",
            "description":"List comments for a Figma artifact.",
            "parameters":{"type":"object","properties":{
                "artifact_id":{"type":"string"},
                "resolved_flag":{"type":"boolean"}
            }}
        }}
