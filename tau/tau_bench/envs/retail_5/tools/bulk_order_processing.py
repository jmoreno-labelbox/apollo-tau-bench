from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class BulkOrderProcessing(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_ids: list[str] = None, new_status: str = None) -> str:
        if not order_ids or not new_status:
            payload = {"error": "order_ids and new_status are required"}
            out = json.dumps(payload)
            return out

        orders = data["orders"]
        updated_orders = []

        for order_id in order_ids:
            order = next((o for o in orders.values() if o["order_id"] == order_id), None)
            if order:
                old_status = order["status"]
                order["status"] = new_status
                updated_orders.append(
                    {
                        "order_id": order_id,
                        "old_status": old_status,
                        "new_status": new_status,
                    }
                )
        payload = {
                "success": True,
                "updated_orders": updated_orders,
                "total_updated": len(updated_orders),
                "updated_at": get_current_timestamp(),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "bulkOrderProcessing",
                "description": "Update the status of multiple orders at once.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of order IDs to update",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status for all orders",
                        },
                    },
                    "required": ["order_ids", "new_status"],
                },
            },
        }
