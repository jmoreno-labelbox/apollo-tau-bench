from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class RequestOrderReturn(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str,
        order_id: str,
        return_items: list[dict[str, Any]] = None,
        return_reason: str = None,
        item_id: str = None,
        quantity: int = None,
        item_return_reason: str = None,
    ) -> str:
        """
        Request return for delivered order items (supports both single item and multiple items)

        Writes to: orders.json (adds return request to order)
        """
        # Rule: Validate user identity exists before processing any user requests
        users = data.get("users", [])
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            payload = {"error": f"User {user_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Validate input parameters - must provide either single item or return_items list
        if not return_items and not item_id:
            payload = {
                "error": "Either 'return_items' list or 'item_id' must be provided",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        if return_items and item_id:
            payload = {
                "error": "Cannot specify both 'return_items' and 'item_id'. Use one or the other.",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Build return items list from single item parameters if provided
        if item_id:
            if not return_reason and not item_return_reason:
                payload = {
                    "error": "Return reason must be provided when using 'item_id' parameter",
                    "status": "failed",
                }
                out = json.dumps(payload)
                return out

            return_items = [
                {
                    "item_id": item_id,
                    "quantity": quantity if quantity is not None else 1,
                    "reason": (
                        item_return_reason if item_return_reason else return_reason
                    ),
                }
            ]

            # Set overall return reason if not provided
            if not return_reason:
                return_reason = item_return_reason

        # Validate return_items structure
        if not return_items:
            payload = {"error": "Return items list cannot be empty", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Validate return_reason is provided
        if not return_reason:
            payload = {"error": "Return reason must be provided", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Find the order to process return for
        orders = data.get("orders", [])
        order_to_return = None
        order_index = None

        for i, order in enumerate(orders):
            if order.get("order_id") == order_id and order.get("user_id") == user_id:
                order_to_return = order
                order_index = i
                break

        if not order_to_return:
            payload = {
                "error": f"Order {order_id} not found or does not belong to user {user_id}",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        current_status = order_to_return.get("status")

        # Can only request returns for delivered orders
        if current_status != "delivered":
            payload = {
                "error": f"Returns can only be requested for delivered orders. Current status: {current_status}",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Validate return items exist in the original order
        order_items = order_to_return.get("items", [])
        valid_return_items = []
        total_return_amount = 0.0

        for return_item in return_items:
            item_id = return_item.get("item_id")
            return_quantity = return_item.get("quantity", 1)

            # Find the item in the original order
            original_item = None
            for order_item in order_items:
                if order_item.get("item_id") == item_id:
                    original_item = order_item
                    break

            if not original_item:
                payload = {
                    "error": f"Item {item_id} not found in original order {order_id}",
                    "status": "failed",
                }
                out = json.dumps(payload)
                return out

            if return_quantity <= 0:
                payload = {
                    "error": f"Return quantity must be greater than 0 for item {item_id}",
                    "status": "failed",
                }
                out = json.dumps(payload)
                return out

            # Calculate return amount
            item_price = original_item.get("price", 0)
            return_amount = item_price * return_quantity
            total_return_amount += return_amount

            valid_return_items.append(
                {
                    "item_id": item_id,
                    "product_name": original_item.get("name"),
                    "return_quantity": return_quantity,
                    "unit_price": item_price,
                    "return_amount": return_amount,
                    "return_reason": return_item.get("reason", return_reason),
                }
            )

        # Generate return request ID
        existing_returns = order_to_return.get("returns", [])
        return_number = len(existing_returns) + 1
        return_request_id = f"RET_{order_id}_{return_number}"

        # WRITE OPERATION: Add return request to order
        return_request = {
            "return_id": return_request_id,
            "requested_date": datetime.now().isoformat(),
            "return_status": "requested",
            "return_reason": return_reason,
            "return_items": valid_return_items,
            "total_return_amount": round(total_return_amount, 2),
            "requested_by": "customer",
        }

        if "returns" not in order_to_return:
            order_to_return["returns"] = []

        order_to_return["returns"].append(return_request)
        order_to_return["last_updated"] = datetime.now().isoformat()

        # Update the order in the data structure
        data["orders"][order_index] = order_to_return

        result = {
            "status": "success",
            "return_request_id": return_request_id,
            "order_id": order_id,
            "user_id": user_id,
            "return_details": {
                "total_items": len(valid_return_items),
                "return_items": valid_return_items,
                "total_return_amount": round(total_return_amount, 2),
                "return_reason": return_reason,
            },
            "return_status": "requested",
            "requested_date": return_request["requested_date"],
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RequestOrderReturn",
                "description": "Request return for items from a delivered order (supports both single item and multiple items)",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Customer identifier",
                        },
                        "order_id": {
                            "type": "string",
                            "description": "Order identifier for return",
                        },
                        "return_items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "item_id": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                    "reason": {"type": "string"},
                                },
                                "required": ["item_id", "quantity"],
                            },
                            "description": "List of items to return (optional if using single item parameters)",
                        },
                        "return_reason": {
                            "type": "string",
                            "description": "Overall reason for return (required for multiple items, optional for single item if item_return_reason provided)",
                        },
                        "item_id": {
                            "type": "string",
                            "description": "Single item identifier to return (optional if using return_items list)",
                        },
                        "quantity": {
                            "type": "integer",
                            "description": "Quantity of single item to return (optional, defaults to 1)",
                        },
                        "item_return_reason": {
                            "type": "string",
                            "description": "Reason for single item return (optional if return_reason provided)",
                        },
                    },
                    "required": ["user_id", "order_id"],
},
            },
        }
