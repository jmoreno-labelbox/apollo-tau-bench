from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class create_gmail_thread(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subject: str = None, sender_email: str = None, recipients: list = None, request_id: str = None, timestamp: str = None, initial_labels: list = None) -> str:
        p = _params(data, {
            "subject": subject,
            "sender_email": sender_email,
            "recipients": recipients,
            "request_id": request_id
        })
        miss = _require(p, ["subject", "sender_email", "recipients", "request_id"])
        if miss:
            return miss
        threads = _ensure(data, "gmail_threads", [])
        thread_id = f"thr_{p['request_id']}"
        thread = {
            "thread_id": thread_id,
            "subject": p.get("subject", ""),
            "participants": list({p["sender_email"], *p.get("recipients", [])}),
            "labels": [],
            "messages": [],
        }
        threads.append(thread)
        return _ok({"thread_id": thread_id})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateGmailThread",
                "description": "Create a new Gmail thread.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {"type": "string"},
                        "sender_email": {"type": "string"},
                        "recipients": {"type": "array", "items": {"type": "string"}},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["subject", "sender_email", "recipients", "request_id"],
                },
            },
        }
