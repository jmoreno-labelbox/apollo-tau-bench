from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class ReserveOrderId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], orders: list[dict[str, Any]] = None, _id_reservations: dict[str, Any] = None) -> str:
        used = [o.get("order_id") for o in (orders or [])]
        reserved = (_id_reservations or {}).get("order_ids", [])
        next_id = _next_sequential_id(list(used) + list(reserved), "O")
        resv = data.setdefault("_id_reservations", {})
        resv["order_ids"] = list(set(reserved + [next_id]))
        payload = {"order_id": next_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReserveOrderId",
                "description": "Generate and reserve the next order_id (O###) by scanning existing orders and prior reservations.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
