# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _j(v):
    return v if isinstance(v, str) else json.dumps(v, separators=(",", ":"), ensure_ascii=False)

class GetFlightScheduledTimes(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], flight_number: str) -> str:
        for f in list(data.get("flights", {}).values()):
            if f.get("flight_number") == flight_number:
                return _j({
                    "flight_number": flight_number,
                    "scheduled_departure_time_est": f.get("scheduled_departure_time_est"),
                    "scheduled_arrival_time_est": f.get("scheduled_arrival_time_est"),
                })
        return _j({"error": "flight_not_found", "flight_number": flight_number})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"get_flight_scheduled_times",
            "description":"Return the estimated scheduled departure/arrival times for a flight.",
            "parameters":{"type":"object","properties":{
                "flight_number":{"type":"string"},
            },"required":["flight_number"]}
        }}