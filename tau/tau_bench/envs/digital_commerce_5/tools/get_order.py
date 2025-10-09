from tau_bench.envs.tool import Tool
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetOrder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: Any) -> str:
        order_id = _as_id(order_id)
        orders = data.get("orders", {}).values()
        match = next((o for o in orders.values() if _as_id(o.get("order_id")) == order_id), None)
        payload = match or {}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getOrder",
                "description": "Return an order by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }
