# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool










def _norm_status(s: str) -> str:
    return (s or "").strip().lower()

def _json(data: Any) -> str:
    return json.dumps(data, indent=2, sort_keys=True, default=str)

def _get_flight(data: Dict[str, Any], flight_number: str) -> Optional[Dict[str, Any]]:
    for f in data.get("flights", []):
        if f.get("flight_number") == flight_number:
            return f
    return None

def _get_date_record(flight: Dict[str, Any], day: str) -> Optional[Dict[str, Any]]:
    return (flight or {}).get("dates", {}).get(day)

class GetFlightStatusByDate(Tool):
    """Return status for a specific flight/date."""
    @staticmethod
    def invoke(
        data: Dict[str, Any], *,
        flight_number: str,
        date: str
    ) -> str:
        f = _get_flight(data, flight_number)
        if not f:
            return _json({"error":"flight_not_found"})
        rec = _get_date_record(f, date)
        if not rec:
            return _json({"error":"price_not_available_for_date"})
        return _json({"flight_number": flight_number, "date": date, "flight_status": _norm_status(rec.get("status"))})

    @staticmethod
    def get_info():
        return {
            "type":"function",
            "function":{
                "name":"get_flight_status_by_date",
                "description":"Status for a flight on a given date.",
                "parameters":{
                    "type":"object",
                    "properties":{
                    "flight_number":{"type":"string"},
                    "date":{"type":"string"}},
                    "required":["flight_number","date"]
                }
            }
        }