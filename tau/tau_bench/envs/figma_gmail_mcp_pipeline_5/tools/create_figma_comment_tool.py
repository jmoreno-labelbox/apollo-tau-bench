# Sierra copyright.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateFigmaCommentTool(Tool):
    """Create an anchored comment on an artifact. Deterministic comment_id from inputs."""

    @staticmethod
    def invoke(data: Dict[str, Any], anchor_ref, artifact_id, author_email, body, created_ts) -> str:
        artifact_id = _require_str(artifact_id, "artifact_id")
        author_email = _require_str(author_email, "author_email")
        body = _require_str(body, "body")
        anchor_ref = _require_str(anchor_ref, "anchor_ref")
        created_ts = _require_str(created_ts, "created_ts")
        if not all([artifact_id, author_email, body, anchor_ref, created_ts]):
            return json.dumps({"error":"artifact_id, author_email, body, anchor_ref, created_ts are required"})

        comments = _safe_table(data, "figma_comments")
        comment_id = _det_id("cmt", [artifact_id, author_email, anchor_ref, created_ts, body[:32]])
        # Idempotent update or insert based on comment_id
        idx = _index_by(comments, "comment_id")
        row = {
            "comment_id": comment_id,
            "artifact_id": artifact_id,
            "author_email": author_email,
            "anchor_ref": anchor_ref,
            "body": body,
            "created_ts": created_ts
        }
        if comment_id in idx:
            comments[idx[comment_id]] = row
        else:
            comments.append(row)

        return json.dumps({"success": True, "comment_id": comment_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"create_figma_comment",
            "description":"Create/update a Figma comment anchored to an artifact (deterministic id).",
            "parameters":{"type":"object","properties":{
                "artifact_id":{"type":"string"},
                "author_email":{"type":"string"},
                "body":{"type":"string"},
                "anchor_ref":{"type":"string","description":"Anchor reference in Figma (e.g., node path or key)."},
                "created_ts":{"type":"string","description":"Explicit ISO timestamp."}
            },"required":["artifact_id","author_email","body","anchor_ref","created_ts"]}
        }}
