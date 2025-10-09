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

class StartEmailThread(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        attachments_asset_ids: list[str] = None,
        body_html: str = None,
        current_labels: list[str] = None,
        recipients: list[str] = None,
        sender_id: str = None,
        subject: str = None
    ) -> str:
        required = [
            "subject",
            "sender_id",
            "recipients",
            "current_labels",
            "body_html",
            "attachments_asset_ids",
        ]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        threads: list[dict[str, Any]] = data.get("gmail_threads", [])
        messages: list[dict[str, Any]] = data.get("gmail_messages", [])

        thread_id = get_next_thread_id(data)
        message_id = get_next_message_id(data)
        ts = get_now_timestamp()

        t = body_html
        t = re.sub(r"</li\s*>", ", ", t, flags=re.IGNORECASE)
        t = re.sub(r"<\s*(br|/p|/ul|/ol)\s*/?>", " ", t, flags=re.IGNORECASE)
        t = re.sub(r"<\s*(p|ul|ol|li)\s*>", " ", t, flags=re.IGNORECASE)
        t = re.sub(r"<[^>]+>", " ", t)
        t = html.unescape(t)
        body_text_stripped = " ".join(t.split())

        new_thread = {
            "thread_id": thread_id,
            "subject": subject,
            "sender_identity": sender_id,
            "recipients": recipients,
            "current_labels": current_labels,
            "created_ts": ts,
            "updated_ts": ts,
        }

        new_message = {
            "message_id": message_id,
            "thread_id": thread_id,
            "sender_email": sender_id,
            "body_html": body_html,
            "body_text_stripped": body_text_stripped,
            "sent_ts": ts,
            "attachments_asset_ids": attachments_asset_ids,
        }

        threads.append(new_thread)
        messages.append(new_message)
        data["gmail_threads"] = threads
        data["gmail_messages"] = messages
        payload = {"thread": new_thread, "message": new_message}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "StartEmailThread",
                "description": "Create a new Gmail thread and its first message; body_text_stripped is derived from body_html.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {"type": "string"},
                        "sender_id": {"type": "string"},
                        "recipients": {"type": "array", "items": {"type": "string"}},
                        "current_labels": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "body_html": {"type": "string"},
                        "attachments_asset_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": [
                        "subject",
                        "sender_id",
                        "recipients",
                        "current_labels",
                        "body_html",
                        "attachments_asset_ids",
                    ],
                },
            },
        }
