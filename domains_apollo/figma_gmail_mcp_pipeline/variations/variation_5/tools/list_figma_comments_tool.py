from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class ListFigmaCommentsTool(Tool):
    """Enumerate comments for an artifact, optionally filtered by author or date."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        artifact_id: str = None,
        author_email: str = None,
        since_ts: str = None
    ) -> str:
        artifact_id = _require_str(artifact_id, "artifact_id")

        if not artifact_id:
            payload = {"error": "artifact_id is required"}
            out = json.dumps(payload)
            return out

        rows = data.get("figma_comments", [])
        out = []
        for r in rows:
            if r.get("artifact_id") != artifact_id:
                continue
            if author_email and r.get("author_email") != author_email:
                continue
            if since_ts and r.get("created_ts", "") < since_ts:
                continue
            out.append(
                _small_fields(
                    r,
                    ["comment_id", "author_email", "anchor_ref", "body", "created_ts"],
                )
            )

        out.sort(key=lambda r: r.get("created_ts", ""))
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListFigmaComments",
                "description": "List Figma comments for an artifact with simple filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "author_email": {"type": "string"},
                        "since_ts": {"type": "string"},
                    },
                    "required": ["artifact_id"],
                },
            },
        }
