# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _j(v):
    return v if isinstance(v, str) else json.dumps(v, separators=(",", ":"), ensure_ascii=False)

class DelayFlightActualTimesForDate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], flight_number: str, date: str, delay_minutes: int, also_mark_status: Optional[str]=None) -> str:
        for f in list(data.get("flights", {}).values()):
            if f.get("flight_number") != flight_number:
                continue
            dates = f.get("dates") or {}
            day = dates.get(date)
            if not isinstance(day, dict):
                return _j({"error":"date_not_found","flight_number":flight_number,"date":date})
            def _bump(ts: Optional[str]):
                if not ts:
                    return ts
                # timestamp format: 2024-05-01T06:26:00 (without timezone)
                try:
                    dt = datetime.fromisoformat(ts)
                    dt = dt + timedelta(minutes=delay_minutes)
                    return dt.isoformat()
                except Exception:
                    return ts
            day["actual_departure_time_est"] = _bump(day.get("actual_departure_time_est"))
            day["actual_arrival_time_est"] = _bump(day.get("actual_arrival_time_est"))
            if also_mark_status:
                day["status"] = also_mark_status
            return _j({"flight_number": flight_number, "date": date, "delay_applied_minutes": delay_minutes, "status": day.get("status")})
        return _j({"error":"flight_not_found","flight_number":flight_number})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"delay_flight_actual_times_for_date",
            "description":"Add delay_minutes to actual_*_time_est fields for specific flight_number/date; optionally set status.",
            "parameters":{"type":"object","properties":{
                "flight_number":{"type":"string"},
                "date":{"type":"string"},
                "delay_minutes":{"type":"integer"},
                "also_mark_status":{"type":"string"}
            },"required":["flight_number","date","delay_minutes"]}
        }}