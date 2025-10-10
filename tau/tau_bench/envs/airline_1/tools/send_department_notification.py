# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendDepartmentNotification(Tool):
    """
    A tool to send a notification to an internal administrative department.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], department_name: str, message: str) -> str:
        operational_events = list(data.get("operational_events", {}).values())
        message = {
            "event_type": "DEPARTMENT_NOTIFICATION",
            "status": "Notification Sent",
            "department": department_name,
            "message": (f"INTERNAL NOTIFICATION to {department_name} Department: {message}")
        }
        operational_events.append(message)
        return json.dumps(message)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "send_department_notification",
                "description": "Sends a notification to an internal company department (e.g., Finance, Scheduling).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department_name": {
                            "type": "string",
                            "description": "The name of the target department."
                        },
                        "message": {
                            "type": "string",
                            "description": "The content of the notification message."
                        }
                    },
                    "required": ["department_name", "message"]
                }
            }
        }
