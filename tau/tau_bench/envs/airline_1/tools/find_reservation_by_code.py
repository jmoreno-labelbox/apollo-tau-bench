# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindReservationByCode(Tool):
    """
    A tool to find a reservation by its unique code.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], reservation_code: str) -> str:
        reservations = list(data.get("reservations", {}).values())
        for res in reservations:
            if res.get("reservation_id") == reservation_code:
                return json.dumps(res)
        return json.dumps({"error": "Reservation not found", "reservation_code": reservation_code})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_reservation_by_code",
                "description": "Retrieves the full details of a reservation using its unique code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_code": {"type": "string", "description": "The unique reservation code (e.g., '4WQ150')."}
                    },
                    "required": ["reservation_code"]
                }
            }
        }
