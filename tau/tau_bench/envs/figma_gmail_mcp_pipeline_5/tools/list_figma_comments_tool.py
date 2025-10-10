# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListFigmaCommentsTool(Tool):
    """List comments for an artifact, optionally filtered by author or since."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        artifact_id = _require_str(kwargs.get("artifact_id"), "artifact_id")
        author_email = kwargs.get("author_email")
        since_ts = kwargs.get("since_ts")

        if not artifact_id:
            return json.dumps({"error":"artifact_id is required"})

        rows = data.get("figma_comments", [])
        out = []
        for r in rows:
            if r.get("artifact_id") != artifact_id:
                continue
            if author_email and r.get("author_email") != author_email:
                continue
            if since_ts and r.get("created_ts","") < since_ts:
                continue
            out.append(_small_fields(r, ["comment_id","author_email","anchor_ref","body","created_ts"]))

        out.sort(key=lambda r: r.get("created_ts",""))
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"list_figma_comments",
            "description":"List Figma comments for an artifact with simple filters.",
            "parameters":{"type":"object","properties":{
                "artifact_id":{"type":"string"},
                "author_email":{"type":"string"},
                "since_ts":{"type":"string"}
            },"required":["artifact_id"]}
        }}
