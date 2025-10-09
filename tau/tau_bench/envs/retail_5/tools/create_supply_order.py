from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class CreateSupplyOrder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None, product_id: str = None, item_id: str = None, quantity: int = None, unit_cost: float = None) -> str:
        if not all([supplier_id, product_id, item_id, quantity, unit_cost]):
            payload = {
                    "error": "supplier_id, product_id, item_id, quantity, and unit_cost are required"
                }
            out = json.dumps(
                payload)
            return out

        supply_orders = data["supply_orders"]

        supply_order_id = f"#SO{generate_unique_id()}-{item_id}"
        total_cost = quantity * unit_cost

        new_order = {
            "supply_order_id": supply_order_id,
            "supplier_id": supplier_id,
            "product_id": product_id,
            "item_id": item_id,
            "quantity": quantity,
            "status": "pending",
            "order_date": get_current_timestamp(),
            "unit_cost": unit_cost,
            "total_cost": total_cost,
        }

        supply_data["orders"][order_id] = new_order
        payload = {
                "success": True,
                "supply_order_id": supply_order_id,
                "total_cost": total_cost,
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
                "name": "createSupplyOrder",
                "description": "Create a new supply order to restock inventory from a supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier ID to order from",
                        },
                        "product_id": {
                            "type": "string",
                            "description": "Product ID to order",
                        },
                        "item_id": {
                            "type": "string",
                            "description": "Specific item variant ID",
                        },
                        "quantity": {
                            "type": "integer",
                            "description": "Quantity to order",
                        },
                        "unit_cost": {"type": "number", "description": "Cost per unit"},
                    },
                    "required": [
                        "supplier_id",
                        "product_id",
                        "item_id",
                        "quantity",
                        "unit_cost",
                    ],
                },
            },
        }
