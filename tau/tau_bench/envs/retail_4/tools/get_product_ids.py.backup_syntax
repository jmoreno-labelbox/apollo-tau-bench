from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetProductIds:
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str,
        order_ids: list[str],
        product_type: list[str] = None,
    ) -> str:
        """
        Get list of product IDs from specified orders for a user, optionally filtered by product type

        Data Sources: orders.json (order items), users.json (user validation), products.json (product names)
        """
        # Rule: Validate user identity exists before processing any user requests
        users = data.get("users", {}).values()
        user = next((u for u in users.values() if u.get("user_id") == user_id), None)

        if not user:
            payload = {"error": f"User {user_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        if not order_ids:
            payload = {"error": "Order IDs list cannot be empty", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Find all specified orders for the user
        orders = data.get("orders", {}).values()
        found_orders = []
        not_found_orders = []

        for order_id in order_ids:
            # Add # prefix if not provided (for convenience)
            formatted_order_id = (
                order_id if order_id.startswith("#") else f"#{order_id}"
            )

            order_found = False
            for order in orders.values()):
                if (
                    order.get("order_id") == formatted_order_id
                    and order.get("user_id") == user_id
                ):
                    found_data["orders"][order_id] = order
                    order_found = True
                    break

            if not order_found:
                not_found_data["orders"][order_id] = formatted_order_id

        if not found_orders:
            payload = {
                "error": f"No valid orders found for user {user_id}",
                "not_found_orders": not_found_orders,
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Get product information for filtering
        products = data.get("products", {}).values()
        product_name_map = {}
        for product in products.values():
            product_id = product.get("product_id")
            product_name = product.get("name", "").lower()
            if product_id:
                product_name_map[product_id] = product_name

        # Convert product_type to lowercase for case-insensitive matching
        product_type_lower = []
        if product_type:
            product_type_lower = [ptype.lower() for ptype in product_type]

        # Extract product IDs from all found orders with optional filtering
        product_id_set = set()
        order_details = []
        filtered_items = 0
        total_items = 0

        for order in found_orders:
            order_items = order.get("items", [])
            order_product_ids = []
            order_filtered_product_ids = []

            for item in order_items:
                product_id = item.get("product_id")
                total_items += 1

                if product_id:
                    order_product_ids.append(product_id)

                    # Check if product matches the type filter (if provided)
                    if product_type_lower:
                        product_name = product_name_map.get(product_id, "")
                        type_matches = any(
                            ptype in product_name for ptype in product_type_lower
                        )

                        if type_matches:
                            product_id_set.add(product_id)
                            order_filtered_product_ids.append(product_id)
                            filtered_items += 1
                    else:
                        # No filter, include all products
                        product_id_set.add(product_id)
                        order_filtered_product_ids.append(product_id)

            order_details.append(
                {
                    "order_id": order.get("order_id"),
                    "order_status": order.get("status"),
                    "all_product_ids": order_product_ids,
                    "filtered_product_ids": (
                        order_filtered_product_ids
                        if product_type
                        else order_product_ids
                    ),
                    "total_items": len(order_items),
                    "filtered_items": (
                        len(order_filtered_product_ids)
                        if product_type
                        else len(order_items)
                    ),
                    "order_date": order.get("timestamp"),
                }
            )

        # Convert set back to list and sort for consistent output
        unique_product_ids = sorted(list(product_id_set))

        result = {
            "status": "success",
            "user_id": user_id,
            "search_criteria": {
                "requested_orders": len(order_ids),
                "product_type_filter": product_type,
                "filter_applied": product_type is not None,
            },
            "found_orders": len(found_orders),
            "not_found_orders": not_found_orders if not_found_orders else [],
            "filtering_summary": {
                "total_items_in_orders": total_items,
                "items_matching_filter": (
                    filtered_items if product_type else total_items
                ),
                "filter_efficiency_percent": (
                    round((filtered_items / total_items * 100), 1)
                    if total_items > 0 and product_type
                    else 100
                ),
            },
            "product_ids": {
                "unique_product_ids": unique_product_ids,
                "total_unique_products": len(unique_product_ids),
            },
            "order_details": order_details,
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductIds",
                "description": "Get list of product IDs from specified orders for a user, optionally filtered by product type",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Customer identifier",
                        },
                        "order_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of order identifiers (e.g., ['W6893533', '#W6893534'])",
                        },
                        "product_type": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional list of product types to filter by (e.g., ['laptop', 'bluetooth speaker', 't-shirt']). Matches product names containing these terms.",
                        },
                    },
                    "required": ["user_id", "order_ids"],
                },
            },
        }
