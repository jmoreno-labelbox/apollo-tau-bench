# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOrdersForHousehold(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int) -> str:
        rows = [
            o for o in list(data.get("orders", {}).values()) if int(o.get("household_id")) == int(household_id)
        ]
        return json({"orders": rows})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_orders_for_household",
                "description": "List orders for a household.",
                "parameters": {
                    "type": "object",
                    "properties": {"household_id": {"type": "integer"}},
                    "required": ["household_id"],
                },
            },
        }
