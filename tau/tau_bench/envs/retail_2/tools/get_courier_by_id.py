# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCourierById(Tool):
    """Retrieve courier details from couriers.json by courier_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], courier_id: str) -> str:
        couriers = data.get("couriers", [])
        for c in couriers:
            if c.get("courier_id") == courier_id:
                return json.dumps(c)
        return json.dumps({"error": "Courier not found", "courier_id": courier_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_courier_by_id",
                "description": "Get courier details from couriers.json by courier_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "courier_id": {"type": "string"}
                    },
                    "required": ["courier_id"]
                }
            }
        }
