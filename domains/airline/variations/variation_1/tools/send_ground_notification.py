from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any

class SendGroundNotification(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any], airport_id: str, message: str, priority: str = "NORMAL"
    ) -> str:
        payload = {
            "status": "Notification Sent",
            "airport_id": airport_id,
            "priority": priority,
            "message": (
                f"NOTIFICATION SENT to {airport_id} with priority {priority}: {message}"
            ),
        }
        out = json.dumps(payload)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendGroundNotification",
                "description": "Sends an operational notification to the ground crew at a specified airport.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "airport_id": {
                            "type": "string",
                            "description": "The unique ID of the airport where the notification should be sent.",
                        },
                        "message": {
                            "type": "string",
                            "description": "The content of the notification message.",
                        },
                        "priority": {
                            "type": "string",
                            "description": "The priority of the message (e.g., 'HIGH', 'NORMAL').",
                        },
                    },
                    "required": ["airport_id", "message", "priority"],
                },
            },
        }
