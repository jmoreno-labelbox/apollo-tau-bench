from tau_bench.envs.tool import Tool
from __future__ import annotations
import json
from datetime import date, datetime, timedelta  #required for fallback window enlargement
from decimal import ROUND_HALF_UP, Decimal
from typing import Any
import re
from datetime import date as _date

class UpdateFlightSchedule(Tool):
    """
    Modify schedule fields for a flight based on either:
      - an explicit 'dates' list (takes priority), or
      - an inclusive [start_date, end_date] range.
    Fields that can be updated: status, aircraft, crew (list).
    Generates missing date records under the flight if necessary (permitted by policy).
    Predictable; returns a summary and preview (first N).
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        flight_number: str,
        dates: list[str] | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        status: str | None = None,
        aircraft: str | None = None,
        crew: list[str] | None = None,
        max_preview: int = 0
    ) -> str:
        dates_list = dates or []
        #🔹 Standardize and verify right away when status is given
        if status is not None:
            s = _norm_status(status)
            if s and s not in FLIGHT_STATUS:
                return _json(
                    {
                        "error": "invalid_status",
                        "entity": "flight",
                        "provided": status,
                        "allowed": sorted(list(FLIGHT_STATUS)),
                    }
                )
            status = s  #replace with standardized lowercase

        #fundamental verification
        if not isinstance(dates_list, list):
            return _json({"error": "invalid_dates_param"})
        if not dates_list and not (start_date and end_date):
            return _json(
                {
                    "error": "missing_date_selector",
                    "reason": "Provide 'dates' or 'start_date'+'end_date'.",
                }
            )
        if crew is not None and not isinstance(crew, list):
            return _json(
                {"error": "invalid_crew", "reason": "crew must be a list of strings"}
            )

        f = _get_flight(data, flight_number)
        if not f:
            return _json(
                {
                    "error": "not_found",
                    "entity": "flight",
                    "flight_number": flight_number,
                }
            )

        #Construct target date set in a predictable manner
        targets: set[str] = set()
        if dates_list:
            for d in dates_list:
                if isinstance(d, str):
                    targets.add(d)
        else:
            for d in f.get("dates") or {}:
                if start_date <= d <= end_date:
                    targets.add(d)
            #generate absent dates within the range
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
        f.setdefault("dates", {}).values()

        for d in sorted(targets):
            rec = f["dates"].setdefault(d, {}).values()
            before = {
                "status": _norm_status(rec.get("status")),
                "aircraft": rec.get("aircraft"),
                "crew": rec.get("crew"),
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
                "crew": rec.get("crew"),
            }
            if before != after:
                changed += 1
                if len(preview) < max_preview:
                    preview.append({"date": d, "before": before, "after": after})

        return _json(
            {
                "success": True,
                "flight_number": flight_number,
                "changed": changed,
                "preview": preview,
            }
        )
        pass
        dates_list = dates or []
        #🔹 Standardize and verify right away when status is given
        if status is not None:
            s = _norm_status(status)
            if s and s not in FLIGHT_STATUS:
                return _json(
                    {
                        "error": "invalid_status",
                        "entity": "flight",
                        "provided": status,
                        "allowed": sorted(list(FLIGHT_STATUS)),
                    }
                )
            status = s  #replace with standardized lowercase

        #fundamental verification
        if not isinstance(dates_list, list):
            return _json({"error": "invalid_dates_param"})
        if not dates_list and not (start_date and end_date):
            return _json(
                {
                    "error": "missing_date_selector",
                    "reason": "Provide 'dates' or 'start_date'+'end_date'.",
                }
            )
        if crew is not None and not isinstance(crew, list):
            return _json(
                {"error": "invalid_crew", "reason": "crew must be a list of strings"}
            )

        f = _get_flight(data, flight_number)
        if not f:
            return _json(
                {
                    "error": "not_found",
                    "entity": "flight",
                    "flight_number": flight_number,
                }
            )

        #Construct target date set in a predictable manner
        targets: set[str] = set()
        if dates_list:
            for d in dates_list:
                if isinstance(d, str):
                    targets.add(d)
        else:
            for d in f.get("dates") or {}:
                if start_date <= d <= end_date:
                    targets.add(d)
            #generate absent dates within the range
            from datetime import datetime, timedelta

            def iter_days(s: str, e: str):
                pass
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
        f.setdefault("dates", {}).values()

        for d in sorted(targets):
            rec = f["dates"].setdefault(d, {}).values()
            before = {
                "status": _norm_status(rec.get("status")),
                "aircraft": rec.get("aircraft"),
                "crew": rec.get("crew"),
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
                "crew": rec.get("crew"),
            }
            if before != after:
                changed += 1
                if len(preview) < max_preview:
                    preview.append({"date": d, "before": before, "after": after})

        return _json(
            {
                "success": True,
                "flight_number": flight_number,
                "changed": changed,
                "preview": preview,
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateFlightSchedule",
                "description": "Update per-date schedule (status/aircraft/crew) for a flight by dates or by range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "dates": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Specific dates to update (YYYY-MM-DD).",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Inclusive start if using a range.",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "Inclusive end if using a range.",
                        },
                        "status": {
                            "type": "string",
                            "description": "e.g. 'available', 'cancelled', 'diverted'",
                        },
                        "aircraft": {"type": "string"},
                        "crew": {"type": "array", "items": {"type": "string"}},
                        "max_preview": {"type": "integer"},
                    },
                    "required": ["flight_number"],
                },
            },
        }
