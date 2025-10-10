# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ScanFlightsByDate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], date: str, flight_numbers: Optional[List[str]]=None, origin: Optional[str]=None, destination: Optional[str]=None, status: Optional[List[str]]=None) -> str:
        out = []
        for f in list(data.get("flights", {}).values()):
            day = (f.get("dates") or {}).get(date)
            if not isinstance(day, dict):
                continue
            if origin and f.get("origin") != origin:
                continue
            if destination and f.get("destination") != destination:
                continue
            if status and day.get("status") not in set(status):
                continue
            if flight_numbers and f.get("flight_number") not in set(flight_numbers):
                continue
            out.append({"flight_number": f.get("flight_number"),
                        "origin": f.get("origin"),
                        "destination": f.get("destination"),
                        "date": date,
                        "status": day.get("status"),
                        "scheduled_departure_time_est": f.get("scheduled_departure_time_est")})
        # organize by scheduled time followed by flight number
        out.sort(key=lambda x: (x.get("scheduled_departure_time_est",""), x.get("flight_number","")))
        return _j(out)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"scan_flights_by_date",
            "description":"Search flights by date with optional origin(iata_code)/destination(iata_code)/status filters; sorted by scheduled_departure_time_est.",
            "parameters":{"type":"object","properties":{
                "date":{"type":"string"},
                "flight_numbers":{"type":"array","items":{"type":"string"}},
                "origin":{"type":"string"},
                "destination":{"type":"string"},
                "status":{"type":"array","items":{"type":"string"}}
            },"required":["date"]}
        }}
