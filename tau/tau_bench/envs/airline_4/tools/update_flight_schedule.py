# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateFlightSchedule(Tool):
    """
    Update schedule fields for a flight on either:
      - explicit 'dates' list (takes precedence), or
      - an inclusive [start_date, end_date] window.
    Updatable fields: status, aircraft, crew (list).
    Creates missing date records under the flight if needed (allowed by policy).
    Deterministic; returns summary and preview (first N).
    """
    @staticmethod
    def invoke(
        data: Dict[str, Any], *,
        flight_number: str,
        dates: Optional[List[str]] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        status: Optional[str] = None,
        aircraft: Optional[str] = None,
        crew: Optional[List[str]] = None,
        max_preview: int = 0
    ) -> str:
        dates_list = dates or []
        # 🔹 Immediately normalize and validate when a status is given.
        if status is not None:
            s = _norm_status(status)
            if s and s not in FLIGHT_STATUS:
                return _json({
                    "error": "invalid_status",
                    "entity": "flight",
                    "provided": status,
                    "allowed": sorted(list(FLIGHT_STATUS))
                })
            status = s  # replace with normalized lowercase

        # fundamental verification
        if not isinstance(dates_list, list):
            return _json({"error": "invalid_dates_param"})
        if not dates_list and not (start_date and end_date):
            return _json({"error": "missing_date_selector", "reason": "Provide 'dates' or 'start_date'+'end_date'."})
        if crew is not None and not isinstance(crew, list):
            return _json({"error": "invalid_crew", "reason": "crew must be a list of strings"})

        f = _get_flight(data, flight_number)
        if not f:
            return _json({"error": "not_found", "entity": "flight", "flight_number": flight_number})

        # Establish the target date in a deterministic manner.
        targets: Set[str] = set()
        if dates_list:
            for d in dates_list:
                if isinstance(d, str):
                    targets.add(d)
        else:
            for d in (f.get("dates") or {}):
                if start_date <= d <= end_date:
                    targets.add(d)
            # generate absent dates within the specified range
            from datetime import datetime, timedelta
            def iter_days(s: str, e: str):
                ds = datetime.strptime(s, "%Y-%m-%d").date()
                de = datetime.strptime(e, "%Y-%m-%d").date()
                cur = ds
                while cur <= de:
                    yield cur.strftime("%Y-%m-%d")
                    cur = cur + timedelta(days=1)
            for d in iter_days(start_date, end_date):
                targets.add(d)

        changed = 0
        preview = []
        f.setdefault("dates", {})

        for d in sorted(targets):
            rec = f["dates"].setdefault(d, {})
            before = {
                "status": _norm_status(rec.get("status")),
                "aircraft": rec.get("aircraft"),
                "crew": rec.get("crew")
            }
            if status is not None:
                rec["status"] = status
            if aircraft is not None:
                rec["aircraft"] = aircraft
            if crew is not None:
                rec["crew"] = crew

            after = {
                "status": _norm_status(rec.get("status")),
                "aircraft": rec.get("aircraft"),
                "crew": rec.get("crew")
            }
            if before != after:
                changed += 1
                if len(preview) < max_preview:
                    preview.append({"date": d, "before": before, "after": after})

        return _json({
            "success": True,
            "flight_number": flight_number,
            "changed": changed,
            "preview": preview
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type":"function",
            "function": {
                "name": "update_flight_schedule",
                "description": "Update per-date schedule (status/aircraft/crew) for a flight by dates or by range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type":"string"},
                        "dates": {"type": "array", "items": {"type": "string"}, "description": "Specific dates to update (YYYY-MM-DD)."},
                        "start_date": {"type": "string", "description": "Inclusive start if using a range."},
                        "end_date": {"type": "string", "description": "Inclusive end if using a range."},
                        "status": {"type": "string", "description": "e.g. 'available', 'cancelled', 'diverted'"},
                        "aircraft": {"type": "string"},
                        "crew": {"type": "array", "items": {"type": "string"}},
                        "max_preview":{"type":"integer"}
                    },
                    "required": ["flight_number"]
                }
            }
        }
