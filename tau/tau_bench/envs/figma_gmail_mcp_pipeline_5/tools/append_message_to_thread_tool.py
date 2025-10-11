# Copyright Sierra

import hashlib
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool










def _safe_table(data: Dict[str, Any], table: str) -> List[Dict[str, Any]]:
    """Get or create a list table."""
    return data.setdefault(table, [])

def _require_str(arg: Any, name: str) -> Optional[str]:
    """Return arg as str if valid, else None."""
    return arg if isinstance(arg, str) and arg.strip() else None

def _index_by(table: List[Dict[str, Any]], key: str) -> Dict[str, int]:
    """Build index map from key -> row_index (first occurrence)."""
    idx = {}
    for i, r in enumerate(table):
        k = r.get(key)
        if isinstance(k, str) and k not in idx:
            idx[k] = i
    return idx

def _det_id(prefix: str, parts: List[str], length: int = 8) -> str:
    """
    Deterministic ID from input parts. Stable across runs.
    """
    m = hashlib.md5()
    m.update(("|".join(parts)).encode("utf-8"))
    return f"{prefix}_{m.hexdigest()[:length]}"

class AppendMessageToThreadTool(Tool):
    """Append (or upsert) a message to a thread. Deterministic message_id from inputs. No send operation."""

    @staticmethod
    def invoke(data: Dict[str, Any], body, created_ts, from_email, thread_id) -> str:
        thread_id = _require_str(thread_id, "thread_id")
        from_email = _require_str(from_email, "from_email")
        body = _require_str(body, "body")
        created_ts = _require_str(created_ts, "created_ts")
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

        # Update the timestamp for the thread.
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