# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateFigmaCommentFromGmailMessage(Tool):  # WRITE
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        artifact_id: str,
        gmail_message_id: str,
    ) -> str:
        # Validate input
        if not isinstance(artifact_id, str) or not artifact_id:
            return json.dumps({"error": "artifact_id must be a non-empty string"})
        if not isinstance(gmail_message_id, str) or not gmail_message_id:
            return json.dumps({"error": "gmail_message_id must be a non-empty string"})
        gmail_messages = data.get("gmail_messages", [])
        figma_comments = data.get("figma_comments", [])
        # Find the gmail message
        gmail_msg = next((m for m in gmail_messages if m.get("message_id") == gmail_message_id), None)
        if not gmail_msg:
            return json.dumps({"error": "gmail_message_id not found in gmail_messages"})
        commenter_email = gmail_msg.get("sender_email")
        comment_text = gmail_msg.get("body_text_stripped")
        next_num = len(figma_comments) + 1
        comment_id = f"comment_{next_num:03d}"
        created_ts = "2025-08-26T12:00:00Z"  # Use current date/time in production
        new_comment = {
            "comment_id": comment_id,
            "artifact_id": artifact_id,
            "message_id": gmail_message_id,
            "commenter_email": commenter_email,
            "comment_text": comment_text,
            "created_ts": created_ts
        }
        figma_comments.append(new_comment)
        return json.dumps({"new_comment": new_comment})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_figma_comment_from_gmail_message",
                "description": "Create a new Figma comment using a Gmail message ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string", "description": "The artifact ID the comment is for."},
                        "gmail_message_id": {"type": "string", "description": "The Gmail message ID used for the comment."},
                        "created_ts": {"type": "string", "description": "Timestamp of comment creation (optional)."}
                    },
                    "required": ["artifact_id", "gmail_message_id"]
                }
            }
        }
