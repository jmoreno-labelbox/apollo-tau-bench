# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetFlightAssignmentByDate(Tool):
    """
    Readback to prove aircraft assignment visibility on a dated flight.
    """
    @staticmethod
    def invoke(
        data: Dict[str, Any], *,
        flight_number: str,
        date: str,
    ) -> str:
        f = _get_flight(data, flight_number)
        if not f:
            return _json({"error": "flight_not_found"})
        rec = _get_date_record(f, date)
        if not rec:
            return _json({"error": "invalid_date_format", "date": date})
        return _json({
            "flight_number": flight_number,
            "date": date
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_flight_assignment_by_date",
                "description": "Return the assigned aircraft_id for a specific flight/date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_number": {"type": "string"},
                        "date": {"type": "string", "description": "YYYY-MM-DD"}
                    },
                    "required": ["flight_number", "date"],
                    "additionalProperties": False
                }
            }
        }
