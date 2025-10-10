# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCompleteEmailThread(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if not kwargs.get("thread_id"):
            return json.dumps({"error": "Missing required field: thread_id"}, indent=2)

        thread_id = kwargs.get("thread_id")
        threads: List[Dict[str, Any]] = list(data.get("gmail_threads", {}).values())
        messages: List[Dict[str, Any]] = list(data.get("gmail_messages", {}).values())

        thread = None
        for row in threads:
            if row.get("thread_id") == thread_id:
                thread = row
                break
        if not thread:
            return json.dumps({"error": f"No thread with id '{thread_id}'"}, indent=2)

        msgs = [m for m in messages if m.get("thread_id") == thread_id]
        msgs.sort(key=lambda r: (str(r.get("sent_ts")), str(r.get("message_id"))))
        return json.dumps({"thread": thread, "messages": msgs, "count": len(msgs)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_complete_email_thread",
                "description": "Return a Gmail thread and all messages within it.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"}
                    },
                    "required": ["thread_id"]
                }
            }
        }
