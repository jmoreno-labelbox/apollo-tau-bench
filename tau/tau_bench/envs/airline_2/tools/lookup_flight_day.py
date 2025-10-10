# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LookupFlightDay(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], date: str , flight_number: Optional[str]=None) -> str:
        for f in list(data.get("flights", {}).values()):
            if flight_number and f.get("flight_number") != flight_number:
                continue
            day = (f.get("dates") or {}).get(date)
            if day is not None:
                # combine top-level schedule with per-day status/times
                out = {
                    "flight_number": f.get("flight_number"),
                    "origin": f.get("origin"),
                    "destination": f.get("destination"),
                    "scheduled_departure_time_est": f.get("scheduled_departure_time_est"),
                    "scheduled_arrival_time_est": f.get("scheduled_arrival_time_est"),
                    "date": date,
                    "day": day,
                }
                return _j(out)
        return _j({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"lookup_flight_day",
            "description":"Return combined schedule + per-day status for a flight_number on a specific date (YYYY-MM-DD).",
            "parameters":{"type":"object","properties":{
                "date": {"type": "string"},
                "flight_number":{"type":"string"},
            },"required":["date"]}
        }}
