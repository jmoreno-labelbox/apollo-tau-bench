from tau_bench.envs.tool import Tool
import json
from typing import Any

class append_gmail_message(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        thread_id: str,
        sender_email: str,
        recipients: list[str],
        body_html: str,
        attachments_asset_ids: list[str],
        timestamp: str,
        request_id: str,
    ) -> str:
        threads = _table(data, "gmail_threads")
        if not any(
            isinstance(t, dict) and t.get("thread_id") == thread_id for t in threads
        ):
            payload = {"error": f"thread_id '{thread_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        assets = _table(data, "assets")
        for aid in attachments_asset_ids or []:
            if not any(
                isinstance(a, dict) and a.get("asset_id") == aid for a in assets
            ):
                payload = {"error": f"attachment asset_id '{aid}' not found"}
                out = json.dumps(
                    payload, indent=2
                )
                return out

        msgs = _table(data, "gmail_messages")
        msg_id = _id_from_request("msg", request_id)
        if msg_id:
            for m in msgs:
                if isinstance(m, dict) and m.get("message_id") == msg_id:
                    payload = m
                    out = json.dumps(payload, indent=2)
                    return out

        row = {
            "message_id": msg_id
            or _get_next_id(
                "msg", [m.get("message_id", "") for m in msgs if isinstance(m, dict)]
            ),
            "thread_id": thread_id,
            "sender_email": sender_email,
            "recipients": _norm_list(recipients),
            "body_html": body_html,
            "attachments": list(attachments_asset_ids or []),
            "day": _ymd(timestamp),
        }
        msgs.append(row)
        payload = row
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AppendGmailMessage",
                "description": "Append/reuse a deterministic Gmail message (msg_<request_id>).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"},
                        "sender_email": {"type": "string"},
                        "recipients": {"type": "array", "items": {"type": "string"}},
                        "body_html": {"type": "string"},
                        "attachments_asset_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": [
                        "thread_id",
                        "sender_email",
                        "recipients",
                        "body_html",
                        "attachments_asset_ids",
                        "timestamp",
                        "request_id",
                    ],
                },
            },
        }
