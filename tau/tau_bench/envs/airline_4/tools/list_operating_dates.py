# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListOperatingDates(Tool):
    """List all dates where a flight operates (status == 'available'), sorted ascending."""

    @staticmethod
    def invoke(
        data: Dict[str, Any], *,
        flight_number: str
    ) -> str:
        f = _get_flight(data, flight_number)

        if not f:
            return _json({"error":"flight_not_found"})
        dates = [
                d for d, rec in (f.get("dates") or {}).items() if _norm_status(rec.get("status")) =="available"
            ]
        dates.sort()
        return _json({"flight_number": flight_number, "dates": dates})

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_operating_dates",
                "description": "Return sorted available operating dates for a flight.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"}
                    },
                    "required": ["flight_number"]
                }
            }
        }
