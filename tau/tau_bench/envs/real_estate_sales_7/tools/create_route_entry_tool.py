# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _next_int_id(rows: List[Dict[str, Any]], key: str) -> int:
    mx = 0
    for r in rows:
        try:
            v = int(r.get(key, 0))
            if v > mx:
                mx = v
        except Exception:
            continue
    return mx + 1

def _err(msg: str, code: str = "bad_request", **extra) -> str:
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)

class CreateRouteEntryTool(Tool):
    """Creates entry in routes table."""

    @staticmethod
    def invoke(data: Dict[str, Any], client_id, created_by_broker_id, map_url, route_date, stops_ordered_json) -> str:

        if (
            client_id is None
            or not route_date
            or not isinstance(stops_ordered_json, list)
            or not map_url
            or created_by_broker_id is None
        ):
            return _err(
                "client_id, route_date, stops_ordered_json(list), map_url, created_by_broker_id are required"
            )

        rows = data.setdefault("routes", [])
        route_id = _next_int_id(rows, "route_id")
        rec = {
            "route_id": route_id,
            "client_id": int(client_id),
            "date": str(route_date),
            "stops_ordered_json": stops_ordered_json,
            "map_url": str(map_url),
            "created_by_broker_id": int(created_by_broker_id),
            "created_at": HARD_TS,
        }
        rows.append(rec)
        return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_route_entry",
                "description": "Creates entry in routes table.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "route_date": {"type": "string"},
                        "stops_ordered_json": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "map_url": {"type": "string"},
                        "created_by_broker_id": {"type": "integer"},
                    },
                    "required": [
                        "client_id",
                        "route_date",
                        "stops_ordered_json",
                        "map_url",
                        "created_by_broker_id",
                    ],
                },
            },
        }