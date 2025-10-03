from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class ComposeReleaseEmailDraftTool(Tool):
    """Draft a release email message in gmail_messages (deterministic message_id)."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        body: str = None,
        created_ts: str = None,
        from_email: str = None,
        release_id: str = None,
        subject: str = None,
        thread_id: str = None
    ) -> str:
        release_id = _require_str(release_id, "release_id")
        thread_id = _require_str(thread_id, "thread_id")
        from_email = _require_str(from_email, "from_email")
        created_ts = _require_str(created_ts, "created_ts")
        subject = _require_str(subject, "subject")
        body = _require_str(body, "body")
        if not all([release_id, thread_id, from_email, created_ts, subject, body]):
            payload = {
                "error": "release_id, thread_id, from_email, created_ts, subject, body required"
            }
            out = json.dumps(payload)
            return out

        message_id = _det_id(
            "relmsg", [release_id, thread_id, created_ts, subject[:32]]
        )
        messages = _safe_table(data, "gmail_messages")
        idx = _index_by(messages, "message_id")
        row = {
            "message_id": message_id,
            "thread_id": thread_id,
            "from_email": from_email,
            "created_ts": created_ts,
            "subject": subject,
            "body": body,
            "snippet": (body[:120] + "...") if len(body) > 123 else body,
        }
        if message_id in idx:
            messages[idx[message_id]] = row
        else:
            messages.append(row)
        payload = {"success": True, "message_id": message_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComposeReleaseEmailDraft",
                "description": "Create/update a release email draft message (deterministic id) in an existing thread.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {"type": "string"},
                        "thread_id": {"type": "string"},
                        "from_email": {"type": "string"},
                        "created_ts": {"type": "string"},
                        "subject": {"type": "string"},
                        "body": {"type": "string"},
                    },
                    "required": [
                        "release_id",
                        "thread_id",
                        "from_email",
                        "created_ts",
                        "subject",
                        "body",
                    ],
                },
            },
        }
