# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ModifyEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        updates = kwargs.get("updates") or {}
        message_id = kwargs.get("message_id")
        emails = data.get("emails", [])
        for e in emails:
            if e.get("message_id") == message_id:
                e.update(updates)
                e["updated_at"] = _fixed_now_iso()
        return json.dumps({"updated_message_id": message_id, "updates": updates}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_email",
            "description":"Update an email record.",
            "parameters":{"type":"object","properties":{"message_id":{"type":"string"},"updates":{"type":"object"}},"required":["message_id","updates"]}
        }}
