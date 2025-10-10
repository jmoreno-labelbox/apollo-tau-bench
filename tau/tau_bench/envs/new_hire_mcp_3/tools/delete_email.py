# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        message_id = kwargs.get("message_id")
        emails = list(data.get("emails", {}).values())
        data["emails"] = [e for e in emails if e.get("message_id") != message_id]
        return json.dumps({"deleted_message_id": message_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"delete_email",
            "description":"Delete an email by message ID.",
            "parameters":{"type":"object","properties":{"message_id":{"type":"string"}},"required":["message_id"]}
        }}
