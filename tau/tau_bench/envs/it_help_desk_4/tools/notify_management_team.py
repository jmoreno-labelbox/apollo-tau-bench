# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class NotifyManagementTeam(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], recipient_group, report_path, subject) -> str:
        return json.dumps({"status": "notified", "recipient_group": recipient_group, "subject": subject}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "notify_management_team", "description": "Send notification to management team with report.", "parameters": {"type": "object", "properties": {"report_path": {"type": "string"}, "recipient_group": {"type": "string"}, "subject": {"type": "string"}}, "required": ["report_path", "recipient_group", "subject"]}}}
