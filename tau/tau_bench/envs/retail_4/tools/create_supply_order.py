# © Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateSupplyOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id: str, quantity: int, unit_cost, product_id: str = None, item_id: str = None, item_ids: List[str] = None) -> str:
        """
        Create a new supply order for inventory replenishment with single or multiple item IDs
        If item_ids are provided, product_id will be determined automatically for each item
        unit_cost can be a single value or list of values corresponding to each item_id

        Writes to: supply_orders.json (creates new supply order entry)
        Data Sources: products.json for validation
        """
        if quantity <= 0:
            return json.dumps({"error": "Quantity must be greater than 0", "status": "failed"})

        # Check that unit_cost is either a float or a list of floats.
        unit_costs_list = []
        if isinstance(unit_cost, (int, float)):
            if unit_cost < 0:
                return json.dumps({"error": "Unit cost cannot be negative", "status": "failed"})
            unit_costs_list = [float(unit_cost)]
        elif isinstance(unit_cost, list):
            for i, cost in enumerate(unit_cost):
                if not isinstance(cost, (int, float)) or cost < 0:
                    return json.dumps({"error": f"Unit cost at index {i} must be a non-negative number", "status": "failed"})
            unit_costs_list = [float(c) for c in unit_cost]
        else:
            return json.dumps({"error": "Unit cost must be a number or list of numbers", "status": "failed"})

        # Ensure that at least one item ID is supplied.
        if not item_id and not item_ids:
            return json.dumps({
                "error": "Either item_id or item_ids must be provided",
                "status": "failed"
            })

        # Create the collection of items for processing.
        items_to_process = []
        if item_id:
            items_to_process.append(item_id)
        if item_ids:
            items_to_process.extend(item_ids)

        # Eliminate duplicates while maintaining sequence.
        items_to_process = list(dict.fromkeys(items_to_process))

        if not items_to_process:
            return json.dumps({
                "error": "No valid item IDs provided",
                "status": "failed"
            })

        # Verify that the unit_cost array corresponds to the count of items for several products.
        if len(items_to_process) > 1:
            if len(unit_costs_list) == 1:
                # Uniform cost per item for all units.
                unit_costs_list = unit_costs_list * len(items_to_process)
            elif len(unit_costs_list) != len(items_to_process):
                return json.dumps({
                    "error": f"When providing multiple items ({len(items_to_process)}), unit_cost must be a single value or a list with the same number of values ({len(unit_costs_list)} provided)",
                    "status": "failed"
                })

        # Retrieve product details
        products = list(data.get("products", {}).values())

        # If item_ids are supplied, retrieve the product_id corresponding to each item.
        if item_ids or not product_id:
            item_to_product_map = {}
            products_involved = set()

            for item in items_to_process:
                product_found = None
                for product in products:
                    variants = product.get("variants", {})
                    if item in variants:
                        product_found = product.get("product_id")
                        products_involved.add(product_found)
                        break

                if not product_found:
                    return json.dumps({
                        "error": f"Item {item} not found in any product catalog",
                        "status": "failed"
                    })

                item_to_product_map[item] = product_found

            # Display a warning if a single product_id is given but the items are from multiple products.
            if product_id and len(products_involved) > 1:
                return json.dumps({
                    "error": f"Items belong to multiple products: {list(products_involved)}. Cannot use single product_id parameter.",
                    "status": "failed"
                })

            # In the absence of a product_id and when items involve multiple products, manage the multi-product order.
            if len(products_involved) > 1:
                return CreateSupplyOrder._create_multi_product_order(
                    data, supplier_id, quantity, unit_costs_list, items_to_process, item_to_product_map, products
                )

            # Single product scenario - utilize the identified product_id.
            target_product_id = list(products_involved)[0]
        else:
            # Verify the existence of the provided product_id.
            target_product_id = product_id

        # Logic for ordering a single product
        return CreateSupplyOrder._create_single_product_order(
            data, supplier_id, target_product_id, quantity, unit_costs_list, items_to_process, products
        )

    @staticmethod
    def _create_single_product_order(data, supplier_id, product_id, quantity, unit_costs_list, items_to_process, products):
        """Create supply order for a single product"""
        # Condition: Supply orders must include a valid supplier_id and a corresponding product_id.
        product_found = None
        for product in products:
            if product.get("product_id") == product_id:
                product_found = product
                break

        if not product_found:
            return json.dumps({"error": f"Product {product_id} not found", "status": "failed"})

        # Condition: Verify that item_id is present in product variants prior to adding to orders.
        variants = product_found.get("variants", {})
        valid_items = []
        invalid_items = []

        for i, item in enumerate(items_to_process):
            if item in variants:
                valid_items.append({
                    "item_id": item,
                    "variant_options": variants[item].get("options", {}),
                    "current_price": variants[item].get("price", 0),
                    "available": variants[item].get("available", False),
                    "unit_cost": unit_costs_list[i] if i < len(unit_costs_list) else unit_costs_list[0]
                })
            else:
                invalid_items.append(item)

        if invalid_items:
            return json.dumps({
                "error": f"Item variants not found in product {product_id}: {', '.join(invalid_items)}",
                "status": "failed"
            })

        if not valid_items:
            return json.dumps({
                "error": f"No valid item variants found for product {product_id}",
                "status": "failed"
            })

        # Create a new identifier for the supply order.
        existing_supply_orders = data.get("supply_orders", [])
        order_number = len(existing_supply_orders) + 1
        new_supply_order_id = f"#SO{str(order_number).zfill(4)}"

        # Compute the total cost by applying the complete quantity to each item, without distribution.
        total_cost = 0
        item_details = []

        for i, item_info in enumerate(valid_items):
            item_unit_cost = item_info["unit_cost"]
            item_cost = item_unit_cost * quantity  # Every item receives the complete amount.
            total_cost += item_cost

            item_details.append({
                "item_id": item_info["item_id"],
                "quantity": quantity,  # Complete amount for each item
                "unit_cost": item_unit_cost,
                "item_total_cost": round(item_cost, 2),
                "variant_options": item_info["variant_options"]
            })

        # Determine the average cost per unit for legacy support.
        total_units = quantity * len(valid_items)  # Aggregate units for all items
        average_unit_cost = total_cost / total_units if total_units > 0 else 0

        # Generate a new supply order.
        new_supply_order = {
            "supply_order_id": new_supply_order_id,
            "supplier_id": supplier_id,
            "product_id": product_id,
            "items": item_details,
            "total_quantity": quantity * len(valid_items),  # Aggregate amount for all items
            "quantity_per_item": quantity,  # Count of each separate item
            "status": "pending",
            "order_date": datetime.now().isoformat(),
            "unit_cost": round(average_unit_cost, 2),  # Mean unit expense for backward compatibility
            "unit_costs": unit_costs_list,  # Cost per unit
            "total_cost": round(total_cost, 2)
        }

        # Include legacy item_id field for compatibility with previous versions when there is a single item.
        if len(valid_items) == 1:
            new_supply_order["item_id"] = valid_items[0]["item_id"]
            new_supply_order["quantity"] = quantity  # Utilize the initial amount for individual items.

        # INSERT OPERATION: Append new supply order to supply_orders.json
        if "supply_orders" not in data:
            data["supply_orders"] = []
        data["supply_orders"].append(new_supply_order)

        result = {
            "status": "success",
            "supply_order_created": new_supply_order_id,
            "supplier_id": supplier_id,
            "product_info": {
                "product_id": product_id,
                "product_name": product_found.get("name"),
                "total_items": len(valid_items)
            },
            "order_details": {
                "quantity_per_item": quantity,
                "total_quantity": new_supply_order["total_quantity"],
                "unit_costs": unit_costs_list,
                "average_unit_cost": round(average_unit_cost, 2),
                "total_cost": round(total_cost, 2),
                "items": item_details
            },
            "order_status": "pending",
        }

        return json.dumps(result)

    @staticmethod
    def _create_multi_product_order(data, supplier_id, quantity, unit_costs_list, items_to_process, item_to_product_map, products):
        """Create multiple supply orders when items belong to different products"""
        # Categorize items by product while preserving sequence and associated unit prices.
        product_groups = {}
        item_costs_map = {}

        for i, item in enumerate(items_to_process):
            product_id = item_to_product_map[item]
            item_unit_cost = unit_costs_list[i] if i < len(unit_costs_list) else unit_costs_list[0]

            if product_id not in product_groups:
                product_groups[product_id] = []

            product_groups[product_id].append(item)
            item_costs_map[item] = item_unit_cost

        # Generate individual supply orders for every product.
        created_orders = []

        for product_id, product_items in product_groups.items():
            # Retrieve the unit prices for the items of this product.
            product_unit_costs = [item_costs_map[item] for item in product_items]

            # Generate a separate supply order for this product with the complete quantity.
            # Every product receives the complete amount, without division.
            order_result = CreateSupplyOrder._create_single_product_order(
                data, supplier_id, product_id, quantity, product_unit_costs, product_items, products
            )

            order_data = json.loads(order_result)
            if order_data.get("status") == "success":
                created_orders.append({
                    "supply_order_id": order_data["supply_order_created"],
                    "product_id": product_id,
                    "items": product_items,
                    "unit_costs": product_unit_costs,
                    "quantity_per_item": quantity,  # Total amount for each item in this product.
                    "total_quantity": order_data["order_details"]["total_quantity"],
                    "total_cost": order_data["order_details"]["total_cost"]
                })
            else:
                return order_result  # Return an error if the creation of any order is unsuccessful.

        # Compute sums
        total_orders_cost = sum(order["total_cost"] for order in created_orders)
        total_quantity_ordered = sum(order["total_quantity"] for order in created_orders)

        result = {
            "status": "success",
            "order_type": "multi_product",
            "supplier_id": supplier_id,
            "total_orders_created": len(created_orders),
            "supply_orders": created_orders,
            "summary": {
                "total_products": len(product_groups),
                "quantity_per_item_per_product": quantity,
                "total_quantity_all_orders": total_quantity_ordered,
                "unit_costs": unit_costs_list,
                "total_cost": round(total_orders_cost, 2)
            },
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_supply_order",
                "description": "Create supply order(s) for inventory replenishment. When item_ids span multiple products, separate orders are created for each product automatically. Each item in each product gets the full specified quantity (quantity is not distributed among items).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string", "description": "Supplier identifier (e.g., '#SUP0001')"},
                        "quantity": {"type": "integer", "description": "Quantity to order for each item (not distributed - each item gets this full quantity)"},
                        "unit_cost": {
                            "oneOf": [
                                {"type": "number", "description": "Single unit cost applied to all items"},
                                {
                                    "type": "array",
                                    "items": {"type": "number"},
                                    "description": "List of unit costs, each corresponding to an item in item_ids (same order)"
                                }
                            ],
                            "description": "Cost per unit. Can be a single value or list of values matching item_ids order"
                        },
                        "product_id": {"type": "string", "description": "Product identifier (optional - auto-determined from item_ids if not provided)"},
                        "item_id": {"type": "string", "description": "Single product variant identifier (optional)"},
                        "item_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of product variant identifiers (optional). Product IDs will be determined automatically for each item."
                        }
                    },
                    "required": ["supplier_id", "quantity", "unit_cost"]
                }
            }
        }
