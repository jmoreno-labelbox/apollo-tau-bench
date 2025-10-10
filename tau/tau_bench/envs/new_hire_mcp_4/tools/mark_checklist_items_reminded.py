# Copyright by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MarkChecklistItemsReminded(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], item_ids, reminder_email_message_id, updated_ts) -> str:
        item_ids: List[str] = item_ids
        msg_id: Optional[str] = reminder_email_message_id
        updated_ts = _fixed_ts(updated_ts)

        updated = 0
        for it in list(data.get("checklist_items", {}).values()):
            if it.get("item_id") in item_ids:
                it["status"] = "Reminder Sent"
                it["reminder_sent_flag"] = True
                it["reminder_email_message_id_nullable"] = msg_id
                it["updated_ts"] = updated_ts
                updated += 1
        return json.dumps({"updated": updated, "message_id": msg_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "mark_checklist_items_reminded",
                "description": "Mark checklist items as reminded, link the reminder email id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_ids": {"type": "array", "items": {"type": "string"}},
                        "reminder_email_message_id": {"type": "string"},
                        "updated_ts": {"type": "string"}
                    },
                    "required": ["item_ids"]
                }
            }
        }
