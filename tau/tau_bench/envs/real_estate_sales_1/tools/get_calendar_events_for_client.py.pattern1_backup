# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCalendarEventsForClient(Tool):
    """Retrieve calendar events for a specific client."""
    
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = kwargs.get('client_id')
        if not client_id:
            return json.dumps({"error": "client_id is required"}, indent=2)
        
        # Get calendar events for client
        events = data.get('calendar_events', [])
        client_events = [e for e in events if e.get('client_id') == client_id]
        
        return json.dumps({
            "client_id": client_id,
            "event_count": len(client_events),
            "events": client_events
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_calendar_events_for_client",
                "description": "Retrieve calendar events for a specific client",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID to get events for"
                        }
                    },
                    "required": ["client_id"]
                }
            }
        }
