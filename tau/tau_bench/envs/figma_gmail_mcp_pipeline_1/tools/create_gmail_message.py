from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateGmailMessage(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        sender_email: str,
        workflow_type: str,
        thread_id: str = None,
        attachments_asset_ids: list[str] = None,
    ) -> str:
        pass
        #Check the input for validity
        if not isinstance(sender_email, str) or not sender_email:
            payload = {"error": "sender_email must be a non-empty string"}
            out = json.dumps(payload)
            return out
        if (
            not isinstance(workflow_type, str)
            or not workflow_type
            or workflow_type not in ["review", "release"]
        ):
            payload = {"error": "workflow_type must be a non-empty string"}
            out = json.dumps(payload)
            return out
        gmail_messages = data.get("gmail_messages", [])
        next_num = len(gmail_messages) + 1
        message_id = f"msg_{next_num:03d}"
        sent_ts = "2025-08-26T12:00:00Z"  #Utilize the current date/time in production
        if workflow_type == "review":
            body_text_stripped = "Hi, please review the attached design."
        elif workflow_type == "release":
            body_text_stripped = "Hi, please find the designs for release attached."
        new_message = {
            "message_id": message_id,
            "thread_id": thread_id,
            "sender_email": sender_email,
            "body_html": f"<p>{body_text_stripped.replace(',', ',</p><p>', 1)}</p>",
            "body_text_stripped": body_text_stripped,
            "sent_ts": sent_ts,
            "attachments_asset_ids": (
                attachments_asset_ids if attachments_asset_ids else []
            ),
        }
        gmail_messages.append(new_message)
        payload = {"new_message": new_message}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateGmailMessage",
                "description": "Create a new Gmail message.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sender_email": {
                            "type": "string",
                            "description": "Sender's email address.",
                        },
                        "body_text_stripped": {
                            "type": "string",
                            "description": "Plain text body of the message.",
                        },
                        "thread_id": {
                            "type": "string",
                            "description": "Optional thread ID for the message.",
                        },
                        "attachments_asset_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional list of asset IDs for attachments.",
                        },
                    },
                    "required": ["sender_email", "body_text_stripped"],
                },
            },
        }
