# Copyright held by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListAllFaresByRoute(Tool):
    """List available fares (by flight/date) for a route, capped by limit (default 5)."""

    @staticmethod
    def invoke(
        data: Dict[str, Any], *,
        origin: str,
        destination: str,
        limit: int = 5,
        offset: int = 0
        ) -> str:

        # standardize inputs
        origin = (origin or "").upper()
        destination = (destination or "").upper()

        # page navigation
        try:
            limit = int(limit)
        except Exception:
            limit = 5
        if limit <= 0:
            limit = 5

        try:
            offset = int(offset)
        except Exception:
            offset = 0
        if offset < 0:
            offset = 0

        if not origin or not destination:
            return _json({"error": "missing_params", "reason": "origin and destination are required."})

        flights = _load_flights(data)
        rows: List[Dict[str, Any]] = []
        for f in flights:
            if f.get("origin") == origin and f.get("destination") == destination:
                for d, info in (f.get("dates") or {}).items():
                    if isinstance(info, dict) and  _norm_status(info.get("status")) == "available" and "prices" in info:
                        rows.append({
                            "flight_number": f["flight_number"],
                            "date": d,
                            "prices": info["prices"],
                            "available_seats": info.get("available_seats"),
                        })

        # order by date followed by flight_number
        rows.sort(key=lambda x: (x["date"], x["flight_number"]))

        total = len(rows)
        sliced = rows[offset: offset + limit]

        return _json({
            "route": {"origin": origin, "destination": destination},
            "total": total,
            "offset": offset,
            "limit": limit,
            "has_more": offset + limit < total,
            "fares": sliced
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_all_fares_by_route",
                "description": "List available fares for a given origin→destination route (paginated).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "origin": {"type": "string"},
                        "destination": {"type": "string"},
                        "limit": {"type": "integer", "minimum": 1, "description": "Max items to return (default 5)."},
                        "offset": {"type": "integer", "minimum": 0, "description": "Items to skip (default 0)."}
                    },
                    "required": ["origin", "destination"]
                }
            }
        }
