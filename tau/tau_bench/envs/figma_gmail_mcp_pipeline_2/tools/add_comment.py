# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddComment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["artifact_id", "author_email", "content", "resolved_flag"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        comments: List[Dict[str, Any]] = data.get("figma_comments", [])
        comment_id = get_next_comment_id(data)
        created_ts = get_now_timestamp()
        source_message_id: Optional[str] = kwargs.get("source_message_id")

        new_comment = {
            "comment_id": comment_id,
            "artifact_id": kwargs["artifact_id"],
            "author_email": kwargs["author_email"],
            "content": kwargs["content"],
            "source_message_id_nullable": source_message_id,
            "created_ts": created_ts,
            "resolved_flag": kwargs["resolved_flag"]
        }

        comments.append(new_comment)
        data["figma_comments"] = comments
        return json.dumps(new_comment, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_comment",
                "description": "Add a new comment to figma_comments. source_message_id may be null.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "author_email": {"type": "string"},
                        "content": {"type": "string"},
                        "source_message_id": {"type": ["string", "null"]},
                        "resolved_flag": {"type": "boolean"}
                    },
                    "required": ["artifact_id", "author_email", "content", "resolved_flag"]
                }
            }
        }
