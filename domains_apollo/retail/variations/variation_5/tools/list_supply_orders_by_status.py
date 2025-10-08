from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class ListSupplyOrdersByStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], status: str, supplier_id: str = None, limit: int = 20) -> str:
        if not status:
            payload = {"error": "status is required"}
            out = json.dumps(payload)
            return out

        supply_orders = data["supply_orders"]
        filtered_orders = []

        for order in supply_orders:
            if order["status"] == status:
                if supplier_id and order["supplier_id"] != supplier_id:
                    continue
                filtered_orders.append(order)

        # Arrange by order date, with the latest first
        filtered_orders.sort(key=lambda x: x["order_date"], reverse=True)
        payload = filtered_orders[:limit]
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listSupplyOrdersByStatus",
                "description": "Get supply orders filtered by status, optionally by supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "Status to filter by (pending, fulfilled, cancelled)",
                        },
                        "supplier_id": {
                            "type": "string",
                            "description": "Optional supplier ID to filter by",
                        },
                        "limit": {
                            "type": "integer",
                            "description": "Maximum number of orders to return",
                            "default": 20,
                        },
                    },
                    "required": ["status"],
                },
            },
        }
