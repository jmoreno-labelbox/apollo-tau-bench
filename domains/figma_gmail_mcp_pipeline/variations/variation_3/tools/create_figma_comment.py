from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class create_figma_comment(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        artifact_id: str = None,
        author_email: str = None,
        content: str = None,
        request_id: str = None,
        timestamp: str = None,
        source_message_id_nullable: str = None
    ) -> str:
        p = {
            "artifact_id": artifact_id,
            "author_email": author_email,
            "content": content,
            "request_id": request_id,
            "timestamp": timestamp
        }
        miss = _require(p, ["artifact_id", "author_email", "content", "request_id"])
        if miss:
            return miss
        comment_id = f"comment_{p['request_id']}"
        c = {
            "comment_id": comment_id,
            "artifact_id": p["artifact_id"],
            "author_email": p["author_email"],
            "content": p["content"],
            "timestamp": p.get("timestamp"),
            "resolved_flag": False,
        }
        _ensure(data, "figma_comments", []).append(c)
        return _ok({"comment_id": comment_id})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateFigmaComment",
                "description": "Create a new comment on a Figma artifact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "author_email": {"type": "string"},
                        "content": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": [
                        "artifact_id",
                        "author_email",
                        "content",
                        "request_id",
                    ],
                },
            },
        }
