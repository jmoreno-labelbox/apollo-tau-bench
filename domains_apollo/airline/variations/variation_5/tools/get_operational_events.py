from tau_bench.envs.tool import Tool
from __future__ import annotations
import json
from datetime import date, datetime, timedelta  #required for fallback window enlargement
from decimal import ROUND_HALF_UP, Decimal
from typing import Any
import re
from datetime import date as _date

class GetOperationalEvents(Tool):
    """Enumerate operational events for a flight within a date range; optionally filter by types.
    Provides `excluded_dates` (unique YYYY-MM-DD) for use in pricing filters."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        start_date: str,
        end_date: str,
        flight_number: str | None = None,
        types: list[str] | None = None
    ) -> str:
        types = {_norm_status(t) for t in (types or [])}

        events_src = data.get("operational_events", [])
        out: list[dict[str, Any]] = []
        for ev in events_src:
            # be accommodating to schema: date / event_date / timestamp
            raw = ev.get("date") or ev.get("event_date") or ev.get("timestamp")
            if not raw:
                continue
            day = str(raw)[:10]  # YYYY-MM-DD also derived from ISO datetimes
            if not (start_date <= day <= end_date):
                continue
            if flight_number and ev.get("flight_number") != flight_number:
                continue
            ev_type = _norm_status(ev.get("type") or ev.get("status"))
            if types and ev_type not in types:
                continue
            out.append({"date": day, "type": ev_type, "raw": ev})

        excluded_dates = sorted({e["date"] for e in out})

        return _json(
            {"events": out, "excluded_dates": excluded_dates, "total": len(out)}
        )
        pass
        types = {_norm_status(t) for t in (types or [])}

        events_src = data.get("operational_events", [])
        out: list[dict[str, Any]] = []
        for ev in events_src:
            #be accommodating to schema: date / event_date / timestamp
            raw = ev.get("date") or ev.get("event_date") or ev.get("timestamp")
            if not raw:
                continue
            day = str(raw)[:10]  #YYYY-MM-DD also derived from ISO datetimes
            if not (start_date <= day <= end_date):
                continue
            if flight_number and ev.get("flight_number") != flight_number:
                continue
            ev_type = _norm_status(ev.get("type") or ev.get("status"))
            if types and ev_type not in types:
                continue
            out.append({"date": day, "type": ev_type, "raw": ev})

        excluded_dates = sorted({e["date"] for e in out})

        return _json(
            {"events": out, "excluded_dates": excluded_dates, "total": len(out)}
        )

    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetOperationalEvents",
                "description": "List operational events for flight/date range; returns excluded_dates and total.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                        "types": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["start_date", "end_date"],
                },
            },
        }
