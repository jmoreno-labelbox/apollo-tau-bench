# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SchedulePropertyShowing(Tool):
    """Schedule a private property showing for a client."""
    
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        property_id = kwargs.get('property_id')
        client_id = kwargs.get('client_id')
        broker_id = kwargs.get('broker_id')
        scheduled_time = kwargs.get('scheduled_time')
        duration_minutes = kwargs.get('duration_minutes', 60)
        
        if not all([property_id, client_id, broker_id, scheduled_time]):
            return json.dumps({
                "error": "property_id, client_id, broker_id, and scheduled_time are required"
            }, indent=2)
        
        # Create showing appointment
        showing = {
            "showing_id": 901,
            "property_id": property_id,
            "client_id": client_id,
            "broker_id": broker_id,
            "scheduled_time": scheduled_time,
            "duration_minutes": duration_minutes,
            "status": "scheduled",
            "created_at": "2024-08-21T00:00:00Z"
        }
        
        return json.dumps({
            "success": True,
            "showing_id": 901,
            "message": f"Showing scheduled for property {property_id}",
            "showing": showing
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "schedule_property_showing",
                "description": "Schedule a private property showing for a client",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_id": {
                            "type": "string",
                            "description": "Property ID to show"
                        },
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID for the showing"
                        },
                        "broker_id": {
                            "type": "integer",
                            "description": "Broker ID conducting the showing"
                        },
                        "scheduled_time": {
                            "type": "string",
                            "description": "Scheduled time in ISO format"
                        },
                        "duration_minutes": {
                            "type": "integer",
                            "description": "Duration of showing in minutes"
                        }
                    },
                    "required": ["property_id", "client_id", "broker_id", "scheduled_time"]
                }
            }
        }
