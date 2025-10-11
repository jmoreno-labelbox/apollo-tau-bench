# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchGetSupplyOrders(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], supplier_ids: List[str], min_quantity: int = None, max_quantity: int = None, status: str = None, statuses: List[str] = None, min_cost: float = None, max_cost: float = None) -> str:
        """
        Search and retrieve supply orders for specified suppliers with optional filtering
        Returns only product_ids, item_ids, supplier_ids, and supply_order_ids

        Data Sources: supply_orders.json (supply_order_id, supplier_id, quantity, status, total_cost)
        """
        if not supplier_ids:
            return json.dumps({
                "error": "Supplier IDs list cannot be empty",
                "status": "failed"
            })

        # Fundamental validation
        if min_quantity is not None and min_quantity < 0:
            return json.dumps({"error": "Minimum quantity must be non-negative", "status": "failed"})
        if max_quantity is not None and max_quantity < 0:
            return json.dumps({"error": "Maximum quantity must be non-negative", "status": "failed"})
        if min_cost is not None and min_cost < 0:
            return json.dumps({"error": "Minimum cost must be non-negative", "status": "failed"})
        if max_cost is not None and max_cost < 0:
            return json.dumps({"error": "Maximum cost must be non-negative", "status": "failed"})

        # Manage filtering based on status (single or multiple).
        if status and statuses:
            return json.dumps({
                "error": "Cannot specify both 'status' and 'statuses' parameters. Use one or the other.",
                "status": "failed"
            })

        status_filter = []
        valid_statuses = ["pending", "fulfilled", "cancelled"]

        if status:
            if status not in valid_statuses:
                return json.dumps({"error": f"Invalid status '{status}'. Valid statuses: {', '.join(valid_statuses)}", "status": "failed"})
            status_filter = [status]
        elif statuses:
            invalid_statuses = [s for s in statuses if s not in valid_statuses]
            if invalid_statuses:
                return json.dumps({"error": f"Invalid statuses: {', '.join(invalid_statuses)}. Valid statuses: {', '.join(valid_statuses)}", "status": "failed"})
            status_filter = statuses

        # Retrieve product details for item-to-product associations.
        products = list(data.get("products", {}).values())
        item_to_product_map = {}
        for product in products:
            product_id = product.get("product_id")
            if product_id:
                variants = product.get("variants", {})
                for item_id in variants.keys():
                    item_to_product_map[item_id] = product_id

        # Select supply orders and gather their IDs.
        supply_orders = data.get("supply_orders", [])
        all_supply_order_ids = set()
        all_supplier_ids = set()
        all_product_ids = set()
        all_item_ids = set()

        for order in supply_orders:
            order_supplier_id = order.get("supplier_id")
            order_quantity = order.get("quantity", 0)
            order_status = order.get("status", "")
            order_cost = order.get("total_cost", 0.0)

            # Implement filters
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

            # Gather identifiers from corresponding orders.
            supply_order_id = order.get("supply_order_id")
            if supply_order_id:
                all_supply_order_ids.add(supply_order_id)

            if order_supplier_id:
                all_supplier_ids.add(order_supplier_id)

            # Retrieve product_ids and item_ids.
            if order.get("product_id"):
                all_product_ids.add(order.get("product_id"))

            if order.get("item_id"):
                all_item_ids.add(order.get("item_id"))
                # Associate item with product if it isn't already linked.
                product_id = item_to_product_map.get(order.get("item_id"))
                if product_id:
                    all_product_ids.add(product_id)

            # Process orders containing multiple items
            if "items" in order and order.get("items"):
                for item_detail in order.get("items", []):
                    item_id = item_detail.get("item_id")
                    if item_id:
                        all_item_ids.add(item_id)
                        # Associate item with product.
                        product_id = item_to_product_map.get(item_id)
                        if product_id:
                            all_product_ids.add(product_id)

        # Transform sets into ordered lists.
        result = {
            "status": "success",
            "supply_order_ids": sorted(list(all_supply_order_ids)),
            "supplier_ids": sorted(list(all_supplier_ids)),
            "product_ids": sorted(list(all_product_ids)),
            "item_ids": sorted(list(all_item_ids)),
            "total_orders": len(all_supply_order_ids),
            "total_suppliers": len(all_supplier_ids),
            "total_products": len(all_product_ids),
            "total_items": len(all_item_ids)
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_get_supply_orders",
                "description": "Search and retrieve supply orders for specified suppliers with optional filtering. Returns only the essential IDs: supply_order_ids, supplier_ids, product_ids, and item_ids.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of supplier identifiers to search orders for (e.g., ['#SUP0001', '#SUP0002'])"
                        },
                        "min_quantity": {
                            "type": "integer",
                            "description": "Optional minimum quantity filter - only returns orders with quantity >= this value",
                            "minimum": 0
                        },
                        "max_quantity": {
                            "type": "integer",
                            "description": "Optional maximum quantity filter - only returns orders with quantity <= this value",
                            "minimum": 0
                        },
                        "status": {
                            "type": "string",
                            "description": "Optional single status filter - only returns orders with this status (cannot be used with 'statuses')",
                            "enum": ["pending", "fulfilled", "cancelled"]
                        },
                        "statuses": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "enum": ["pending", "fulfilled", "cancelled"]
                            },
                            "description": "Optional list of statuses to filter by - returns orders matching any of these statuses (cannot be used with 'status')"
                        },
                        "min_cost": {
                            "type": "number",
                            "description": "Optional minimum total cost filter - only returns orders with total_cost >= this value",
                            "minimum": 0
                        },
                        "max_cost": {
                            "type": "number",
                            "description": "Optional maximum total cost filter - only returns orders with total_cost <= this value",
                            "minimum": 0
                        }
                    },
                    "required": ["supplier_ids"]
                }
            }
        }
