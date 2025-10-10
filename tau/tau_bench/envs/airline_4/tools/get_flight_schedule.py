# Copyright by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetFlightSchedule(Tool):
    """Return schedule for a flight in [start_date, end_date] with per-date status."""
    @staticmethod
    def invoke(
        data: Dict[str, Any], *,
        flight_number: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
    ) -> str:
        f = _get_flight(data, flight_number)
        if not f: return _json({"error":"flight_not_found"})
        rows = []
        for d, rec in (f.get("dates") or {}).items():
            if (not start_date or d >= start_date) and (not end_date or d <= end_date):
                rows.append({"date": d, "status": _norm_status(rec.get("status"))})
        rows.sort(key=lambda r: r["date"])
        return _json({"flight_number": flight_number, "schedule": rows})

    @staticmethod
    def get_info():
        return {
            "type":"function",
            "function":{
                "name":"get_flight_schedule",
                "description":"List per-date status for a flight within a window.",
                "parameters":{
                    "type":"object",
                    "properties":{
                        "flight_number": {"type":"string"},
                        "start_date": {"type":"string"},
                        "end_date": {"type":"string"}
                    },
                    "required":["flight_number"]
                }
            }
        }
