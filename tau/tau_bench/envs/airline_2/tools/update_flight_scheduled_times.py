# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateFlightScheduledTimes(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        flight_number: str,
        scheduled_departure_time_est: Optional[str]=None,
        scheduled_arrival_time_est: Optional[str]=None
    ) -> str:
        for f in list(data.get("flights", {}).values()):
            if f.get("flight_number") != flight_number:
                continue
            # only update fields that are provided
            if scheduled_departure_time_est is not None:
                f["scheduled_departure_time_est"] = scheduled_departure_time_est
            if scheduled_arrival_time_est is not None:
                f["scheduled_arrival_time_est"] = scheduled_arrival_time_est
            return _j({
                "flight_number": flight_number,
                "scheduled_departure_time_est": f.get("scheduled_departure_time_est"),
                "scheduled_arrival_time_est": f.get("scheduled_arrival_time_est"),
            })
        return _j({"error": "flight_not_found", "flight_number": flight_number})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"update_flight_scheduled_times",
            "description":"Update the estimated scheduled departure/arrival times for a flight (top-level schedule fields).",
            "parameters":{"type":"object","properties":{
                "flight_number":{"type":"string"},
                "scheduled_departure_time_est":{"type":"string","description":"Time-only (24-hour): HH:MM:SS"},
                "scheduled_arrival_time_est":{"type":"string","description":"Time-only (24-hour): HH:MM:SS"},
            },"required":["flight_number"]}
        }}
