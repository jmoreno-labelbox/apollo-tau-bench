# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetNextCartId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        carts = data.get("carts", [])
        if not carts:
            next_id = 706
        else:
            max_id = max(int(c.get("cart_id", "0")) for c in carts)
            next_id = max_id + 1
        return json.dumps({"next_cart_id": f"{next_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_next_cart_id",
                "description": "Return the next available cart_id as a zero-padded string.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
