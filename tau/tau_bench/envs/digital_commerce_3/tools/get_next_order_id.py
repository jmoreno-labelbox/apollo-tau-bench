# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetNextOrderId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        orders = list(data.get("orders", {}).values())
        if not orders:
            next_id = 9017
        else:
            max_id = max(int(o.get("order_id", "0")) for o in orders)
            next_id = max_id + 1
        return json.dumps({"next_order_id": f"{next_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_next_order_id",
                "description": "Return the next available order_id as a zero-padded string.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
