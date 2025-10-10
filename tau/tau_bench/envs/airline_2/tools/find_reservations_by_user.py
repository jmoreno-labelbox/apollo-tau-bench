# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindReservationsByUser(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        res = [r for r in list(data.get("reservations", {}).values()) if r.get("user_id") == user_id]
        return _j(res)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"find_reservations_by_user",
            "description":"Return all reservations for a user_id.",
            "parameters":{"type":"object","properties":{"user_id":{"type":"string"}},"required":["user_id"]}
        }}
