from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class AppendMessageToThreadTool(Tool):
    """Add (or upsert) a message to a thread. Deterministic message_id derived from inputs. No sending action."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        body: str = None,
        created_ts: str = None,
        from_email: str = None,
        thread_id: str = None
    ) -> str:
        thread_id = _require_str(thread_id, "thread_id")
        from_email = _require_str(from_email, "from_email")
        body = _require_str(body, "body")
        created_ts = _require_str(created_ts, "created_ts")
        snippet = (body[:120] + "...") if len(body) > 123 else body
        if not all([thread_id, from_email, body, created_ts]):
            payload = {"error": "thread_id, from_email, body, created_ts required"}
            out = json.dumps(payload)
            return out

        message_id = _det_id("msg", [thread_id, from_email, created_ts, body[:64]])
        messages = _safe_table(data, "gmail_messages")
        idx = _index_by(messages, "message_id")
        row = {
            "message_id": message_id,
            "thread_id": thread_id,
            "from_email": from_email,
            "created_ts": created_ts,
            "body": body,
            "snippet": snippet,
        }
        if message_id in idx:
            messages[idx[message_id]] = row
        else:
            messages.append(row)

        threads = _safe_table(data, "gmail_threads")
        t_idx = _index_by(threads, "thread_id")
        if thread_id in t_idx:
            threads[t_idx[thread_id]]["updated_ts"] = created_ts
        payload = {"success": True, "message_id": message_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AppendMessageToThread",
                "description": "Append/upsert a message in a thread (deterministic id). Stores snippet; does not send email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"},
                        "from_email": {"type": "string"},
                        "body": {"type": "string"},
                        "created_ts": {"type": "string"},
                    },
                    "required": ["thread_id", "from_email", "body", "created_ts"],
                },
            },
        }
