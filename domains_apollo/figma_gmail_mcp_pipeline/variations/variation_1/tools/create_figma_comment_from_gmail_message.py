from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateFigmaCommentFromGmailMessage(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        artifact_id: str,
        gmail_message_id: str,
    ) -> str:
        pass
        #Check the input for validity
        if not isinstance(artifact_id, str) or not artifact_id:
            payload = {"error": "artifact_id must be a non-empty string"}
            out = json.dumps(payload)
            return out
        if not isinstance(gmail_message_id, str) or not gmail_message_id:
            payload = {"error": "gmail_message_id must be a non-empty string"}
            out = json.dumps(payload)
            return out
        gmail_messages = data.get("gmail_messages", [])
        figma_comments = data.get("figma_comments", [])
        #Locate the Gmail message
        gmail_msg = next(
            (m for m in gmail_messages if m.get("message_id") == gmail_message_id), None
        )
        if not gmail_msg:
            payload = {"error": "gmail_message_id not found in gmail_messages"}
            out = json.dumps(payload)
            return out
        commenter_email = gmail_msg.get("sender_email")
        comment_text = gmail_msg.get("body_text_stripped")
        next_num = len(figma_comments) + 1
        comment_id = f"comment_{next_num:03d}"
        created_ts = "2025-08-26T12:00:00Z"  #Utilize the current date/time in production
        new_comment = {
            "comment_id": comment_id,
            "artifact_id": artifact_id,
            "message_id": gmail_message_id,
            "commenter_email": commenter_email,
            "comment_text": comment_text,
            "created_ts": created_ts,
        }
        figma_comments.append(new_comment)
        payload = {"new_comment": new_comment}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateFigmaCommentFromGmailMessage",
                "description": "Create a new Figma comment using a Gmail message ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {
                            "type": "string",
                            "description": "The artifact ID the comment is for.",
                        },
                        "gmail_message_id": {
                            "type": "string",
                            "description": "The Gmail message ID used for the comment.",
                        },
                        "created_ts": {
                            "type": "string",
                            "description": "Timestamp of comment creation (optional).",
                        },
                    },
                    "required": ["artifact_id", "gmail_message_id"],
                },
            },
        }
