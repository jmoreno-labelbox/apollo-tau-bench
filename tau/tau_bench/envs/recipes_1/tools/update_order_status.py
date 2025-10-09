from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateOrderStatus(Tool):
    """Update orders.status_enum to a new state (e.g., 'placed', 'delivered')."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: int = None, new_status: str = None) -> str:
        if order_id is None or not new_status:
            return _json_dump({"error": "order_id and new_status are required"})
        row = _require(data, "orders", "order_id", int(order_id))
        if not row:
            return _json_dump({"error": f"order_id {order_id} not found"})
        row["status_enum"] = str(new_status)
        return _json_dump(row)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateOrderStatus",
                "description": "Update the status of an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "integer"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["order_id", "new_status"],
                },
            },
        }
