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

class NotifyStakeholders(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], thread_id: str = None, body_html: str = None, attachments_asset_ids: list[str] = None) -> str:
        required = ["thread_id", "body_html", "attachments_asset_ids"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required.values() if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

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

        sender_id = thread.get("sender_identity")

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
                "name": "NotifyStakeholders",
                "description": "Post a notification email in an existing Gmail thread from the thread's sender_identity with the given HTML body and asset attachments.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"},
                        "body_html": {"type": "string"},
                        "attachments_asset_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["thread_id", "body_html", "attachments_asset_ids"],
                },
            },
        }
