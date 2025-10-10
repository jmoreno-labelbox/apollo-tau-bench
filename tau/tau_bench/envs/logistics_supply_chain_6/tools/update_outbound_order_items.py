# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateOutboundOrderItems(Tool):
    """Tool to add or remove items from a pending outbound order."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, items_to_add: Optional[List[Dict[str, Any]]] = None, items_to_remove: Optional[List[Dict[str, Any]]] = None) -> str:
        """Execute the tool with given parameters."""
        orders = data.get("outbound_orders", [])
        inventory = list(data.get("inventory", {}).values())
        order_found = False
        for order in orders:
            if order.get("order_id") == order_id:
                order_found = True
                if order["status"] != "Pending":
                    return json.dumps({"error": f"Order {order_id} cannot be modified as its status is '{order['status']}'"}, indent=2)

                warehouse_id = order["warehouse_id"]

                # Handle new entries
                if items_to_add:
                    for item_to_add in items_to_add:
                        sku = item_to_add["sku"]
                        quantity = item_to_add["quantity"]
                        # Verify inventory levels
                        stock_found = False
                        for inv_item in inventory:
                            if inv_item["warehouse_id"] == warehouse_id and inv_item["sku"] == sku:
                                if inv_item["quantity_available"] < quantity:
                                    return json.dumps({"error": f"Insufficient stock for SKU {sku}. Available: {inv_item['quantity_available']}, Requested: {quantity}"}, indent=2)
                                stock_found = True
                                break
                        if not stock_found:
                            return json.dumps({"error": f"SKU {sku} not found in warehouse {warehouse_id}"}, indent=2)

                        # Assign inventory and include item.
                        for inv_item in inventory:
                            if inv_item["warehouse_id"] == warehouse_id and inv_item["sku"] == sku:
                                inv_item["quantity_allocated"] += quantity
                                inv_item["quantity_available"] -= quantity
                                order["items"].append(item_to_add)
                                order["total_cost"] += inv_item.get("unit_cost", 0) * quantity
                                break

                # Handle removals
                if items_to_remove:
                    for item_to_remove in items_to_remove:
                        sku_to_remove = item_to_remove["sku"]
                        quantity_to_remove = item_to_remove["quantity"]
                        item_in_order = False
                        for i, order_item in enumerate(order["items"]):
                            if order_item["sku"] == sku_to_remove:
                                item_in_order = True
                                if order_item["quantity"] < quantity_to_remove:
                                    return json.dumps({"error": f"Cannot remove {quantity_to_remove} of SKU {sku_to_remove}, only {order_item['quantity']} in order."}, indent=2)

                                # Release inventory
                                for inv_item in inventory:
                                    if inv_item["warehouse_id"] == warehouse_id and inv_item["sku"] == sku_to_remove:
                                        inv_item["quantity_allocated"] -= quantity_to_remove
                                        inv_item["quantity_available"] += quantity_to_remove
                                        order["total_cost"] -= inv_item.get("unit_cost", 0) * quantity_to_remove
                                        break

                                order_item["quantity"] -= quantity_to_remove
                                if order_item["quantity"] == 0:
                                    order["items"].pop(i)
                                break
                        if not item_in_order:
                            return json.dumps({"error": f"SKU {sku_to_remove} not found in order {order_id}"}, indent=2)

                order["total_cost"] = round(order["total_cost"], 2)
                order["status"] = "Updated"
                return json.dumps({"order_id": order_id, "new_total_cost": order["total_cost"], "status": "Updated"}, indent=2)

        if not order_found:
            return json.dumps({"error": f"Order with ID {order_id} not found"}, indent=2)
        return ""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "update_outbound_order_items",
                "description": "Adds or removes items from a pending outbound customer order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The ID of the order to modify."},
                        "items_to_add": {
                            "type": "array",
                            "description": "A list of items to add to the order.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {"type": "string", "description": "Product SKU."},
                                    "quantity": {"type": "integer", "description": "Number of units to add."}
                                },
                                "required": ["sku", "quantity"]
                            }
                        },
                        "items_to_remove": {
                            "type": "array",
                            "description": "A list of items to remove from the order.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {"type": "string", "description": "Product SKU."},
                                    "quantity": {"type": "integer", "description": "Number of units to remove."}
                                },
                                "required": ["sku", "quantity"]
                            }
                        }
                    },
                    "required": ["order_id"],
                },
            },
        }
