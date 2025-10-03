from tau_bench.envs.tool import Tool
import json
from typing import Any

class SchedulePropertyShowing(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], property_id: str = None, client_id: str = None, broker_id: str = None, scheduled_time: str = None, duration_minutes: int = 60) -> str:
        if not all([property_id, client_id, broker_id, scheduled_time]):
            payload = {
                    "error": "property_id, client_id, broker_id, and scheduled_time are required"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        showing = {
            "showing_id": 901,
            "property_id": property_id,
            "client_id": client_id,
            "broker_id": broker_id,
            "scheduled_time": scheduled_time,
            "duration_minutes": duration_minutes,
            "status": "scheduled",
            "created_at": "2024-08-21T00:00:00Z",
        }
        payload = {
                "success": True,
                "showing_id": 901,
                "message": f"Showing scheduled for property {property_id}",
                "showing": showing,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "schedulePropertyShowing",
                "description": "Schedule a private property showing for a client",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_id": {
                            "type": "string",
                            "description": "Property ID to show",
                        },
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID for the showing",
                        },
                        "broker_id": {
                            "type": "integer",
                            "description": "Broker ID conducting the showing",
                        },
                        "scheduled_time": {
                            "type": "string",
                            "description": "Scheduled time in ISO format",
                        },
                        "duration_minutes": {
                            "type": "integer",
                            "description": "Duration of showing in minutes",
                        },
                    },
                    "required": [
                        "property_id",
                        "client_id",
                        "broker_id",
                        "scheduled_time",
                    ],
                },
            },
        }
