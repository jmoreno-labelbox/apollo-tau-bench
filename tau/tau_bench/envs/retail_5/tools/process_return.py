from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class ProcessReturn(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, item_ids: list = None, reason: str = None) -> str:
        if not all([order_id, item_ids, reason]):
            payload = {"error": "order_id, item_ids, and reason are required"}
            out = json.dumps(payload)
            return out

        orders = data["orders"]
        suppliers = data["suppliers"]
        products = data["products"]
        order = next((o for o in orders.values() if o["order_id"] == order_id), None)

        if not order:
            payload = {"error": "Order not found"}
            out = json.dumps(payload)
            return out

        if order["status"] not in ["delivered", "completed", "processed"]:
            payload = {
                    "error": f'Returns not allowed for orders with status: {order["status"]}'
                }
            out = json.dumps(
                payload)
            return out

        return_items = []
        refund_amount = 0.0

        for item_to_return_id in item_ids:
            item_in_order = next(
                (i for i in order["items"] if i["item_id"] == item_to_return_id), None
            )
            if item_in_order:
                return_items.append(item_in_order)
                refund_amount += item_in_order["price"]

                #Replenish inventory
                product_for_item = next(
                    (
                        p
                        for p in products
                        if p["product_id"] == item_in_order["product_id"]
                    ),
                    None,
                )
                if product_for_item:
                    supplier_for_product = next(
                        (
                            s
                            for s in suppliers
                            if s["supplier_id"] == product_for_item["supplier_id"]
                        ),
                        None,
                    )
                    if (
                        supplier_for_product
                        and item_to_return_id in supplier_for_product["item_stock"]
                    ):
                        current_stock = supplier_for_product["item_stock"][
                            item_to_return_id
                        ]
                        if isinstance(current_stock, int):
                            supplier_for_product["item_stock"][item_to_return_id] = (
                                current_stock + 1
                            )  #Presuming the quantity is 1

        if not return_items:
            payload = {"error": "No matching items found in order for return"}
            out = json.dumps(payload)
            return out

        #Record the refund transaction
        refund_transaction = {
            "transaction_type": "refund",
            "amount": -refund_amount,
            "reason": reason,
            "timestamp": get_current_timestamp(),
        }
        if "payment_history" not in order:
            order["payment_history"] = []
        order["payment_history"].append(refund_transaction)

        #Modify order status to indicate return
        order["status"] = (
            "partially_returned"
            if len(order["items"]) > len(return_items)
            else "returned"
        )
        payload = {
                "success": True,
                "order_id": order_id,
                "returned_items_count": len(return_items),
                "refund_amount": refund_amount,
                "new_order_status": order["status"],
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "processReturn",
                "description": "Process a return for specific items from an order, logs the refund, and restock inventory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Order ID to process return for",
                        },
                        "item_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of item IDs to return",
                        },
                        "reason": {
                            "type": "string",
                            "description": "Reason for return",
                        },
                    },
                    "required": ["order_id", "item_ids", "reason"],
                },
            },
        }
