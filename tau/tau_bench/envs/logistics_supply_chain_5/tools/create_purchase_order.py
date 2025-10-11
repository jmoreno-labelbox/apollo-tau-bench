# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreatePurchaseOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], destination_warehouse, quantity, sku, supplier_id, notes = "", priority = "Medium", unit_price = "") -> str:
        unit_price_specific = unit_price

        if not all([supplier_id, sku, quantity, destination_warehouse]):
            return json.dumps({
                "error": "supplier_id, sku, quantity, and destination_warehouse are required"
            })

        suppliers = list(data.get("supplier_master", {}).values())
        products = list(data.get("product_master", {}).values())
        warehouses = list(data.get("warehouses", {}).values())

        supplier = next((s for s in suppliers if s.get("supplier_id") == supplier_id), None)
        if not supplier:
            return json.dumps({"error": f"Supplier {supplier_id} not found"})

        product = next((p for p in products if p.get("sku") == sku), None)
        if not product:
            return json.dumps({"error": f"Product {sku} not found"})

        warehouse = next((w for w in warehouses if w.get("warehouse_id") == destination_warehouse), None)
        if not warehouse:
            return json.dumps({"error": f"Warehouse {destination_warehouse} not found"})

        existing_pos = data.get("purchase_orders", [])
        po_counter = len(existing_pos) + 1
        po_id = f"PO-{supplier_id}-{sku}-{po_counter:03d}"

        total_cost = product.get("unit_price", 0) * quantity
        if unit_price_specific:
            total_cost = unit_price_specific * quantity

        fixed_creation_date = "2024-07-20T18:06:05.000000"
        fixed_delivery_date = "2024-08-19T18:06:05.000000"

        purchase_order = {
            "po_id": po_id,
            "supplier_id": supplier_id,
            "supplier_name": supplier.get("supplier_name"),
            "sku": sku,
            "product_name": product.get("product_name"),
            "quantity": quantity,
            "unit_price": product.get("unit_price"),
            "total_cost": total_cost,
            "destination_warehouse": destination_warehouse,
            "priority": priority,
            "notes": notes,
            "status": "Created",
            "created_date": fixed_creation_date,
            "expected_delivery": fixed_delivery_date
        }

        if "purchase_orders" not in data:
            data["purchase_orders"] = []
        data["purchase_orders"].append(purchase_order)

        return json.dumps({
            "status": "Created",
            "total_cost": total_cost,
            "priority": priority,
            "po_id": po_id,
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_purchase_order",
                "description": "Create a new purchase order for inventory replenishment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string", "description": "Supplier identifier"},
                        "sku": {"type": "string", "description": "Product SKU"},
                        "quantity": {"type": "integer", "description": "Order quantity"},
                        "destination_warehouse": {"type": "string", "description": "Destination warehouse ID"},
                        "priority": {"type": "string", "description": "Order priority (Low/Medium/High/Critical)"},
                        "notes": {"type": "string", "description": "Additional order notes"},
                        "unit_price": {"type": "number", "description": "Unit price of the product (optional, defaults to product master)"},
                    },
                    "required": ["supplier_id", "sku", "quantity", "destination_warehouse"]
                }
            }
        }
