from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SearchGetSupplyOrders:
    @staticmethod
    def invoke(
        data: dict[str, Any],
        supplier_ids: list[str],
        min_quantity: int = None,
        max_quantity: int = None,
        status: str = None,
        statuses: list[str] = None,
        min_cost: float = None,
        max_cost: float = None,
    ) -> str:
        """
        Search and retrieve supply orders for specified suppliers with optional filtering
        Returns only product_ids, item_ids, supplier_ids, and supply_order_ids

        Data Sources: supply_orders.json (supply_order_id, supplier_id, quantity, status, total_cost)
        """
        if not supplier_ids:
            payload = {"error": "Supplier IDs list cannot be empty", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Basic validation
        if min_quantity is not None and min_quantity < 0:
            payload = {"error": "Minimum quantity must be non-negative", "status": "failed"}
            out = json.dumps(payload)
            return out
        if max_quantity is not None and max_quantity < 0:
            payload = {"error": "Maximum quantity must be non-negative", "status": "failed"}
            out = json.dumps(payload)
            return out
        if min_cost is not None and min_cost < 0:
            payload = {"error": "Minimum cost must be non-negative", "status": "failed"}
            out = json.dumps(payload)
            return out
        if max_cost is not None and max_cost < 0:
            payload = {"error": "Maximum cost must be non-negative", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Handle status filtering (single or multiple)
        if status and statuses:
            payload = {
                "error": "Cannot specify both 'status' and 'statuses' parameters. Use one or the other.",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        status_filter = []
        valid_statuses = ["pending", "fulfilled", "cancelled"]

        if status:
            if status not in valid_statuses:
                payload = {
                    "error": f"Invalid status '{status}'. Valid statuses: {', '.join(valid_statuses)}",
                    "status": "failed",
                }
                out = json.dumps(payload)
                return out
            status_filter = [status]
        elif statuses:
            invalid_statuses = [s for s in statuses.values() if s not in valid_statuses]
            if invalid_statuses:
                payload = {
                    "error": f"Invalid statuses: {', '.join(invalid_statuses)}. Valid statuses: {', '.join(valid_statuses)}",
                    "status": "failed",
                }
                out = json.dumps(payload)
                return out
            status_filter = statuses

        # Get product information for item-to-product mapping
        products = data.get("products", {}).values()
        item_to_product_map = {}
        for product in products.values():
            product_id = product.get("product_id")
            if product_id:
                variants = product.get("variants", {}).values()
                for item_id in variants.keys():
                    item_to_product_map[item_id] = product_id

        # Filter supply orders and collect IDs
        supply_orders = data.get("supply_orders", {}).values()
        all_supply_order_ids = set()
        all_supplier_ids = set()
        all_product_ids = set()
        all_item_ids = set()

        for order in supply_orders.values():
            order_supplier_id = order.get("supplier_id")
            order_quantity = order.get("quantity", 0)
            order_status = order.get("status", "")
            order_cost = order.get("total_cost", 0.0)

            # Apply filters
            if order_supplier_id not in supplier_ids:
                continue
            if min_quantity is not None and order_quantity < min_quantity:
                continue
            if max_quantity is not None and order_quantity > max_quantity:
                continue
            if status_filter and order_status not in status_filter:
                continue
            if min_cost is not None and order_cost < min_cost:
                continue
            if max_cost is not None and order_cost > max_cost:
                continue

            # Collect IDs from matching orders
            supply_order_id = order.get("supply_order_id")
            if supply_order_id:
                all_supply_order_ids.add(supply_order_id)

            if order_supplier_id:
                all_supplier_ids.add(order_supplier_id)

            # Get product_ids and item_ids
            if order.get("product_id"):
                all_product_ids.add(order.get("product_id"))

            if order.get("item_id"):
                all_item_ids.add(order.get("item_id"))
                # Map item to product if not already present
                product_id = item_to_product_map.get(order.get("item_id"))
                if product_id:
                    all_product_ids.add(product_id)

            # Handle multi-item orders
            if "items" in order and order.get("items"):
                for item_detail in order.get("items", []):
                    item_id = item_detail.get("item_id")
                    if item_id:
                        all_item_ids.add(item_id)
                        # Map item to product
                        product_id = item_to_product_map.get(item_id)
                        if product_id:
                            all_product_ids.add(product_id)

        # Convert sets to sorted lists
        result = {
            "status": "success",
            "supply_order_ids": sorted(list(all_supply_order_ids)),
            "supplier_ids": sorted(list(all_supplier_ids)),
            "product_ids": sorted(list(all_product_ids)),
            "item_ids": sorted(list(all_item_ids)),
            "total_orders": len(all_supply_order_ids),
            "total_suppliers": len(all_supplier_ids),
            "total_products": len(all_product_ids),
            "total_items": len(all_item_ids),
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchGetSupplyOrders",
                "description": "Search and retrieve supply orders for specified suppliers with optional filtering. Returns only the essential IDs: supply_order_ids, supplier_ids, product_ids, and item_ids.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of supplier identifiers to search orders for (e.g., ['#SUP0001', '#SUP0002'])",
                        },
                        "min_quantity": {
                            "type": "integer",
                            "description": "Optional minimum quantity filter - only returns orders with quantity >= this value",
                            "minimum": 0,
                        },
                        "max_quantity": {
                            "type": "integer",
                            "description": "Optional maximum quantity filter - only returns orders with quantity <= this value",
                            "minimum": 0,
                        },
                        "status": {
                            "type": "string",
                            "description": "Optional single status filter - only returns orders with this status (cannot be used with 'statuses')",
                            "enum": ["pending", "fulfilled", "cancelled"],
                        },
                        "statuses": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "enum": ["pending", "fulfilled", "cancelled"],
                            },
                            "description": "Optional list of statuses to filter by - returns orders matching any of these statuses (cannot be used with 'status')",
                        },
                        "min_cost": {
                            "type": "number",
                            "description": "Optional minimum total cost filter - only returns orders with total_cost >= this value",
                            "minimum": 0,
                        },
                        "max_cost": {
                            "type": "number",
                            "description": "Optional maximum total cost filter - only returns orders with total_cost <= this value",
                            "minimum": 0,
                        },
                    },
                    "required": ["supplier_ids"],
                },
            },
        }
