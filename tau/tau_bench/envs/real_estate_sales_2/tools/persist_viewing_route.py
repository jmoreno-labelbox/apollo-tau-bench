# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class PersistViewingRoute(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], client_id, created_by_broker_id, date, map_url, stops_ordered_json) -> str:
        routes = list(data.get("routes", {}).values())
        new_id = _next_auto_id(routes, "route_id")
        row = {
            "route_id": new_id,
            "client_id": client_id,
            "date": date,
            "stops_ordered_json": stops_ordered_json,
            "map_url": map_url or f"https://maps.google.com/route/route_{new_id:03d}",
            "created_by_broker_id": created_by_broker_id,
            "created_at": _now_iso_fixed(),
        }
        routes.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "persist_viewing_route",
                "description": "Persist a route with ordered stops and a map link.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "date": {"type": "string"},
                        "stops_ordered_json": {"type": "array", "items": {"type": "string"}},
                        "map_url": {"type": "string"},
                        "created_by_broker_id": {"type": "integer"},
                    },
                    "required": ["client_id", "date", "stops_ordered_json", "created_by_broker_id"],
                },
            },
        }
