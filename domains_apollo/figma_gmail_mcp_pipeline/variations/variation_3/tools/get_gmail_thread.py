from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class get_gmail_thread(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], thread_id: str = None, request_id: str = None, timestamp: str = None) -> str:
        p = _params(data, {"thread_id": thread_id})
        miss = _require(p, ["thread_id"])
        if miss:
            return miss
        threads = _ensure(data, "gmail_threads", [])
        for t in threads:
            if t.get("thread_id") == p["thread_id"]:
                return _ok(
                    {"thread_id": t["thread_id"], "current_labels": t.get("labels", [])}
                )
        return _ok({"thread_id": p["thread_id"], "current_labels": []})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetGmailThread",
                "description": "Fetch a Gmail thread metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {"thread_id": {"type": "string"}},
                    "required": ["thread_id"],
                },
            },
        }
