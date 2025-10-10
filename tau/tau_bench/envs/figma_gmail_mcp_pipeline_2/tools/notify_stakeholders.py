# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class NotifyStakeholders(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["thread_id", "body_html", "attachments_asset_ids"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        thread_id = kwargs.get("thread_id")
        body_html = kwargs.get("body_html")
        attachments_asset_ids: List[str] = kwargs.get("attachments_asset_ids")

        threads: List[Dict[str, Any]] = list(data.get("gmail_threads", {}).values())
        messages: List[Dict[str, Any]] = list(data.get("gmail_messages", {}).values())

        thread = None
        for row in threads:
            if row.get("thread_id") == thread_id:
                thread = row
                break
        if not thread:
            return json.dumps({"error": f"No thread with id '{thread_id}'"}, indent=2)

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
                "name": "notify_stakeholders",
                "description": "Post a notification email in an existing Gmail thread from the thread's sender_identity with the given HTML body and asset attachments.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"},
                        "body_html": {"type": "string"},
                        "attachments_asset_ids": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["thread_id", "body_html", "attachments_asset_ids"]
                }
            }
        }
