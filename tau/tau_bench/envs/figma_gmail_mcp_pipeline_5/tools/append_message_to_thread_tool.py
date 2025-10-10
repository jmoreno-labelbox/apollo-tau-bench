# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AppendMessageToThreadTool(Tool):
    """Append (or upsert) a message to a thread. Deterministic message_id from inputs. No send operation."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        thread_id = _require_str(kwargs.get("thread_id"), "thread_id")
        from_email = _require_str(kwargs.get("from_email"), "from_email")
        body = _require_str(kwargs.get("body"), "body")
        created_ts = _require_str(kwargs.get("created_ts"), "created_ts")
        snippet = (body[:120] + "...") if len(body) > 123 else body
        if not all([thread_id, from_email, body, created_ts]):
            return json.dumps({"error":"thread_id, from_email, body, created_ts required"})

        message_id = _det_id("msg", [thread_id, from_email, created_ts, body[:64]])
        messages = _safe_table(data, "gmail_messages")
        idx = _index_by(messages, "message_id")
        row = {
            "message_id": message_id,
            "thread_id": thread_id,
            "from_email": from_email,
            "created_ts": created_ts,
            "body": body,
            "snippet": snippet
        }
        if message_id in idx:
            messages[idx[message_id]] = row
        else:
            messages.append(row)

        # Mark thread updated_ts
        threads = _safe_table(data, "gmail_threads")
        t_idx = _index_by(threads, "thread_id")
        if thread_id in t_idx:
            threads[t_idx[thread_id]]["updated_ts"] = created_ts

        return json.dumps({"success": True, "message_id": message_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"append_message_to_thread",
            "description":"Append/upsert a message in a thread (deterministic id). Stores snippet; does not send email.",
            "parameters":{"type":"object","properties":{
                "thread_id":{"type":"string"},
                "from_email":{"type":"string"},
                "body":{"type":"string"},
                "created_ts":{"type":"string"}
            },"required":["thread_id","from_email","body","created_ts"]}
        }}
