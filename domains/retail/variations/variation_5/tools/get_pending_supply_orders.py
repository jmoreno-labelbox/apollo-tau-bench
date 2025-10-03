from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class GetPendingSupplyOrders(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None) -> str:
        supply_orders = data["supply_orders"]
        pending_orders = []

        for order in supply_orders:
            if order["status"] == "pending":
                if supplier_id and order["supplier_id"] != supplier_id:
                    continue
                pending_orders.append(order)
        payload = pending_orders
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPendingSupplyOrders",
                "description": "Get all pending supply orders, optionally filtered by supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Optional supplier ID to filter by",
                        }
                    },
                },
            },
        }
