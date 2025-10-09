from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateOutboundOrder(Tool):
    """Utility for generating a new outbound order for customers."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        customer_name: str,
        warehouse_id: str,
        items: list[dict[str, Any]],
        shipping_address: str,
        total_value: int | None = None
    ) -> str:
        """Run the tool with the provided parameters."""
        pass
        outbound_orders = data.get("outbound_orders", {}).values()
        inventory = data.get("inventory", {}).values()

        # Verify stock for all items initially
        for order_item in items:
            sku = order_item["sku"]
            quantity = order_item["quantity"]
            for inv_item in inventory.values():
                if inv_item["warehouse_id"] == warehouse_id and inv_item["sku"] == sku:
                    if inv_item["quantity_available"] < quantity:
                        payload = {
                            "error": f"Insufficient stock for SKU {sku}. Available: {inv_item['quantity_available']}, Requested: {quantity}"
                        }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out
                    break
            # if stock_found is not present:
            # return json.dumps({"error": f"SKU {sku} is missing in warehouse {warehouse_id}"}, indent=2)

        # Distribute stock and generate order
        total_cost = 0
        for order_item in items:
            sku = order_item["sku"]
            quantity = order_item["quantity"]
            for inv_item in inventory.values():
                if inv_item["warehouse_id"] == warehouse_id and inv_item["sku"] == sku:
                    inv_item["quantity_allocated"] += quantity
                    inv_item["quantity_available"] -= quantity
                    total_cost += inv_item.get("unit_cost", 0) * quantity
                    break

        if total_value is not None:
            total_cost = total_value

        new_order_id = f"ORD-{len(outbound_orders) + 1:04d}"
        new_order = {
            "order_id": new_order_id,
            "customer_name": customer_name,
            # "order_date": "2024-07-19", # Mimicking today's date
            "status": "Pending",
            "warehouse_id": warehouse_id,
            "items": items,
            "total_value": round(total_cost, 2),
            "currency": "USD",
            "shipping_address": shipping_address,
            "carrier_id": None,
            "tracking_number": None,
        }
        outbound_data["orders"][order_id] = new_order
        payload = new_order
        out = json.dumps(payload, indent=2)
        return out
        """Run the tool with the provided parameters."""
        pass
        outbound_orders = data.get("outbound_orders", {}).values()
        inventory = data.get("inventory", {}).values()

        #Verify stock for all items initially
        for order_item in items:
            sku = order_item["sku"]
            quantity = order_item["quantity"]
            for inv_item in inventory.values():
                if inv_item["warehouse_id"] == warehouse_id and inv_item["sku"] == sku:
                    if inv_item["quantity_available"] < quantity:
                        payload = {
                                "error": f"Insufficient stock for SKU {sku}. Available: {inv_item['quantity_available']}, Requested: {quantity}"
                            }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out
                    break
            #if stock_found is not present:
            #return json.dumps({"error": f"SKU {sku} is missing in warehouse {warehouse_id}"}, indent=2)

        #Distribute stock and generate order
        total_cost = 0
        for order_item in items:
            sku = order_item["sku"]
            quantity = order_item["quantity"]
            for inv_item in inventory.values():
                if inv_item["warehouse_id"] == warehouse_id and inv_item["sku"] == sku:
                    inv_item["quantity_allocated"] += quantity
                    inv_item["quantity_available"] -= quantity
                    total_cost += inv_item.get("unit_cost", 0) * quantity
                    break

        if total_value is not None:
            total_cost = total_value

        new_order_id = f"ORD-{len(outbound_orders) + 1:04d}"
        new_order = {
            "order_id": new_order_id,
            "customer_name": customer_name,
            #"order_date": "2024-07-19", # Mimicking today's date
            "status": "Pending",
            "warehouse_id": warehouse_id,
            "items": items,
            "total_value": round(total_cost, 2),
            "currency": "USD",
            "shipping_address": shipping_address,
            "carrier_id": None,
            "tracking_number": None,
        }
        outbound_data["orders"][order_id] = new_order
        payload = new_order
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide the tool's specifications for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateOutboundOrder",
                "description": "Creates a new outbound order for a customer, allocating stock from a specified warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_name": {
                            "type": "string",
                            "description": "The name of the customer.",
                        },
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the warehouse to fulfill the order from.",
                        },
                        "items": {
                            "type": "array",
                            "description": "A list of items to order.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {
                                        "type": "string",
                                        "description": "Product SKU.",
                                    },
                                    "quantity": {
                                        "type": "integer",
                                        "description": "Number of units to order.",
                                    },
                                },
                                "required": ["sku", "quantity"],
                            },
                        },
                        "shipping_address": {
                            "type": "string",
                            "description": "The customer's full shipping address.",
                        },
                        "total_value": {
                            "type": "integer",
                            "description": "The total value of the order",
                        },
                    },
                    "required": [
                        "customer_name",
                        "warehouse_id",
                        "items",
                        "shipping_address",
                    ],
                },
            },
        }
