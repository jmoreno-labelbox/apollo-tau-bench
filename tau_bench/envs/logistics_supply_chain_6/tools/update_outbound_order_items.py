from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateOutboundOrderItems(Tool):
    """Utility for including or excluding items from a pending outbound order."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str,
        items_to_add: list[dict[str, Any]] | None = None,
        items_to_remove: list[dict[str, Any]] | None = None
    ) -> str:
        """Run the tool with the provided parameters."""
        orders = data.get("outbound_orders", [])
        inventory = data.get("inventory", [])
        order_found = False
        for order in orders:
            if order.get("order_id") == order_id:
                order_found = True
                if order["status"] != "Pending":
                    payload = {
                        "error": f"Order {order_id} cannot be modified as its status is '{order['status']}'"
                    }
                    out = json.dumps(
                        payload, indent=2,
                    )
                    return out

                warehouse_id = order["warehouse_id"]

                # Handle additions
                if items_to_add:
                    for item_to_add in items_to_add:
                        sku = item_to_add["sku"]
                        quantity = item_to_add["quantity"]
                        # Verify stock
                        stock_found = False
                        for inv_item in inventory:
                            if (
                                inv_item["warehouse_id"] == warehouse_id
                                and inv_item["sku"] == sku
                            ):
                                if inv_item["quantity_available"] < quantity:
                                    payload = {
                                        "error": f"Insufficient stock for SKU {sku}. Available: {inv_item['quantity_available']}, Requested: {quantity}"
                                    }
                                    out = json.dumps(
                                        payload, indent=2,
                                    )
                                    return out
                                stock_found = True
                                break
                        if not stock_found:
                            payload = {
                                "error": f"SKU {sku} not found in warehouse {warehouse_id}"
                            }
                            out = json.dumps(
                                payload, indent=2,
                            )
                            return out

                        # Distribute stock and include item
                        for inv_item in inventory:
                            if (
                                inv_item["warehouse_id"] == warehouse_id
                                and inv_item["sku"] == sku
                            ):
                                inv_item["quantity_allocated"] += quantity
                                inv_item["quantity_available"] -= quantity
                                order["items"].append(item_to_add)
                                order["total_cost"] += (
                                    inv_item.get("unit_cost", 0) * quantity
                                )
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
                                    payload = {
                                        "error": f"Cannot remove {quantity_to_remove} of SKU {sku_to_remove}, only {order_item['quantity']} in order."
                                    }
                                    out = json.dumps(
                                        payload, indent=2,
                                    )
                                    return out

                                # Release stock allocation
                                for inv_item in inventory:
                                    if (
                                        inv_item["warehouse_id"] == warehouse_id
                                        and inv_item["sku"] == sku_to_remove
                                    ):
                                        inv_item[
                                            "quantity_allocated"
                                        ] -= quantity_to_remove
                                        inv_item[
                                            "quantity_available"
                                        ] += quantity_to_remove
                                        order["total_cost"] -= (
                                            inv_item.get("unit_cost", 0)
                                            * quantity_to_remove
                                        )
                                        break

                                order_item["quantity"] -= quantity_to_remove
                                if order_item["quantity"] == 0:
                                    order["items"].pop(i)
                                break
                        if not item_in_order:
                            payload = {
                                "error": f"SKU {sku_to_remove} not found in order {order_id}"
                            }
                            out = json.dumps(
                                payload, indent=2,
                            )
                            return out

                order["total_cost"] = round(order["total_cost"], 2)
                order["status"] = "Updated"
                payload = {
                    "order_id": order_id,
                    "new_total_cost": order["total_cost"],
                    "status": "Updated",
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out

        if not order_found:
            payload = {"error": f"Order with ID {order_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        return ""
        """Run the tool with the provided parameters."""
        pass
        orders = data.get("outbound_orders", [])
        inventory = data.get("inventory", [])
        order_found = False
        for order in orders:
            if order.get("order_id") == order_id:
                order_found = True
                if order["status"] != "Pending":
                    payload = {
                            "error": f"Order {order_id} cannot be modified as its status is '{order['status']}'"
                        }
                    out = json.dumps(
                        payload, indent=2,
                    )
                    return out

                warehouse_id = order["warehouse_id"]

                #Handle additions
                if items_to_add:
                    for item_to_add in items_to_add:
                        sku = item_to_add["sku"]
                        quantity = item_to_add["quantity"]
                        #Verify stock
                        stock_found = False
                        for inv_item in inventory:
                            if (
                                inv_item["warehouse_id"] == warehouse_id
                                and inv_item["sku"] == sku
                            ):
                                if inv_item["quantity_available"] < quantity:
                                    payload = {
                                            "error": f"Insufficient stock for SKU {sku}. Available: {inv_item['quantity_available']}, Requested: {quantity}"
                                        }
                                    out = json.dumps(
                                        payload, indent=2,
                                    )
                                    return out
                                stock_found = True
                                break
                        if not stock_found:
                            payload = {
                                    "error": f"SKU {sku} not found in warehouse {warehouse_id}"
                                }
                            out = json.dumps(
                                payload, indent=2,
                            )
                            return out

                        #Distribute stock and include item
                        for inv_item in inventory:
                            if (
                                inv_item["warehouse_id"] == warehouse_id
                                and inv_item["sku"] == sku
                            ):
                                inv_item["quantity_allocated"] += quantity
                                inv_item["quantity_available"] -= quantity
                                order["items"].append(item_to_add)
                                order["total_cost"] += (
                                    inv_item.get("unit_cost", 0) * quantity
                                )
                                break

                #Handle removals
                if items_to_remove:
                    for item_to_remove in items_to_remove:
                        sku_to_remove = item_to_remove["sku"]
                        quantity_to_remove = item_to_remove["quantity"]
                        item_in_order = False
                        for i, order_item in enumerate(order["items"]):
                            if order_item["sku"] == sku_to_remove:
                                item_in_order = True
                                if order_item["quantity"] < quantity_to_remove:
                                    payload = {
                                            "error": f"Cannot remove {quantity_to_remove} of SKU {sku_to_remove}, only {order_item['quantity']} in order."
                                        }
                                    out = json.dumps(
                                        payload, indent=2,
                                    )
                                    return out

                                #Release stock allocation
                                for inv_item in inventory:
                                    if (
                                        inv_item["warehouse_id"] == warehouse_id
                                        and inv_item["sku"] == sku_to_remove
                                    ):
                                        inv_item[
                                            "quantity_allocated"
                                        ] -= quantity_to_remove
                                        inv_item[
                                            "quantity_available"
                                        ] += quantity_to_remove
                                        order["total_cost"] -= (
                                            inv_item.get("unit_cost", 0)
                                            * quantity_to_remove
                                        )
                                        break

                                order_item["quantity"] -= quantity_to_remove
                                if order_item["quantity"] == 0:
                                    order["items"].pop(i)
                                break
                        if not item_in_order:
                            payload = {
                                    "error": f"SKU {sku_to_remove} not found in order {order_id}"
                                }
                            out = json.dumps(
                                payload, indent=2,
                            )
                            return out

                order["total_cost"] = round(order["total_cost"], 2)
                order["status"] = "Updated"
                payload = {
                        "order_id": order_id,
                        "new_total_cost": order["total_cost"],
                        "status": "Updated",
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out

        if not order_found:
            payload = {"error": f"Order with ID {order_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        return ""

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide the specifications of the tool for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "updateOutboundOrderItems",
                "description": "Adds or removes items from a pending outbound customer order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The ID of the order to modify.",
                        },
                        "items_to_add": {
                            "type": "array",
                            "description": "A list of items to add to the order.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {
                                        "type": "string",
                                        "description": "Product SKU.",
                                    },
                                    "quantity": {
                                        "type": "integer",
                                        "description": "Number of units to add.",
                                    },
                                },
                                "required": ["sku", "quantity"],
                            },
                        },
                        "items_to_remove": {
                            "type": "array",
                            "description": "A list of items to remove from the order.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {
                                        "type": "string",
                                        "description": "Product SKU.",
                                    },
                                    "quantity": {
                                        "type": "integer",
                                        "description": "Number of units to remove.",
                                    },
                                },
                                "required": ["sku", "quantity"],
                            },
                        },
                    },
                    "required": ["order_id"],
                },
            },
        }
