from tau_bench.envs.tool import Tool
import json
from typing import Any

class BuildRoute(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        client_id: str = None,
        date: str = None,
        stops_ordered_json: str = None,
        map_url: str = None,
        created_by_broker_id: str = None
    ) -> str:
        routes = data.get("routes", [])
        new_id = _next_int_id(routes, "route_id")
        row = {
            "route_id": new_id,
            "client_id": client_id,
            "date": date,
            "stops_ordered_json": stops_ordered_json,
            "map_url": map_url or f"https://maps.google.com/route/route_{new_id:03d}",
            "created_by_broker_id": created_by_broker_id,
            "created_at": _fixed_now_iso(),
        }
        routes.append(row)
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BuildRoute",
                "description": "Persist a route with ordered stops and a map link.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "date": {"type": "string"},
                        "stops_ordered_json": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "map_url": {"type": "string"},
                        "created_by_broker_id": {"type": "integer"},
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
