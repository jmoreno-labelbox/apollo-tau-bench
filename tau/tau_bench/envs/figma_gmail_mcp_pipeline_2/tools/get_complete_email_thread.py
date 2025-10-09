from tau_bench.envs.tool import Tool
import html
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetCompleteEmailThread(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], thread_id: str = None) -> str:
        if not thread_id:
            payload = {"error": "Missing required field: thread_id"}
            out = json.dumps(payload, indent=2)
            return out

        threads: list[dict[str, Any]] = data.get("gmail_threads", [])
        messages: list[dict[str, Any]] = data.get("gmail_messages", [])

        thread = None
        for row in threads:
            if row.get("thread_id") == thread_id:
                thread = row
                break
        if not thread:
            payload = {"error": f"No thread with id '{thread_id}'"}
            out = json.dumps(payload, indent=2)
            return out

        msgs = [m for m in messages if m.get("thread_id") == thread_id]
        msgs.sort(key=lambda r: (str(r.get("sent_ts")), str(r.get("message_id"))))
        payload = {"thread": thread, "messages": msgs, "count": len(msgs)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCompleteEmailThread",
                "description": "Return a Gmail thread and all messages within it.",
                "parameters": {
                    "type": "object",
                    "properties": {"thread_id": {"type": "string"}},
                    "required": ["thread_id"],
                },
            },
        }
