# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendEmailInThread(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], attachments_asset_ids, body_html, sender_id, thread_id) -> str:
        required = ["thread_id", "sender_id", "body_html"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)
        attachments_asset_ids: Optional[List[str]] = attachments_asset_ids or []

        threads: List[Dict[str, Any]] = list(data.get("gmail_threads", {}).values())
        messages: List[Dict[str, Any]] = list(data.get("gmail_messages", {}).values())

        thread = None
        for row in threads:
            if row.get("thread_id") == thread_id:
                thread = row
                break
        if not thread:
            return json.dumps({"error": f"No thread with id '{thread_id}'"}, indent=2)

        allowed = (sender_id == thread.get("sender_identity")) or (sender_id in (thread.get("recipients") or []))
        if not allowed:
            return json.dumps({"error": "SENDER_NOT_AUTHORIZED"}, indent=2)

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
            "attachments_asset_ids": attachments_asset_ids
        }

        messages.append(new_message)
        thread["updated_ts"] = ts
        data["gmail_messages"] = messages
        data["gmail_threads"] = threads

        return json.dumps({"thread": thread, "message": new_message}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "send_email_in_thread",
                "description": "Send a message in an existing Gmail thread. Sender must match thread sender_identity or be in recipients. HTML body is converted to stripped text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"},
                        "sender_id": {"type": "string"},
                        "body_html": {"type": "string"},
                        "attachments_asset_ids": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["thread_id", "sender_id", "body_html"]
                }
            }
        }
