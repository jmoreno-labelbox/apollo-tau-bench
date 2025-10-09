from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetOutboundOrderById(Tool):
    """Utility for obtaining an outbound order using its order ID."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str) -> str:
        orders = data.get("outbound_orders", {}).values()
        for order in orders.values():
            if order["order_id"] == order_id:
                payload = order
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Order with ID {order_id} not found."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOutboundOrderById",
                "description": "Retrieve outbound order using order ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Order ID (e.g., 'ORD-0004')",
                        }
                    },
                    "required": ["order_id"],
                },
            },
        }
