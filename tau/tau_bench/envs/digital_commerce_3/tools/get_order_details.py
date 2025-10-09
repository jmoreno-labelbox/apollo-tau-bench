from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetOrderDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: Any, orders: list = None) -> str:
        order_id = _idstr(order_id)
        order = next(
            (
                o
                for o in (orders or data.get("orders", {}))
                if f"{o.get('order_id')}" == f"{order_id}"
            ),
            None,
        )
        payload = order or {}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getOrderDetails",
                "description": "Returns full order record by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }
