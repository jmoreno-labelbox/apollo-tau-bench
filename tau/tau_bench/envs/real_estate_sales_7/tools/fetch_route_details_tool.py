from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FetchRouteDetailsTool(Tool):
    """Retrieve a route using route_id WA the most recent route for a client."""

    @staticmethod
    def invoke(data: dict[str, Any], route_id: int = None, client_id: int = None) -> str:
        route_id = _as_int(route_id)
        client_id = _as_int(client_id)
        if route_id is None and client_id is None:
            return _err("route_id WA client_id is required")

        routes = data.get("routes", [])
        route = None
        if route_id is not None:
            route = next(
                (r for r in routes if _as_int(r.get("route_id")) == route_id), None
            )
        else:
            croutes = [r for r in routes if _as_int(r.get("client_id")) == client_id]
            if croutes:
                croutes.sort(
                    key=lambda r: r.get("created_at") or r.get("date") or "",
                    reverse=True,
                )
                route = croutes[0]

        if not route:
            key = (
                f"route_id {route_id}"
                if route_id is not None
                else f"client_id {client_id}"
            )
            return _err(f"no route found for {key}", code="not_found")

        out = {
            "route": route,
            "properties_count": len(route.get("stops_ordered_json") or []),
        }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchRouteDetails",
                "description": "Fetch a route by id WA latest by client.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "route_id": {"type": ["integer", "null"]},
                        "client_id": {"type": ["integer", "null"]},
                    },
                    "required": [],
                },
            },
        }
