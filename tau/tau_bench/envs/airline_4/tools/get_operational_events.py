# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOperationalEvents(Tool):
    """List operational events for a flight in a date range; optionally filter by types.
       Exposes `excluded_dates` (unique YYYY-MM-DD) to feed into pricing filters."""
    @staticmethod
    def invoke(
        data: Dict[str, Any], *,
        start_date: str,
        end_date: str,
        flight_number: Optional[str] = None,
        types: Optional[List[str]] = None
    ) -> str:
        types = set([_norm_status(t) for t in (types or [])])

        events_src = data.get("operational_events", [])
        out: List[Dict[str, Any]] = []
        for ev in events_src:
            # be tolerant to schema: date / event_date / timestamp
            raw = ev.get("date") or ev.get("event_date") or ev.get("timestamp")
            if not raw:
                continue
            day = str(raw)[:10]  # YYYY-MM-DD from ISO datetimes too
            if not (start_date <= day <= end_date):
                continue
            if flight_number and ev.get("flight_number") != flight_number:
                continue
            ev_type = _norm_status(ev.get("type") or ev.get("status"))
            if types and ev_type not in types:
                continue
            out.append({"date": day, "type": ev_type, "raw": ev})

        excluded_dates = sorted({e["date"] for e in out})

        return _json({
            "events": out,
            "excluded_dates": excluded_dates,
            "total": len(out)
        })

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_operational_events",
                "description": "List operational events for flight/date range; returns excluded_dates and total.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                        "types": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["start_date", "end_date"]
                }
            }
        }
