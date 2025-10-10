# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _fixed_now_iso


class DispatchResultsEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], attachment, batch_name, body_text, model_name, subject, to_address) -> str:
        inbox = data.get("gmail_messages", [])
        max_id = 0
        for m in inbox:
            try:
                mid = int(m.get("message_id", 0))
                if mid > max_id: max_id = mid
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
            "sent_at": _fixed_now_iso()
        }
        inbox.append(row)
        return json.dumps({"status":"sent","message_id": new_id, "to": row["to"]}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"send_results_email",
            "description":"Send a results email with an attachment (deterministic parameters only).",
            "parameters":{"type":"object","properties":{
                "to_address":{"type":"string"},
                "subject":{"type":"string"},
                "body_text":{"type":"string"},
                "attachment":{"type":"string"},
                "model_name":{"type":"string"},
                "batch_name":{"type":"string"}
            },"required":["to_address","subject","body_text","attachment"]}
        }}
