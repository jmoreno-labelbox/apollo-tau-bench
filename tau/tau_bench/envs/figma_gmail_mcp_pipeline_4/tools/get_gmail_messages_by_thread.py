from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetGmailMessagesByThread(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        message_id: str = None,
        thread_id: str = None,
        sender_email: str = None,
        content_keywords: list[str] = [],
        has_attachments: bool = None,
        sent_after: str = None,
        sent_before: str = None
    ) -> str:
        """
        Obtains Gmail messages filtered by thread ID, sender, and additional criteria.
        """
        gmail_messages = data.get("gmail_messages", [])

        # Return the specific message if message_id is given
        if message_id:
            for message in gmail_messages:
                if message.get("message_id") == message_id:
                    payload = message
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Message with ID '{message_id}' not found."}
            out = json.dumps(payload)
            return out

        # Sort messages based on specified criteria
        results = []
        for message in gmail_messages:
            # Implement filters
            if thread_id:
                if message.get("thread_id") != thread_id:
                    continue

            if sender_email:
                if message.get("sender_email") != sender_email:
                    continue

            if content_keywords:
                content = message.get("body_text_stripped", "").lower()
                if not any(keyword.lower() in content for keyword in content_keywords):
                    continue

            if has_attachments is not None:
                attachments = message.get("attachments_asset_ids", [])
                if has_attachments and not attachments:
                    continue
                if not has_attachments and attachments:
                    continue

            # Enforce date filters
            if sent_after:
                sent_ts = message.get("sent_ts", "")
                if sent_ts < sent_after:
                    continue

            if sent_before:
                sent_ts = message.get("sent_ts", "")
                if sent_ts > sent_before:
                    continue

            results.append(message)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getGmailMessagesByThread",
                "description": "Retrieves Gmail messages filtered by thread ID, sender email, content keywords, attachment status, and date ranges for comprehensive message management.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {
                            "type": "string",
                            "description": "The ID of a specific message to retrieve.",
                        },
                        "thread_id": {
                            "type": "string",
                            "description": "Filter messages by thread ID.",
                        },
                        "sender_email": {
                            "type": "string",
                            "description": "Filter messages by sender email address.",
                        },
                        "content_keywords": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Filter messages by keywords in the content.",
                        },
                        "has_attachments": {
                            "type": "boolean",
                            "description": "Filter messages by attachment presence (true for messages with attachments, false for without).",
                        },
                        "sent_after": {
                            "type": "string",
                            "description": "Filter messages sent after this ISO timestamp.",
                        },
                        "sent_before": {
                            "type": "string",
                            "description": "Filter messages sent before this ISO timestamp.",
                        },
                    },
                },
            },
        }
