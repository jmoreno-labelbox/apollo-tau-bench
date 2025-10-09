from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateOrderStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: Any, new_status: Any) -> str:
        order_id = _idstr(order_id)
        new_status = f"{new_status}"
        order = next(
            (
                o
                for o in data.get("orders", [])
                if f"{o.get('order_id')}" == f"{order_id}"
            ),
            None,
        )
        if not order:
            payload = {"error": "Order not found."}
            out = json.dumps(payload, indent=2)
            return out
        order["status"] = new_status
        payload = order
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateOrderStatus",
                "description": "Updates order status deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["order_id", "new_status"],
                },
            },
        }
