# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateCalendarEvent(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        broker_id = kwargs.get('broker_id')
        client_id = kwargs.get('client_id')
        title = kwargs.get('title')
        start_at = kwargs.get('start_at')
        end_at = kwargs.get('end_at')
        location = kwargs.get('location')
        notes = kwargs.get('notes')
        source = kwargs.get('source')
        
        if not all([broker_id, client_id, title, start_at, end_at]):
            return json.dumps({
                "error": "broker_id, client_id, title, start_at, and end_at are required"
            }, indent=2)
        
        import time
        timestamp = str(int(time.time() * 1000))
        event_id = f"EVENT-{client_id}-{timestamp}"
        event = {
            "event_id": event_id,
            "broker_id": broker_id,
            "client_id": client_id,
            "title": title,
            "start_at": start_at,
            "end_at": end_at,
            "location": location,
            "notes": notes,
            "source": source,
            "status": "scheduled",
            "created_at": "2024-08-21T00:00:00Z"
        }
        
        return json.dumps({
            "success": True,
            "event_id": event_id,
            "message": f"Calendar event created for client {client_id}",
            "event": event
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_calendar_event",
                "description": "Create a calendar event for client meetings or appointments",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "broker_id": {
                            "type": "integer",
                            "description": "Broker ID creating the event"
                        },
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID for the event"
                        },
                        "title": {
                            "type": "string",
                            "description": "Event title"
                        },
                        "start_at": {
                            "type": "string",
                            "description": "Start time in ISO format"
                        },
                        "end_at": {
                            "type": "string",
                            "description": "End time in ISO format"
                        },
                        "location": {
                            "type": "string",
                            "description": "Event location"
                        },
                        "notes": {
                            "type": "string",
                            "description": "Event notes"
                        },
                        "source": {
                            "type": "string",
                            "description": "Event source (client_meeting, follow_up, viewing, etc.)"
                        }
                    },
                    "required": ["broker_id", "client_id", "title", "start_at", "end_at"]
                }
            }
        }
