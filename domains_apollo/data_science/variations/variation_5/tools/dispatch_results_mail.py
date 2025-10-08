from tau_bench.envs.tool import Tool
import json
from typing import Any

class DispatchResultsMail(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        to_address: str = None,
        subject: str = None,
        body_text: str = None,
        attachment: str = None,
        model_name: str = None,
        batch_name: str = None
    ) -> str:
        inbox = data.get("gmail_messages", [])
        max_id = 0
        for m in inbox:
            try:
                mid = int(m.get("message_id", 0))
                if mid > max_id:
                    max_id = mid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "message_id": new_id,
            "to": to_address,
            "subject": subject,
            "body_text": body_text,
            "attachment": attachment,
            "model_name": model_name,
            "batch_name": batch_name,
            "sent_at": _now_iso_fixed(),
        }
        inbox.append(row)
        payload = {"status": "sent", "message_id": new_id, "to": row["to"]}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DispatchResultsMail",
                "description": "Send a results email with a single attachment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "to_address": {"type": "string"},
                        "subject": {"type": "string"},
                        "body_text": {"type": "string"},
                        "attachment": {"type": "string"},
                        "model_name": {"type": "string"},
                        "batch_name": {"type": "string"},
                    },
                    "required": ["to_address", "subject", "body_text", "attachment"],
                },
            },
        }
