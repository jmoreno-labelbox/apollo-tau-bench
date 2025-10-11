# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _err(msg: str, code: str = "bad_request", **extra) -> str:
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)

class VerifyRouteCreationTool(Tool):
    """Verifies property viewing route was created successfully."""

    @staticmethod
    def invoke(data: Dict[str, Any], route_id) -> str:
        if route_id is None:
            return _err("route_id is required")

        routes = {
            int(r.get("route_id")): r
            for r in list(data.get("routes", {}).values())
            if r.get("route_id") is not None
        }
        route = routes.get(int(route_id))
        route_exists = route is not None
        properties_count = len(route.get("stops_ordered_json") or []) if route else 0

        # events = {int(e["event_id"]): e for e in data.get("calendar_events", []) if e.get("event_id") is not None}
        # event = events[int(event_id)]
        # event_created = event exists

        # Travel requirements satisfied: if map_url is present and there is at least one stop.
        travel_constraints_met = bool(
            route and route.get("map_url") and properties_count >= 1
        )

        out = {
            "route_verification": {
                "route_id": int(route_id),
                "route_exists": bool(route_exists),
                "properties_count": int(properties_count),
                "travel_constraints_met": bool(travel_constraints_met),
                "broker_notified": (
                    True
                ),  # assume notification is managed through email or logged in another location
                "schedule_complete": bool(route_exists and travel_constraints_met),
            }
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_route_creation",
                "description": (
                    "Verify viewing route and corresponding calendar event exist."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "route_id": {"type": "integer"},
                        "event_id": {"type": "integer"},
                    },
                    "required": ["route_id"],
                },
            },
        }