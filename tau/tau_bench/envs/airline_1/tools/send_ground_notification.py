# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendGroundNotification(Tool):
    """
    A tool to send a notification to ground staff at a specific airport.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], airport_id: str, message: str, priority: str = "NORMAL") -> str:
        operational_events = data.get("operational_events", [])
        message = {
            "event_type": "GROUND_NOTIFICATION",
            "status": "Notification Sent",
            "airport_id": airport_id,
            "priority": priority,
            "message": (f"NOTIFICATION SENT to {airport_id} with priority {priority}: {message}")
        }
        operational_events.append(message)
        return json.dumps(message)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "send_ground_notification",
                "description": "Sends an operational notification to the ground crew/Station Manager at a specified airport.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "airport_id": {
                            "type": "string",
                            "description": "The unique ID of the airport where the notification should be sent."
                        },
                        "message": {
                            "type": "string",
                            "description": "The content of the notification message."
                        },
                        "priority": {
                            "type": "string",
                            "description": "The priority of the message (e.g., 'HIGH', 'NORMAL')."
                        }
                    },
                    "required": ["airport_id", "message", "priority"]
                }
            }
        }
