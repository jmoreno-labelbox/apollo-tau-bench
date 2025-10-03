from tau_bench.envs.tool import Tool
import json
from typing import Any

class BuildRoute(Tool):
    """Construct a route for property showings for clients."""

    @staticmethod
    def invoke(data: dict[str, Any], client_id: str = None, date: str = None, stops_ordered_json: str = None, map_url: str = None, created_by_broker_id: str = None) -> str:
        if not all([client_id, date, stops_ordered_json, created_by_broker_id]):
            payload = {
                    "error": "client_id, date, stops_ordered_json, and created_by_broker_id are required"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Establish a route record
        route = {
            "route_id": 401,
            "client_id": client_id,
            "date": date,
            "stops_ordered": stops_ordered_json,
            "map_url": map_url,
            "created_by_broker_id": created_by_broker_id,
            "status": "active",
            "created_at": "2024-08-21T00:00:00Z",
        }
        payload = {
                "success": True,
                "route_id": 401,
                "message": f"Route created for client {client_id}",
                "route": route,
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
                "name": "buildRoute",
                "description": "Build a property showing route for clients",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID for the route",
                        },
                        "date": {
                            "type": "string",
                            "description": "Date for the route in YYYY-MM-DD format",
                        },
                        "stops_ordered_json": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Ordered list of property IDs to visit",
                        },
                        "map_url": {
                            "type": "string",
                            "description": "URL to the route map",
                        },
                        "created_by_broker_id": {
                            "type": "integer",
                            "description": "Broker ID creating the route",
                        },
                    },
                    "required": [
                        "client_id",
                        "date",
                        "stops_ordered_json",
                        "created_by_broker_id",
                    ],
                },
            },
        }
