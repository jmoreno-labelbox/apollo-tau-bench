# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendPassengerNotification(Tool):
    """
    A tool to send a notification to a passenger for a specific reservation.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], reservation_id: str, message: str) -> str:
        operational_events = data.get("operational_events", [])
        message = {
            "event_type": "PASSENGER_NOTIFICATION",
            "status": "Notification Sent",
            "reservation_id": reservation_id,
            "message": (f"PASSENGER NOTIFICATION for reservation {reservation_id}: {message}")
        }
        operational_events.append(message)
        return json.dumps(message)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "send_passenger_notification",
                "description": "Sends a notification to the passenger of a specific reservation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "The unique ID of the reservation."
                        },
                        "message": {
                            "type": "string",
                            "description": "The content of the notification message."
                        }
                    },
                    "required": ["reservation_id", "message"]
                }
            }
        }
