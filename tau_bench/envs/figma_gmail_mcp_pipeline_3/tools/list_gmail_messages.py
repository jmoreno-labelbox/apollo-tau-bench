from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class list_gmail_messages(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], thread_id: str = None, request_id: str = None, timestamp: str = None) -> str:
        p = _params(data, {"thread_id": thread_id})
        miss = _require(p, ["thread_id"])
        if miss:
            return miss
        rows = []
        messages = _ensure(data, "gmail_messages", [])
        for m in messages:
            if m.get("thread_id") == p["thread_id"]:
                rows.append(
                    {
                        "message_id": m.get("message_id"),
                        "sender_email": m.get("sender_email"),
                        "recipients": m.get("recipients", []),
                        "body_html": m.get("body_html"),
                        "timestamp": m.get("timestamp"),
                    }
                )
                break
        return _ok({"rows": rows})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListGmailMessages",
                "description": "List messages for a Gmail thread.",
                "parameters": {
                    "type": "object",
                    "properties": {"thread_id": {"type": "string"}},
                },
            },
        }
