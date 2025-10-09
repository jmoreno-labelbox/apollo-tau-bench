from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetThreadMessagesTool(Tool):
    """Provide basic message information (sender, timestamp, snippet) for a thread."""

    @staticmethod
    def invoke(data: dict[str, Any], thread_id: str = None) -> str:
        thread_id = _require_str(thread_id, "thread_id")
        if not thread_id:
            payload = {"error": "thread_id is required"}
            out = json.dumps(payload)
            return out

        msgs = data.get("gmail_messages", [])
        out = []
        for m in msgs:
            if m.get("thread_id") == thread_id:
                out.append(
                    _small_fields(
                        m, ["message_id", "from_email", "created_ts", "snippet"]
                    )
                )
        out.sort(key=lambda r: r.get("created_ts", ""))
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetThreadMessages",
                "description": "List messages for a thread (sender, ts, snippet only).",
                "parameters": {
                    "type": "object",
                    "properties": {"thread_id": {"type": "string"}},
                    "required": ["thread_id"],
                },
            },
        }
