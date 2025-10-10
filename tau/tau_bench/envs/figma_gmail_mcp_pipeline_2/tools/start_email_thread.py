# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class StartEmailThread(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], attachments_asset_ids, body_html, current_labels, recipients, sender_id, subject) -> str:
        required = ["subject", "sender_id", "recipients", "current_labels", "body_html", "attachments_asset_ids"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        threads: List[Dict[str, Any]] = list(data.get("gmail_threads", {}).values())
        messages: List[Dict[str, Any]] = list(data.get("gmail_messages", {}).values())

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
            "updated_ts": ts
        }

        new_message = {
            "message_id": message_id,
            "thread_id": thread_id,
            "sender_email": sender_id,
            "body_html": body_html,
            "body_text_stripped": body_text_stripped,
            "sent_ts": ts,
            "attachments_asset_ids": attachments_asset_ids
        }

        threads.append(new_thread)
        messages.append(new_message)
        data["gmail_threads"] = threads
        data["gmail_messages"] = messages

        return json.dumps({"thread": new_thread, "message": new_message}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "start_email_thread",
                "description": "Create a new Gmail thread and its first message; body_text_stripped is derived from body_html.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {"type": "string"},
                        "sender_id": {"type": "string"},
                        "recipients": {"type": "array", "items": {"type": "string"}},
                        "current_labels": {"type": "array", "items": {"type": "string"}},
                        "body_html": {"type": "string"},
                        "attachments_asset_ids": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["subject", "sender_id", "recipients", "current_labels", "body_html", "attachments_asset_ids"]
                }
            }
        }
