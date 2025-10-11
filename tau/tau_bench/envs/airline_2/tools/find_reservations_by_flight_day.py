# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _j(v):
    return v if isinstance(v, str) else json.dumps(v, separators=(",", ":"), ensure_ascii=False)

class FindReservationsByFlightDay(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], flight_number: str, date: str) -> str:
        out = []
        for r in list(data.get("reservations", {}).values()):
            for seg in r.get("flights", []):
                if seg.get("flight_number") == flight_number and seg.get("date") == date:
                    out.append(r)
                    break
        return _j(out)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"find_reservations_by_flight_day",
            "description":"Return reservations that include a segment with the given flight_number on the given date.",
            "parameters":{"type":"object","properties":{
                "flight_number":{"type":"string"},
                "date":{"type":"string"}
            },"required":["flight_number","date"]}
        }}