from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any

class SendDepartmentNotification(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], department_name: str, message: str) -> str:
        payload = {
            "status": "Notification Sent",
            "department": department_name,
            "message": (
                f"INTERNAL NOTIFICATION to {department_name} Department: {message}"
            ),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendDepartmentNotification",
                "description": "Sends a notification to an internal company department (e.g., Finance, Scheduling).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department_name": {
                            "type": "string",
                            "description": "The name of the target department.",
                        },
                        "message": {
                            "type": "string",
                            "description": "The content of the notification message.",
                        },
                    },
                    "required": ["department_name", "message"],
                },
            },
        }
