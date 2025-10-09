from tau_bench.envs.tool import Tool
import json
from typing import Any

class GmailSendEmail(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        draft_id: str = None,
        message_id: str = None,
        sent_ts: str = "1970-01-01T00:00:00Z"
    ) -> str:
        req = ["draft_id"]
        err = _require({"draft_id": draft_id}, req)
        if err:
            return err
        msg = next(
            (
                m
                for m in data.setdefault("gmail_messages", [])
                if m.get("draft_id_nullable") == draft_id
            ),
            None,
        )
        if not msg:
            payload = {"error": f"draft_id '{draft_id}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        msg["message_id_nullable"] = message_id if message_id is not None else msg.get("message_id_nullable")
        msg["status"] = "sent"
        msg["sent_ts_nullable"] = sent_ts if sent_ts is not None else msg.get("sent_ts_nullable", "1970-01-01T00:00:00Z")
        payload = msg
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GmailSendEmail",
                "description": "Marks a drafted Gmail message as sent.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "draft_id": {"type": "string"},
                        "message_id": {"type": "string"},
                        "sent_ts": {"type": "string"},
                    },
                    "required": ["draft_id"],
                },
            },
        }
