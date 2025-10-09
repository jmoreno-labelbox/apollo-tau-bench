from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class ReserveCartId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], carts: list[dict[str, Any]] = None, _id_reservations: dict[str, Any] = None) -> str:
        used = [c.get("cart_id") for c in (carts or [])]
        reserved = (_id_reservations or {}).get("cart_ids", [])
        next_id = _next_sequential_id(list(used) + list(reserved), "C")
        resv = data.setdefault("_id_reservations", [])
        resv["cart_ids"] = list(set(reserved + [next_id]))
        payload = {"cart_id": next_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReserveCartId",
                "description": "Generate and reserve the next cart_id (C###) by scanning existing carts and prior reservations.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
