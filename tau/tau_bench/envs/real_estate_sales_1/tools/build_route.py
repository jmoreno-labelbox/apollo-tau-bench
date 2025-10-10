# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BuildRoute(Tool):
    """Build a property showing route for clients."""
    
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = kwargs.get('client_id')
        date = kwargs.get('date')
        stops_ordered_json = kwargs.get('stops_ordered_json')
        map_url = kwargs.get('map_url')
        created_by_broker_id = kwargs.get('created_by_broker_id')
        
        if not all([client_id, date, stops_ordered_json, created_by_broker_id]):
            return json.dumps({
                "error": "client_id, date, stops_ordered_json, and created_by_broker_id are required"
            }, indent=2)
        
        # Generate route entry
        route = {
            "route_id": 401,
            "client_id": client_id,
            "date": date,
            "stops_ordered": stops_ordered_json,
            "map_url": map_url,
            "created_by_broker_id": created_by_broker_id,
            "status": "active",
            "created_at": "2024-08-21T00:00:00Z"
        }
        
        return json.dumps({
            "success": True,
            "route_id": 401,
            "message": f"Route created for client {client_id}",
            "route": route
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "build_route",
                "description": "Build a property showing route for clients",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID for the route"
                        },
                        "date": {
                            "type": "string",
                            "description": "Date for the route in YYYY-MM-DD format"
                        },
                        "stops_ordered_json": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Ordered list of property IDs to visit"
                        },
                        "map_url": {
                            "type": "string",
                            "description": "URL to the route map"
                        },
                        "created_by_broker_id": {
                            "type": "integer",
                            "description": "Broker ID creating the route"
                        }
                    },
                    "required": ["client_id", "date", "stops_ordered_json", "created_by_broker_id"]
                }
            }
        }
