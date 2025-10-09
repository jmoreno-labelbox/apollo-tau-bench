from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateSupplyOrder(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        supplier_id: str,
        item_id: str,
        quantity: int,
        unit_cost: float,
    ) -> str:
        pass
        suppliers = data["suppliers"]
        supply_orders = data["supply_orders"]
        products = data["products"]

        product = [row for row in products.values() if item_id in row["variants"].keys()]
        if not product:
            payload = {"error": "Product not found"}
            out = json.dumps(payload)
            return out
        product = product[0]

        #Verify if the supplier is present
        supplier = [row for row in suppliers.values() if row["supplier_id"] == supplier_id]
        if len(supplier) > 1:
            payload = {"error": "Multiple suppliers found"}
            out = json.dumps(payload)
            return out
        if not supplier:
            payload = {"error": "Supplier not found"}
            out = json.dumps(payload)
            return out
        supplier = supplier[0]

        #Initiate a new supply order
        supply_order_id = f"#SO{len(supply_orders) + 1:04d}"
        total_cost = round(unit_cost * quantity, 2)
        supply_order = {
            "supply_order_id": supply_order_id,
            "supplier_id": supplier_id,
            "product_id": product["product_id"],
            "item_id": item_id,
            "quantity": quantity,
            "status": "pending",
            "order_date": "2024-10-26T00:01:34.394073",  #Constant timestamp for consistency
            "unit_cost": unit_cost,
            "total_cost": total_cost,
        }

        #Insert the supply order into the database
        supply_data["orders"][order_id] = supply_order
        payload = supply_order
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateSupplyOrder",
                "description": "Create a new supply order for a supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "The ID of the supplier to create the supply order for.",
                        },
                        "item_id": {
                            "type": "string",
                            "description": "The item ID to be ordered.",
                        },
                        "quantity": {
                            "type": "integer",
                            "description": "The quantity of the item to be ordered.",
                        },
                        "unit_cost": {
                            "type": "number",
                            "description": "The unit cost of the item.",
                        },
                    },
                    "required": ["supplier_id", "item_id", "quantity", "unit_cost"],
                },
            },
        }
