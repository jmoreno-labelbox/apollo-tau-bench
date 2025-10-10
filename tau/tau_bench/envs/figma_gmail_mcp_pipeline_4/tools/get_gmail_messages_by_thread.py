# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetGmailMessagesByThread(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves Gmail messages filtered by thread ID, sender, and other criteria.
        """
        message_id = kwargs.get('message_id')
        thread_id = kwargs.get('thread_id')
        sender_email = kwargs.get('sender_email')
        content_keywords = kwargs.get('content_keywords', [])
        has_attachments = kwargs.get('has_attachments')
        sent_after = kwargs.get('sent_after')
        sent_before = kwargs.get('sent_before')

        gmail_messages = data.get('gmail_messages', [])

        # If message_id is provided, return specific message
        if message_id:
            for message in gmail_messages:
                if message.get('message_id') == message_id:
                    return json.dumps(message, indent=2)
            return json.dumps({"error": f"Message with ID '{message_id}' not found."})

        # Filter messages by criteria
        results = []
        for message in gmail_messages:
            # Apply filters
            if thread_id:
                if message.get('thread_id') != thread_id:
                    continue

            if sender_email:
                if message.get('sender_email') != sender_email:
                    continue

            if content_keywords:
                content = message.get('body_text_stripped', '').lower()
                if not any(keyword.lower() in content for keyword in content_keywords):
                    continue

            if has_attachments is not None:
                attachments = message.get('attachments_asset_ids', [])
                if has_attachments and not attachments:
                    continue
                if not has_attachments and attachments:
                    continue

            # Apply date filters
            if sent_after:
                sent_ts = message.get('sent_ts', '')
                if sent_ts < sent_after:
                    continue

            if sent_before:
                sent_ts = message.get('sent_ts', '')
                if sent_ts > sent_before:
                    continue

            results.append(message)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_gmail_messages_by_thread",
                "description": "Retrieves Gmail messages filtered by thread ID, sender email, content keywords, attachment status, and date ranges for comprehensive message management.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {"type": "string", "description": "The ID of a specific message to retrieve."},
                        "thread_id": {"type": "string", "description": "Filter messages by thread ID."},
                        "sender_email": {"type": "string", "description": "Filter messages by sender email address."},
                        "content_keywords": {"type": "array", "items": {"type": "string"}, "description": "Filter messages by keywords in the content."},
                        "has_attachments": {"type": "boolean", "description": "Filter messages by attachment presence (true for messages with attachments, false for without)."},
                        "sent_after": {"type": "string", "description": "Filter messages sent after this ISO timestamp."},
                        "sent_before": {"type": "string", "description": "Filter messages sent before this ISO timestamp."}
                    }
                }
            }
        }
