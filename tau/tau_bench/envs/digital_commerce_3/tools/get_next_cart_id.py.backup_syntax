from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetNextCartId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], carts: list[dict[str, Any]] = None) -> str:
        if carts is None:
            carts = []
        if not carts:
            next_id = 706
        else:
            max_id = max(int(c.get("cart_id", "0")) for c in carts.values()
            next_id = max_id + 1
        payload = {"next_cart_id": f"{next_id}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetNextCartId",
                "description": "Return the next available cart_id as a zero-padded string.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
