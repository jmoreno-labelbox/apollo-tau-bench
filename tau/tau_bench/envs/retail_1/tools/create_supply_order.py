# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateSupplyOrder(Tool): # WRITE
    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id: str, item_id: str, quantity: int, unit_cost: float) -> str:
        suppliers = data["suppliers"]
        supply_orders = data["supply_orders"]
        products = data["products"]

        product = [row for row in products if item_id in row["variants"].keys()]
        if not product:
            return json.dumps({"error": "Product not found"})
        product = product[0]

        # Check if the supplier exists
        supplier = [row for row in suppliers if row["supplier_id"] == supplier_id]
        if len(supplier) > 1:
            return json.dumps({"error": "Multiple suppliers found"})
        if not supplier:
            return json.dumps({"error": "Supplier not found"})
        supplier = supplier[0]

        # Create a new supply order
        supply_order_id = f"#SO{len(supply_orders) + 1:04d}"
        total_cost = round(unit_cost * quantity, 2)
        supply_order = {
            "supply_order_id": supply_order_id,
            "supplier_id": supplier_id,
            "product_id": product["product_id"],
            "item_id": item_id,
            "quantity": quantity,
            "status": "pending",
            "order_date": "2024-10-26T00:01:34.394073",  # Fixed timestamp for determinism
            "unit_cost": unit_cost,
            "total_cost": total_cost
        }

        # Add the supply order to the database
        supply_orders.append(supply_order)

        return json.dumps(supply_order)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_supply_order",
                "description": "Create a new supply order for a supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string", "description": "The ID of the supplier to create the supply order for."},
                        "item_id": {"type": "string", "description": "The item ID to be ordered."},
                        "quantity": {"type": "integer", "description": "The quantity of the item to be ordered."},
                        "unit_cost": {"type": "number", "description": "The unit cost of the item."}
                    },
                    "required": ["supplier_id", "item_id", "quantity", "unit_cost"]
                }
            }
        }
