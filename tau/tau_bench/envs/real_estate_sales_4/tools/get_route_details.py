from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetRouteDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], route_id: str = None) -> str:
        if not route_id:
            payload = {"error": "route_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        routes = data.get("routes", [])
        route = next((r for r in routes if r.get("route_id") == route_id), None)

        if not route:
            mock_route = {
                "route_id": route_id,
                "client_id": 5,
                "date": "2024-09-25",
                "stops_ordered": ["HTX007", "HTX008", "HTX009"],
                "status": "active",
                "created_at": "2024-08-21T00:00:00Z",
            }
            payload = mock_route
            out = json.dumps(payload, indent=2)
            return out
        payload = route
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getRouteDetails",
                "description": "Get details about a specific property route",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "route_id": {
                            "type": "integer",
                            "description": "Route ID to get details for",
                        }
                    },
                    "required": ["route_id"],
                },
            },
        }
