from tau_bench.envs.tool import Tool
import html
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AddComment(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        author_email: str,
        content: str,
        resolved_flag: bool,
        artifact_id: str = None,
        source_message_id: str = None
    ) -> str:
        required = ["artifact_id", "author_email", "content", "resolved_flag"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        comments: list[dict[str, Any]] = data.get("figma_comments", [])
        comment_id = get_next_comment_id(data)
        created_ts = get_now_timestamp()

        new_comment = {
            "comment_id": comment_id,
            "artifact_id": artifact_id,
            "author_email": author_email,
            "content": content,
            "source_message_id_nullable": source_message_id,
            "created_ts": created_ts,
            "resolved_flag": resolved_flag,
        }

        comments.append(new_comment)
        data["figma_comments"] = comments
        payload = new_comment
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddComment",
                "description": "Add a new comment to figma_comments. source_message_id may be null.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "author_email": {"type": "string"},
                        "content": {"type": "string"},
                        "source_message_id": {"type": ["string", "null"]},
                        "resolved_flag": {"type": "boolean"},
                    },
                    "required": [
                        "artifact_id",
                        "author_email",
                        "content",
                        "resolved_flag",
                    ],
                },
            },
        }
