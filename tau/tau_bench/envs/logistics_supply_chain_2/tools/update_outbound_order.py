from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateOutboundOrder(Tool):
    """Utility for modifying details of outbound orders."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, updates: dict[str, Any] = None) -> str:
        orders = data.get("outbound_orders", [])

        for order in orders:
            if order["order_id"] == order_id:
                order.update(updates)
                payload = {"success": f"outbound order {order_id} updated"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"order_id {order_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateOutboundOrder",
                "description": "Update outbound order by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The outbound order ID to update",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Fields and values to update",
                        },
                    },
                    "required": ["order_id", "updates"],
                },
            },
        }
