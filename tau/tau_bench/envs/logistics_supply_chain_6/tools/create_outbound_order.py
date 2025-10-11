# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateOutboundOrder(Tool):
    """Tool to create a new outbound customer order."""

    @staticmethod
    def invoke(data: Dict[str, Any], customer_name: str, warehouse_id: str, items: List[Dict[str, Any]], shipping_address: str, total_value: Optional[int] = None) -> str:
        """Execute the tool with given parameters."""
        outbound_orders = data.get("outbound_orders", [])
        inventory = list(data.get("inventory", {}).values())

        # Verify inventory for all products initially.
        for order_item in items:
            sku = order_item["sku"]
            quantity = order_item["quantity"]
            stock_found = False
            for inv_item in inventory:
                if inv_item["warehouse_id"] == warehouse_id and inv_item["sku"] == sku:
                    if inv_item["quantity_available"] < quantity:
                        return json.dumps({"error": f"Insufficient stock for SKU {sku}. Available: {inv_item['quantity_available']}, Requested: {quantity}"}, indent=2)
                    stock_found = True
                    break
            # if stock_not_found:
            # return json.dumps({"error": f"SKU {sku} is missing in warehouse {warehouse_id}"}, indent=2)

        # Assign inventory and generate order.
        total_cost = 0
        for order_item in items:
            sku = order_item["sku"]
            quantity = order_item["quantity"]
            for inv_item in inventory:
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
            # "order_date": "2024-07-19", # "order_date": "2024-07-19", # Mocking today's date
            "status": "Pending",
            "warehouse_id": warehouse_id,
            "items": items,
            "total_value": round(total_cost, 2),
            "currency": "USD",
            "shipping_address": shipping_address,
            "carrier_id": None,
            "tracking_number": None
        }
        outbound_orders.append(new_order)
        return json.dumps(new_order, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "create_outbound_order",
                "description": "Creates a new outbound order for a customer, allocating stock from a specified warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_name": {"type": "string", "description": "The name of the customer."},
                        "warehouse_id": {"type": "string", "description": "The ID of the warehouse to fulfill the order from."},
                        "items": {
                            "type": "array",
                            "description": "A list of items to order.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {"type": "string", "description": "Product SKU."},
                                    "quantity": {"type": "integer", "description": "Number of units to order."}
                                },
                                "required": ["sku", "quantity"]
                            }
                        },
                        "shipping_address": {"type": "string", "description": "The customer's full shipping address."},
                        "total_value": {"type": "integer", "description": "The total value of the order"}
                    },
                    "required": ["customer_name", "warehouse_id", "items", "shipping_address"],
                },
            },
        }
