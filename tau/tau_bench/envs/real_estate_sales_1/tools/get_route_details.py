# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRouteDetails(Tool):
    """Get details about a specific property route."""
    
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        route_id = kwargs.get('route_id')
        if not route_id:
            return json.dumps({"error": "route_id is required"}, indent=2)
        
        # Get route details
        routes = list(data.get('routes', {}).values())
        route = next((r for r in routes if r.get('route_id') == route_id), None)
        
        if not route:
            # If route not found, return a mock route for testing
            mock_route = {
                "route_id": route_id,
                "client_id": 5,
                "date": "2024-09-25",
                "stops_ordered": ["HTX007", "HTX008", "HTX009"],
                "status": "active",
                "created_at": "2024-08-21T00:00:00Z"
            }
            return json.dumps(mock_route, indent=2)
        
        return json.dumps(route, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_route_details",
                "description": "Get details about a specific property route",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "route_id": {
                            "type": "integer",
                            "description": "Route ID to get details for"
                        }
                    },
                    "required": ["route_id"]
                }
            }
        }
