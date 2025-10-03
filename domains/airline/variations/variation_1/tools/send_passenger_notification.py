from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any

class SendPassengerNotification(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], reservation_id: str, message: str) -> str:
        payload = {
            "status": "Notification Sent",
            "reservation_id": reservation_id,
            "message": (
                f"PASSENGER NOTIFICATION for reservation {reservation_id}: {message}"
            ),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendPassengerNotification",
                "description": "Sends a notification to the passenger of a specific reservation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "The unique ID of the reservation.",
                        },
                        "message": {
                            "type": "string",
                            "description": "The content of the notification message.",
                        },
                    },
                    "required": ["reservation_id", "message"],
                },
            },
        }
