from tau_bench.envs.tool import Tool
import json
from typing import Any

class GmailDraftEmail(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        attachments_paths: list[str] = [],
        body_preview_nullable: str = None,
        created_ts: str = None,
        draft_id: str = None,
        recipients: list[str] = None,
        subject: str = None
    ) -> str:
        req = ["draft_id", "subject", "recipients"]
        err = _require({"draft_id": draft_id, "subject": subject, "recipients": recipients}, req)
        if err:
            return err
        row = {
            "draft_id_nullable": draft_id,
            "message_id_nullable": None,
            "subject": subject,
            "recipients": recipients,
            "body_preview_nullable": body_preview_nullable,
            "attachments_paths": attachments_paths,
            "status": "drafted",
            "created_ts": created_ts,
            "sent_ts_nullable": None,
        }
        payload = _append(data.setdefault("gmail_messages", []), row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GmailDraftEmail",
                "description": "Creates a drafted Gmail message entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "draft_id": {"type": "string"},
                        "subject": {"type": "string"},
                        "recipients": {"type": "array", "items": {"type": "string"}},
                        "body_preview_nullable": {"type": "string"},
                        "attachments_paths": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "created_ts": {"type": "string"},
                    },
                    "required": ["draft_id", "subject", "recipients"],
                },
            },
        }
