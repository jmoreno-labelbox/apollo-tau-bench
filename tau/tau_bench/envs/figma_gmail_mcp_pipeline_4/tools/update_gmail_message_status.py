from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class UpdateGmailMessageStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        message_id: str = None,
        sender_email: str = None,
        body_html: str = None,
        body_text_stripped: str = None,
        attachments_asset_ids: list = None,
        message_metadata: dict = None,
        new_status: str = None,
        updated_by: str = None
    ) -> str:
        """
        Modifies Gmail message metadata and oversees message workflow tracking.
        """
        if attachments_asset_ids is None:
            attachments_asset_ids = []
        if message_metadata is None:
            message_metadata = {}

        if not message_id:
            payload = {"error": "message_id is required."}
            out = json.dumps(payload)
            return out

        gmail_messages = data.get("gmail_messages", [])

        # Locate the message
        message_found = False
        for message in gmail_messages:
            if message.get("message_id") == message_id:
                message_found = True

                # Revise fields of the message
                if sender_email:
                    message["sender_email"] = sender_email
                if body_html:
                    message["body_html"] = body_html
                if body_text_stripped:
                    message["body_text_stripped"] = body_text_stripped
                if attachments_asset_ids:
                    message["attachments_asset_ids"] = attachments_asset_ids

                message["last_updated"] = datetime.now().isoformat()

                # Include metadata
                if message_metadata:
                    for key, value in message_metadata.items():
                        message[key] = value

                # Document the update
                if "update_history" not in message:
                    message["update_history"] = []
                message["update_history"].append(
                    {
                        "timestamp": datetime.now().isoformat(),
                        "updated_fields": [
                            "message_id",
                            "sender_email",
                            "body_html",
                            "body_text_stripped",
                            "attachments_asset_ids",
                            "message_metadata",
                        ],
                        "metadata": message_metadata,
                    }
                )

                break

        if not message_found:
            payload = {"error": f"Gmail message with ID '{message_id}' not found."}
            out = json.dumps(payload)
            return out

        payload = {
            "success": True,
            "message_id": message_id,
            "updated_at": datetime.now().isoformat(),
            "updated_fields": [
                "message_id",
                "sender_email",
                "body_html",
                "body_text_stripped",
                "attachments_asset_ids",
                "message_metadata",
            ],
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateGmailMessageStatus",
                "description": "Updates Gmail message metadata including sender, body content, attachments, and custom metadata for message workflow tracking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {
                            "type": "string",
                            "description": "The ID of the Gmail message to update.",
                        },
                        "sender_email": {
                            "type": "string",
                            "description": "Optional updated sender email address.",
                        },
                        "body_html": {
                            "type": "string",
                            "description": "Optional updated HTML body content.",
                        },
                        "body_text_stripped": {
                            "type": "string",
                            "description": "Optional updated plain text body content.",
                        },
                        "attachments_asset_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional updated list of attachment asset IDs.",
                        },
                        "message_metadata": {
                            "type": "object",
                            "description": "Optional additional metadata fields for the message.",
                        },
                    },
                    "required": ["message_id"],
                },
            },
        }
