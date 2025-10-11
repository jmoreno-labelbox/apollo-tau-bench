# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class NotifyManager(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], body, manager_id, subject) -> str:
        return json.dumps({"status": "sent", "recipient_manager_id": manager_id, "subject": subject}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "notify_manager", "description": "Sends a notification email to a manager for onboarding or offboarding events.", "parameters": {"type": "object", "properties": {"manager_id": {"type": "string"}, "subject": {"type": "string"}, "body": {"type": "string"}}, "required": ["manager_id", "subject", "body"]}}}
