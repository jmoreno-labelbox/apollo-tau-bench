from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class CreateSupplyOrder(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        supplier_id: str,
        quantity: int,
        unit_cost,
        product_id: str = None,
        item_id: str = None,
        item_ids: list[str] = None,
    ) -> str:
        """
        Create a new supply order for inventory replenishment with single or multiple item IDs
        If item_ids are provided, product_id will be determined automatically for each item
        unit_cost can be a single value or list of values corresponding to each item_id

        Writes to: supply_orders.json (creates new supply order entry)
        Data Sources: products.json for validation
        """
        pass
        if quantity <= 0:
            payload = {"error": "Quantity must be greater than 0", "status": "failed"}
            out = json.dumps(
                payload)
            return out

        #Validate unit_cost (can be float or list of floats)
        unit_costs_list = []
        if isinstance(unit_cost, (int, float)):
            if unit_cost < 0:
                payload = {"error": "Unit cost cannot be negative", "status": "failed"}
                out = json.dumps(
                    payload)
                return out
            unit_costs_list = [float(unit_cost)]
        elif isinstance(unit_cost, list):
            for i, cost in enumerate(unit_cost):
                if not isinstance(cost, (int, float)) or cost < 0:
                    payload = {
                            "error": f"Unit cost at index {i} must be a non-negative number",
                            "status": "failed",
                        }
                    out = json.dumps(
                        payload)
                    return out
            unit_costs_list = [float(c) for c in unit_cost]
        else:
            payload = {
                    "error": "Unit cost must be a number or list of numbers",
                    "status": "failed",
                }
            out = json.dumps(
                payload)
            return out

        #Validate that at least one item identifier is provided
        if not item_id and not item_ids:
            payload = {
                    "error": "Either item_id or item_ids must be provided",
                    "status": "failed",
                }
            out = json.dumps(
                payload)
            return out

        #Build the list of items to process
        items_to_process = []
        if item_id:
            items_to_process.append(item_id)
        if item_ids:
            items_to_process.extend(item_ids)

        #Remove duplicates while preserving order
        items_to_process = list(dict.fromkeys(items_to_process))

        if not items_to_process:
            payload = {"error": "No valid item IDs provided", "status": "failed"}
            out = json.dumps(
                payload)
            return out

        #Validate unit_cost list matches item count for multiple items
        if len(items_to_process) > 1:
            if len(unit_costs_list) == 1:
                #Single unit cost for multiple items - use same cost for all
                unit_costs_list = unit_costs_list * len(items_to_process)
            elif len(unit_costs_list) != len(items_to_process):
                payload = {
                        "error": f"When providing multiple items ({len(items_to_process)}), unit_cost must be a single value or a list with the same number of values ({len(unit_costs_list)} provided)",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out

        #Get product information
        products = data.get("products", [])

        #When item_ids are provided, find product_id for each item
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
                    payload = {
                            "error": f"Item {item} not found in any product catalog",
                            "status": "failed",
                        }
                    out = json.dumps(
                        payload)
                    return out

                item_to_product_map[item] = product_found

            #If single product_id was provided but items belong to different products, show warning
            if product_id and len(products_involved) > 1:
                payload = {
                        "error": f"Items belong to multiple products: {list(products_involved)}. Cannot use single product_id parameter.",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out

            #If no product_id provided and items span multiple products, handle multi-product order
            if len(products_involved) > 1:
                return CreateSupplyOrder._create_multi_product_order(
                    data,
                    supplier_id,
                    quantity,
                    unit_costs_list,
                    items_to_process,
                    item_to_product_map,
                    products,
                )

            #Single product case - use the found product_id
            target_product_id = list(products_involved)[0]
        else:
            #product_id was provided, validate it exists
            target_product_id = product_id

        #Single product order logic
        return CreateSupplyOrder._create_single_product_order(
            data,
            supplier_id,
            target_product_id,
            quantity,
            unit_costs_list,
            items_to_process,
            products,
        )
        if quantity <= 0:
            payload = {"error": "Quantity must be greater than 0", "status": "failed"}
            out = json.dumps(
                payload)
            return out

        #Validate unit_cost (can be float or list of floats)
        unit_costs_list = []
        if isinstance(unit_cost, (int, float)):
            if unit_cost < 0:
                payload = {"error": "Unit cost cannot be negative", "status": "failed"}
                out = json.dumps(
                    payload)
                return out
            unit_costs_list = [float(unit_cost)]
        elif isinstance(unit_cost, list):
            for i, cost in enumerate(unit_cost):
                if not isinstance(cost, (int, float)) or cost < 0:
                    payload = {
                            "error": f"Unit cost at index {i} must be a non-negative number",
                            "status": "failed",
                        }
                    out = json.dumps(
                        payload)
                    return out
            unit_costs_list = [float(c) for c in unit_cost]
        else:
            payload = {
                    "error": "Unit cost must be a number or list of numbers",
                    "status": "failed",
                }
            out = json.dumps(
                payload)
            return out

        #Validate that at least one item identifier is provided
        if not item_id and not item_ids:
            payload = {
                    "error": "Either item_id or item_ids must be provided",
                    "status": "failed",
                }
            out = json.dumps(
                payload)
            return out

        #Build the list of items to process
        items_to_process = []
        if item_id:
            items_to_process.append(item_id)
        if item_ids:
            items_to_process.extend(item_ids)

        #Remove duplicates while preserving order
        items_to_process = list(dict.fromkeys(items_to_process))

        if not items_to_process:
            payload = {"error": "No valid item IDs provided", "status": "failed"}
            out = json.dumps(
                payload)
            return out

        #Validate unit_cost list matches item count for multiple items
        if len(items_to_process) > 1:
            if len(unit_costs_list) == 1:
                #Single unit cost for multiple items - use same cost for all
                unit_costs_list = unit_costs_list * len(items_to_process)
            elif len(unit_costs_list) != len(items_to_process):
                payload = {
                        "error": f"When providing multiple items ({len(items_to_process)}), unit_cost must be a single value or a list with the same number of values ({len(unit_costs_list)} provided)",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out

        #Get product information
        products = data.get("products", [])

        #When item_ids are provided, find product_id for each item
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
                    payload = {
                            "error": f"Item {item} not found in any product catalog",
                            "status": "failed",
                        }
                    out = json.dumps(
                        payload)
                    return out

                item_to_product_map[item] = product_found

            #If single product_id was provided but items belong to different products, show warning
            if product_id and len(products_involved) > 1:
                payload = {
                        "error": f"Items belong to multiple products: {list(products_involved)}. Cannot use single product_id parameter.",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out

            #If no product_id provided and items span multiple products, handle multi-product order
            if len(products_involved) > 1:
                return CreateSupplyOrder._create_multi_product_order(
                    data,
                    supplier_id,
                    quantity,
                    unit_costs_list,
                    items_to_process,
                    item_to_product_map,
                    products,
                )

            #Single product case - use the found product_id
            target_product_id = list(products_involved)[0]
        else:
            #product_id was provided, validate it exists
            target_product_id = product_id

        #Single product order logic
        return CreateSupplyOrder._create_single_product_order(
            data,
            supplier_id,
            target_product_id,
            quantity,
            unit_costs_list,
            items_to_process,
            products,
        )
    

    @staticmethod
    def _create_single_product_order(
        data,
        supplier_id,
        product_id,
        quantity,
        unit_costs_list,
        items_to_process,
        products,
    ):
        """Create supply order for a single product"""
        pass
        #Rule: Supply orders must reference valid supplier_id and existing product_id
        product_found = None
        for product in products:
            if product.get("product_id") == product_id:
                product_found = product
                break

        if not product_found:
            payload = {"error": f"Product {product_id} not found", "status": "failed"}
            out = json.dumps(
                payload)
            return out

        #Rule: Confirm item_id exists in product variants before including in orders
        variants = product_found.get("variants", {})
        valid_items = []
        invalid_items = []

        for i, item in enumerate(items_to_process):
            if item in variants:
                valid_items.append(
                    {
                        "item_id": item,
                        "variant_options": variants[item].get("options", {}),
                        "current_price": variants[item].get("price", 0),
                        "available": variants[item].get("available", False),
                        "unit_cost": (
                            unit_costs_list[i]
                            if i < len(unit_costs_list)
                            else unit_costs_list[0]
                        ),
                    }
                )
            else:
                invalid_items.append(item)

        if invalid_items:
            payload = {
                    "error": f"Item variants not found in product {product_id}: {', '.join(invalid_items)}",
                    "status": "failed",
                }
            out = json.dumps(
                payload)
            return out

        if not valid_items:
            payload = {
                    "error": f"No valid item variants found for product {product_id}",
                    "status": "failed",
                }
            out = json.dumps(
                payload)
            return out

        #Generate new supply order ID
        existing_supply_orders = data.get("supply_orders", [])
        order_number = len(existing_supply_orders) + 1
        new_supply_order_id = f"#SO{str(order_number).zfill(4)}"

        #Calculate total cost - each item gets the full quantity, not distributed
        total_cost = 0
        item_details = []

        for i, item_info in enumerate(valid_items):
            item_unit_cost = item_info["unit_cost"]
            item_cost = item_unit_cost * quantity  #Each item gets the full quantity
            total_cost += item_cost

            item_details.append(
                {
                    "item_id": item_info["item_id"],
                    "quantity": quantity,  #Full quantity for each item
                    "unit_cost": item_unit_cost,
                    "item_total_cost": round(item_cost, 2),
                    "variant_options": item_info["variant_options"],
                }
            )

        #Calculate average unit cost for legacy compatibility
        total_units = quantity * len(valid_items)  #Total units across all items
        average_unit_cost = total_cost / total_units if total_units > 0 else 0

        #Create new supply order
        new_supply_order = {
            "supply_order_id": new_supply_order_id,
            "supplier_id": supplier_id,
            "product_id": product_id,
            "items": item_details,
            "total_quantity": quantity
            * len(valid_items),  #Total quantity across all items
            "quantity_per_item": quantity,  #Quantity for each individual item
            "status": "pending",
            "order_date": datetime.now().isoformat(),
            "unit_cost": round(
                average_unit_cost, 2
            ),  #Average unit cost for legacy compatibility
            "unit_costs": unit_costs_list,  #Individual unit costs
            "total_cost": round(total_cost, 2),
        }

        #Add legacy item_id field for backward compatibility if only one item
        if len(valid_items) == 1:
            new_supply_order["item_id"] = valid_items[0]["item_id"]
            new_supply_order["quantity"] = (
                quantity  #Use original quantity for single item
            )

        #WRITE OPERATION: Add new supply order to supply_orders.json
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
                "total_items": len(valid_items),
            },
            "order_details": {
                "quantity_per_item": quantity,
                "total_quantity": new_supply_order["total_quantity"],
                "unit_costs": unit_costs_list,
                "average_unit_cost": round(average_unit_cost, 2),
                "total_cost": round(total_cost, 2),
                "items": item_details,
            },
            "order_status": "pending",
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def _create_multi_product_order(
        data,
        supplier_id,
        quantity,
        unit_costs_list,
        items_to_process,
        item_to_product_map,
        products,
    ):
        """Create multiple supply orders when items belong to different products"""
        pass
        #Group items by product, maintaining order and corresponding unit costs
        product_groups = {}
        item_costs_map = {}

        for i, item in enumerate(items_to_process):
            product_id = item_to_product_map[item]
            item_unit_cost = (
                unit_costs_list[i] if i < len(unit_costs_list) else unit_costs_list[0]
            )

            if product_id not in product_groups:
                product_groups[product_id] = []

            product_groups[product_id].append(item)
            item_costs_map[item] = item_unit_cost

        #Create separate supply orders for each product
        created_orders = []

        for product_id, product_items in product_groups.items():
            #Get unit costs for this product's items
            product_unit_costs = [item_costs_map[item] for item in product_items]

            #Create individual supply order for this product with full quantity
            #Each product gets the full quantity, not distributed
            order_result = CreateSupplyOrder._create_single_product_order(
                data,
                supplier_id,
                product_id,
                quantity,
                product_unit_costs,
                product_items,
                products,
            )

            order_data = json.loads(order_result)
            if order_data.get("status") == "success":
                created_orders.append(
                    {
                        "supply_order_id": order_data["supply_order_created"],
                        "product_id": product_id,
                        "items": product_items,
                        "unit_costs": product_unit_costs,
                        "quantity_per_item": quantity,  #Full quantity for each item in this product
                        "total_quantity": order_data["order_details"]["total_quantity"],
                        "total_cost": order_data["order_details"]["total_cost"],
                    }
                )
            else:
                return order_result  #Return error if any order creation fails

        #Calculate totals
        total_orders_cost = sum(order["total_cost"] for order in created_orders)
        total_quantity_ordered = sum(
            order["total_quantity"] for order in created_orders
        )

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
                "total_cost": round(total_orders_cost, 2),
            },
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateSupplyOrder",
                "description": "Create supply order(s) for inventory replenishment. When item_ids span multiple products, separate orders are created for each product automatically. Each item in each product gets the full specified quantity (quantity is not distributed among items).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier identifier (e.g., '#SUP0001')",
                        },
                        "quantity": {
                            "type": "integer",
                            "description": "Quantity to order for each item (not distributed - each item gets this full quantity)",
                        },
                        "unit_cost": {
                            "oneOf": [
                                {
                                    "type": "number",
                                    "description": "Single unit cost applied to all items",
                                },
                                {
                                    "type": "array",
                                    "items": {"type": "number"},
                                    "description": "List of unit costs, each corresponding to an item in item_ids (same order)",
                                },
                            ],
                            "description": "Cost per unit. Can be a single value or list of values matching item_ids order",
                        },
                        "product_id": {
                            "type": "string",
                            "description": "Product identifier (optional - auto-determined from item_ids if not provided)",
                        },
                        "item_id": {
                            "type": "string",
                            "description": "Single product variant identifier (optional)",
                        },
                        "item_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of product variant identifiers (optional). Product IDs will be determined automatically for each item.",
                        },
                    },
                    "required": ["supplier_id", "quantity", "unit_cost"],
                },
            },
        }
