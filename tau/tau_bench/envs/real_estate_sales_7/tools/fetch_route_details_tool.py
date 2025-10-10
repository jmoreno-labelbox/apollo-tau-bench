# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchRouteDetailsTool(Tool):
    """Fetch a route by route_id or the latest route for a client."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        route_id = _as_int(kwargs.get("route_id"))
        client_id = _as_int(kwargs.get("client_id"))
        if route_id is None and client_id is None:
            return _err("route_id or client_id is required")

        routes = list(data.get("routes", {}).values())
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
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_route_details",
                "description": "Fetch a route by id or latest by client.",
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
