# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateReservationStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], reservation_id: str, new_status: str) -> str:
        reservations = list(data.get("reservations", {}).values())
        for r in reservations:
            if r.get("reservation_id") == reservation_id:
                r["status"] = new_status
                return _j(r)
        return _j({"error":"reservation_not_found","reservation_id":reservation_id})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"update_reservation_status",
            "description":"Update the status of a reservation (e.g., confirmed, ticketed, cancelled).",
            "parameters":{"type":"object","properties":{
                "reservation_id":{"type":"string"},
                "new_status":{"type":"string"}
            },"required":["reservation_id","new_status"]}
        }}
