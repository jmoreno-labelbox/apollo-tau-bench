# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class notify_hr(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], message: str) -> str:
        notification = {
            "message": message,
            "timestamp": "2025-07-04",
            "type": "HR_NOTIFICATION",
        }
        data.setdefault("hr_notifications", []).append(notification)
        return json.dumps({"success": "HR notified", "message": message}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "notify_hr",
                "description": "Send a notification to HR",
                "parameters": {
                    "type": "object",
                    "properties": {"message": {"type": "string"}},
                    "required": ["message"],
                },
            },
        }
