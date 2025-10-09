from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetHighValueOutboundOrders(Tool):
    """Utility for obtaining outbound orders that exceed a certain value."""

    @staticmethod
    def invoke(data: dict[str, Any], min_value: int = 100000, list_of_ids: list = None) -> str:
        orders = data.get("outbound_orders", {}).values()
        result = [
            order["order_id"]
            for order in orders.values() if order.get("total_value", 0) >= min_value
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
                "name": "GetHighValueOutboundOrders",
                "description": "Retrieve outbound orders where total value exceeds the given threshold.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "min_value": {
                            "type": "number",
                            "description": "Minimum total value (default is 100000)",
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of orders to choose from.",
                        },
                    },
                },
            },
        }
