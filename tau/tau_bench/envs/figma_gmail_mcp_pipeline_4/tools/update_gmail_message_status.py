# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateGmailMessageStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates Gmail message metadata and manages message workflow tracking.
        """
        message_id = kwargs.get('message_id')
        sender_email = kwargs.get('sender_email')
        body_html = kwargs.get('body_html')
        body_text_stripped = kwargs.get('body_text_stripped')
        attachments_asset_ids = kwargs.get('attachments_asset_ids', [])
        message_metadata = kwargs.get('message_metadata', {})

        if not message_id:
            return json.dumps({"error": "message_id is required."})

        gmail_messages = data.get('gmail_messages', [])

        # Find the message
        message_found = False
        for message in gmail_messages:
            if message.get('message_id') == message_id:
                message_found = True

                # Update message fields
                if sender_email:
                    message['sender_email'] = sender_email
                if body_html:
                    message['body_html'] = body_html
                if body_text_stripped:
                    message['body_text_stripped'] = body_text_stripped
                if attachments_asset_ids:
                    message['attachments_asset_ids'] = attachments_asset_ids

                message['last_updated'] = datetime.now().isoformat()

                # Add metadata
                if message_metadata:
                    for key, value in message_metadata.items():
                        message[key] = value

                # Log the update
                if 'update_history' not in message:
                    message['update_history'] = []
                message['update_history'].append({
                    "timestamp": datetime.now().isoformat(),
                    "updated_fields": list(kwargs.keys()),
                    "metadata": message_metadata
                })

                break

        if not message_found:
            return json.dumps({"error": f"Gmail message with ID '{message_id}' not found."})

        return json.dumps({
            "success": True,
            "message_id": message_id,
            "updated_at": datetime.now().isoformat(),
            "updated_fields": list(kwargs.keys())
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_gmail_message_status",
                "description": "Updates Gmail message metadata including sender, body content, attachments, and custom metadata for message workflow tracking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {"type": "string", "description": "The ID of the Gmail message to update."},
                        "sender_email": {"type": "string", "description": "Optional updated sender email address."},
                        "body_html": {"type": "string", "description": "Optional updated HTML body content."},
                        "body_text_stripped": {"type": "string", "description": "Optional updated plain text body content."},
                        "attachments_asset_ids": {"type": "array", "items": {"type": "string"}, "description": "Optional updated list of attachment asset IDs."},
                        "message_metadata": {"type": "object", "description": "Optional additional metadata fields for the message."}
                    },
                    "required": ["message_id"]
                }
            }
        }
