from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetOrdersByStatus(Tool):
    """Utility for fetching outbound orders based on their status."""

    @staticmethod
    def invoke(data: dict[str, Any], status: str, list_of_ids: list[str] = None) -> str:
        orders = data.get("outbound_orders", {}).values()
        result = [
            order["order_id"]
            for order in orders.values() if order["status"].lower() == status.lower()
        ]
        if list_of_ids:
            result = [r for r in result.values() if r in list_of_ids]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrdersByStatus",
                "description": "Retrieve all outbound orders with a given status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "Status of the order (e.g., 'Shipped', 'Delivered')",
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of orders to choose from.",
                        },
                    },
                    "required": ["status"],
                },
            },
        }
