# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _params, _require


class create_figma_comment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        p = _params(data, kwargs)
        miss = _require(p, ["artifact_id","author_email","content","request_id"])
        if miss: return miss
        comment_id = f"comment_{p['request_id']}"
        c = {
            "comment_id": comment_id,
            "artifact_id": p["artifact_id"],
            "author_email": p["author_email"],
            "content": p["content"],
            "timestamp": p.get("timestamp"),
            "resolved_flag": False
        }
        _ensure(data, "figma_comments", []).append(c)
        return _ok({"comment_id": comment_id})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"create_figma_comment",
            "description":"Create a new comment on a Figma artifact.",
            "parameters":{"type":"object","properties":{
                "artifact_id":{"type":"string"},
                "author_email":{"type":"string"},
                "content":{"type":"string"},
                "timestamp":{"type":"string"},
                "request_id":{"type":"string"}
            },"required":["artifact_id","author_email","content","request_id"]}
        }}
