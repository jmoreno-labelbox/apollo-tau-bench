from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any

class MarkChecklistItemsReminded(Tool):
    """Update status to 'Reminder Sent', set reminder_sent_flag to true, set reminder_email_message_id_nullable, and update the timestamp."""

    @staticmethod
    def invoke(data: dict[str, Any], item_ids: list[str], reminder_email_message_id: str | None = None, updated_ts: Any = None, due_date_lte: Any = None, candidate_id: str = None, status: str = None, subject: str = None) -> str:
        updated_ts = _fixed_ts(updated_ts)

        updated = 0
        for it in data.get("checklist_items", []):
            if it.get("item_id") in item_ids:
                it["status"] = "Reminder Sent"
                it["reminder_sent_flag"] = True
                it["reminder_email_message_id_nullable"] = reminder_email_message_id
                it["updated_ts"] = updated_ts
                updated += 1
        payload = {"updated": updated, "message_id": reminder_email_message_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MarkChecklistItemsReminded",
                "description": "Mark checklist items as reminded, link the reminder email id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_ids": {"type": "array", "items": {"type": "string"}},
                        "reminder_email_message_id": {"type": "string"},
                        "updated_ts": {"type": "string"},
                    },
                    "required": ["item_ids"],
                },
            },
        }
