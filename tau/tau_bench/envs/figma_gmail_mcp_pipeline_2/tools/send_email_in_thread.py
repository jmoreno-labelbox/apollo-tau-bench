from tau_bench.envs.tool import Tool
import html
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SendEmailInThread(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        thread_id: str = None,
        sender_id: str = None,
        body_html: str = None,
        attachments_asset_ids: list[str] | None = None
    ) -> str:
        pass
        required = ["thread_id", "sender_id", "body_html"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required.values() if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        attachments_asset_ids = attachments_asset_ids or []

        threads: list[dict[str, Any]] = data.get("gmail_threads", {}).values()
        messages: list[dict[str, Any]] = data.get("gmail_messages", {}).values()

        thread = None
        for row in threads:
            if row.get("thread_id") == thread_id:
                thread = row
                break
        if not thread:
            payload = {"error": f"No thread with id '{thread_id}'"}
            out = json.dumps(payload, indent=2)
            return out

        allowed = (sender_id == thread.get("sender_identity")) or (
            sender_id in (thread.get("recipients") or [])
        )
        if not allowed:
            payload = {"error": "SENDER_NOT_AUTHORIZED"}
            out = json.dumps(payload, indent=2)
            return out

        t = body_html
        t = re.sub(r"</li\s*>", ", ", t, flags=re.IGNORECASE)
        t = re.sub(r"<\s*(br|/p|/ul|/ol)\s*/?>", " ", t, flags=re.IGNORECASE)
        t = re.sub(r"<\s*(p|ul|ol|li)\s*>", " ", t, flags=re.IGNORECASE)
        t = re.sub(r"<[^>]+>", " ", t)
        t = html.unescape(t)
        body_text_stripped = " ".join(t.split())

        message_id = get_next_message_id(data)
        ts = get_now_timestamp()

        new_message = {
            "message_id": message_id,
            "thread_id": thread_id,
            "sender_email": sender_id,
            "body_html": body_html,
            "body_text_stripped": body_text_stripped,
            "sent_ts": ts,
            "attachments_asset_ids": attachments_asset_ids,
        }

        messages.append(new_message)
        thread["updated_ts"] = ts
        data["gmail_messages"] = messages
        data["gmail_threads"] = threads
        payload = {"thread": thread, "message": new_message}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendEmailInThread",
                "description": "Send a message in an existing Gmail thread. Sender must match thread sender_identity or be in recipients. HTML body is converted to stripped text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"},
                        "sender_id": {"type": "string"},
                        "body_html": {"type": "string"},
                        "attachments_asset_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["thread_id", "sender_id", "body_html"],
                },
            },
        }
