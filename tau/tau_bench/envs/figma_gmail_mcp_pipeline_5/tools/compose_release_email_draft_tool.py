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

class ComposeReleaseEmailDraftTool(Tool):
    """Compose a release email draft message in gmail_messages (deterministic message_id)."""

    @staticmethod
    def invoke(data: Dict[str, Any], body, created_ts, from_email, release_id, subject, thread_id) -> str:
        release_id = _require_str(release_id, "release_id")
        thread_id = _require_str(thread_id, "thread_id")  # identifier for an existing or new thread
        from_email = _require_str(from_email, "from_email")
        created_ts = _require_str(created_ts, "created_ts")
        subject = _require_str(subject, "subject")
        body = _require_str(body, "body")
        if not all([release_id, thread_id, from_email, created_ts, subject, body]):
            return json.dumps({"error":"release_id, thread_id, from_email, created_ts, subject, body required"})

        message_id = _det_id("relmsg", [release_id, thread_id, created_ts, subject[:32]])
        messages = _safe_table(data, "gmail_messages")
        idx = _index_by(messages, "message_id")
        row = {
            "message_id": message_id,
            "thread_id": thread_id,
            "from_email": from_email,
            "created_ts": created_ts,
            "subject": subject,
            "body": body,
            "snippet": (body[:120] + "...") if len(body) > 123 else body
        }
        if message_id in idx:
            messages[idx[message_id]] = row
        else:
            messages.append(row)

        return json.dumps({"success": True, "message_id": message_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"compose_release_email_draft",
            "description":"Create/update a release email draft message (deterministic id) in an existing thread.",
            "parameters":{"type":"object","properties":{
                "release_id":{"type":"string"},
                "thread_id":{"type":"string"},
                "from_email":{"type":"string"},
                "created_ts":{"type":"string"},
                "subject":{"type":"string"},
                "body":{"type":"string"}
            },"required":["release_id","thread_id","from_email","created_ts","subject","body"]}
        }}