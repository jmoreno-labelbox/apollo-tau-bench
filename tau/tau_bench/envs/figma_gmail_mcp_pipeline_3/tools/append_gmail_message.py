from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class append_gmail_message(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        body_html: str = None,
        recipients: list = None,
        request_id: str = None,
        sender_email: str = None,
        thread_id: str = None,
        timestamp: Any = None,
        attachments_asset_ids: list = None
    ) -> str:
        p = {
            "thread_id": thread_id,
            "sender_email": sender_email,
            "body_html": body_html,
            "request_id": request_id,
            "recipients": recipients or [],
            "timestamp": timestamp
        }
        miss = _require(p, ["thread_id", "sender_email", "body_html", "request_id"])
        if miss:
            return miss
        threads = _ensure(data, "gmail_threads", [])
        for t in threads:
            if t.get("thread_id") == p["thread_id"]:
                msg_id = f"msg_{p['request_id']}"
                msg = {
                    "message_id": msg_id,
                    "sender_email": p["sender_email"],
                    "recipients": p["recipients"],
                    "body_html": p["body_html"],
                    "timestamp": p["timestamp"],
                }
                t.setdefault("gmail_messages", []).append(msg)
                new_parts = set(t.get("participants", []))
                new_parts.add(p["sender_email"])
                for r in p["recipients"]:
                    new_parts.add(r)
                t["participants"] = list(new_parts)
                return _ok({"message_id": msg_id})
        return _err("thread_not_found", {"thread_id": p["thread_id"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AppendGmailMessage",
                "description": "Append a message to an existing Gmail thread.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"},
                        "sender_email": {"type": "string"},
                        "recipients": {"type": "array", "items": {"type": "string"}},
                        "body_html": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": [
                        "thread_id",
                        "sender_email",
                        "body_html",
                        "request_id",
                    ],
                },
            },
        }
