# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DispatchResultsMail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
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
            "to": kwargs.get("to_address"),
            "subject": kwargs.get("subject"),
            "body_text": kwargs.get("body_text"),
            "attachment": kwargs.get("attachment"),
            "model_name": kwargs.get("model_name"),
            "batch_name": kwargs.get("batch_name"),
            "sent_at": _now_iso_fixed(),
        }
        inbox.append(row)
        return json.dumps({"status": "sent", "message_id": new_id, "to": row["to"]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "dispatch_results_mail",
            "description": "Send a results email with a single attachment.",
            "parameters": {"type": "object", "properties": {
                "to_address": {"type": "string"},
                "subject": {"type": "string"},
                "body_text": {"type": "string"},
                "attachment": {"type": "string"},
                "model_name": {"type": "string"},
                "batch_name": {"type": "string"}
            }, "required": ["to_address", "subject", "body_text", "attachment"]}
        }}
