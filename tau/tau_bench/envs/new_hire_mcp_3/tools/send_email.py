# Copyright Sierra Technologies

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        new_email = kwargs.get("email") or {}
        emails = list(data.get("emails", {}).values())
        emails.append(new_email)
        data["emails"] = emails
        return json.dumps({"sent_email": new_email}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"send_email",
            "description":"Send a new email and add it to the record.",
            "parameters":{"type":"object","properties":{"email":{"type":"object"}},"required":["email"]}
        }}
