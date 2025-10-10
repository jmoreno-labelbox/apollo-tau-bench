# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ComposeReleaseEmailDraftTool(Tool):
    """Compose a release email draft message in gmail_messages (deterministic message_id)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        release_id = _require_str(kwargs.get("release_id"), "release_id")
        thread_id = _require_str(kwargs.get("thread_id"), "thread_id")  # existing or new thread id
        from_email = _require_str(kwargs.get("from_email"), "from_email")
        created_ts = _require_str(kwargs.get("created_ts"), "created_ts")
        subject = _require_str(kwargs.get("subject"), "subject")
        body = _require_str(kwargs.get("body"), "body")
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
