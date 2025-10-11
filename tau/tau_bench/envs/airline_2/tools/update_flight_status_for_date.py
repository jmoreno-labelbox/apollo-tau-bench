# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _j(v):
    return v if isinstance(v, str) else json.dumps(v, separators=(",", ":"), ensure_ascii=False)

class UpdateFlightStatusForDate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], flight_numbers: Optional[List[str]], date: str, new_status: str) -> str:
        updated = []
        errors = []
        for f in list(data.get("flights", {}).values()):
            if f.get("flight_number") not in set(flight_numbers):
                continue
            day = (f.get("dates") or {}).get(date)
            if not isinstance(day, dict):
                errors.append({"error":"date_not_found","flight_number":f.get("flight_number"),"date":date})
                continue
            day["status"] = new_status.lower()
            updated.append(f.get("flight_number"))

        if not updated and errors:
            return _j(errors[0])  # initial error
        elif not updated:
            return _j({"error":"flight_not_found","flight_numbers":flight_numbers})
        else:
            return _j({"flight_numbers": updated, "date": date, "status": new_status.lower()})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"update_flight_status_for_date",
            "description":"Set per-day status on a flight_number's date entry deterministically.",
            "parameters":{"type":"object","properties":{
                "flight_numbers":{"type":"array","items":{"type":"string"}},
                "date":{"type":"string"},
                "new_status":{"type":"string"}
            },"required":["flight_numbers","date","new_status"]}
        }}