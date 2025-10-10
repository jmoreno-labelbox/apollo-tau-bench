# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendNewHireWelcomeEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        upn = kwargs.get("upn")
        personal_email = kwargs.get("personal_email")
        pickup_code = kwargs.get("pickup_code")
        return json.dumps({"status": "sent", "recipients": [upn, personal_email], "pickup_code": pickup_code}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "send_new_hire_welcome_email", "description": "Sends a welcome email to the new hire's company and personal addresses with device pickup information.", "parameters": {"type": "object", "properties": {"upn": {"type": "string"}, "personal_email": {"type": "string"}, "pickup_code": {"type": "string"}}, "required": ["upn", "personal_email", "pickup_code"]}}}
