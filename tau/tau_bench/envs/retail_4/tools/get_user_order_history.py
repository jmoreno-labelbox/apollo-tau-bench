# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserOrderHistory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, product_type: List[str] = None) -> str:
        """
        Retrieve customer order history and account summary, optionally filtered by product type

        Data Sources: users.json (user_id, orders, payment_methods, name, email, address), orders.json (order details), products.json (product names for filtering)
        """
        # Condition: Confirm user identity is present prior to handling any requests.
        users = list(data.get("users", {}).values())
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            return json.dumps({"error": f"User {user_id} not found", "status": "failed"})

        # Retrieve user data from the users.json format.
        user_orders = user.get("orders", [])
        payment_methods = user.get("payment_methods", {})
        user_name = user.get("name", {})
        user_address = user.get("address", {})

        # Retrieve comprehensive order details when a product_type filter is applied.
        filtered_orders = user_orders
        filter_applied = False

        if product_type:
            # Transform product_type to lowercase for uniform matching regardless of case.
            product_type_lower = [ptype.lower() for ptype in product_type]
            filter_applied = True

            # Retrieve product details for filtering purposes.
            products = list(data.get("products", {}).values())
            product_name_map = {}
            for product in products:
                product_id = product.get("product_id")
                product_name = product.get("name", "").lower()
                if product_id:
                    product_name_map[product_id] = product_name

            # Retrieve order information for filtering based on product type.
            orders = list(data.get("orders", {}).values())
            filtered_orders = []

            for order_id in user_orders:
                # Retrieve the order information.
                order_details = None
                for order in orders:
                    if order.get("order_id") == order_id and order.get("user_id") == user_id:
                        order_details = order
                        break

                if order_details:
                    order_items = order_details.get("items", [])
                    order_has_matching_products = False

                    # Verify if any item in the order corresponds to the product type filter.
                    for item in order_items:
                        item_product_id = item.get("product_id")
                        if item_product_id:
                            product_name = product_name_map.get(item_product_id, "")
                            if product_name:
                                type_matches = any(
                                    ptype in product_name
                                    for ptype in product_type_lower
                                )
                                if type_matches:
                                    order_has_matching_products = True
                                    break

                    # Add the order if corresponding products are present.
                    if order_has_matching_products:
                        filtered_orders.append(order_id)

        # Requirement: Accepted payment methods include credit_card, paypal, or gift_card.
        valid_payment_methods = []
        for method_id, method_details in payment_methods.items():
            payment_source = method_details.get("source")
            if payment_source in ["credit_card", "paypal", "gift_card"]:
                method_info = {
                    "id": method_id,
                    "source": payment_source
                }

                # Incorporate details tailored to the payment method.
                if payment_source == "credit_card":
                    method_info["brand"] = method_details.get("brand")
                    method_info["last_four"] = method_details.get("last_four")
                elif payment_source == "gift_card":
                    method_info["balance"] = method_details.get("balance", 0)

                valid_payment_methods.append(method_info)

        # Validation is required for all mandatory address fields: address1, city, country, state, and zip.
        address_complete = all(user_address.get(field) for field in ["address1", "city", "country", "state", "zip"])

        # Retrieve comprehensive data on filtered orders, including those with and without a product type filter.
        order_details_summary = []
        orders = list(data.get("orders", {}).values())

        # Retrieve product details for item_ids mapping
        products = list(data.get("products", {}).values())
        product_name_map = {}
        for product in products:
            product_id = product.get("product_id")
            product_name = product.get("name", "").lower()
            if product_id:
                product_name_map[product_id] = product_name

        for order_id in filtered_orders:
            for order in orders:
                if order.get("order_id") == order_id and order.get("user_id") == user_id:
                    if filter_applied and product_type:
                        # Retrieve products that match in this sequence (filtered case)
                        matching_products = []
                        order_items = order.get("items", [])

                        for item in order_items:
                            item_product_id = item.get("product_id")
                            if item_product_id:
                                product_name = product_name_map.get(item_product_id, "")
                                if product_name:
                                    type_matches = any(
                                        ptype in product_name
                                        for ptype in product_type_lower
                                    )
                                    if type_matches:
                                        matching_products.append({
                                            "product_id": item_product_id,
                                            "product_name": item.get("name"),
                                            "item_id": item.get("item_id"),
                                            "quantity": item.get("quantity", 1),
                                            "price": item.get("price", 0)
                                        })

                        if matching_products:
                            order_details_summary.append({
                                "order_id": order_id,
                                "order_status": order.get("status"),
                                "order_date": order.get("timestamp"),
                                "matching_products": matching_products,
                                "total_matching_items": len(matching_products)
                            })
                    else:
                        # Retrieve all products in this sequence (without any filter applied).
                        all_products = []
                        order_items = order.get("items", [])

                        for item in order_items:
                            all_products.append({
                                "product_id": item.get("product_id"),
                                "product_name": item.get("name"),
                                "item_id": item.get("item_id"),
                                "quantity": item.get("quantity", 1),
                                "price": item.get("price", 0)
                            })

                        order_details_summary.append({
                            "order_id": order_id,
                            "order_status": order.get("status"),
                            "order_date": order.get("timestamp"),
                            "all_products": all_products,
                            "total_items": len(all_products)
                        })
                    break

        result = {
            "status": "success",
            "user_id": user_id,
            "customer_info": {
                "name": f"{user_name.get('first_name', '')} {user_name.get('last_name', '')}".strip(),
                "email": user.get("email"),
                "address_complete": address_complete,
                "address": user_address
            },
            "filter_info": {
                "product_type_filter": product_type,
                "filter_applied": filter_applied,
                "original_order_count": len(user_orders),
                "filtered_order_count": len(filtered_orders)
            },
            "order_history": {
                "total_orders": len(filtered_orders),
                "order_ids": filtered_orders,
                "order_details": order_details_summary
            },
            "payment_methods": {
                "total_methods": len(valid_payment_methods),
                "methods": valid_payment_methods
            }
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_order_history",
                "description": "Retrieve customer order history and account information with detailed product and item information, optionally filtered by product type",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Customer identifier"},
                        "product_type": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional list of product types to filter orders by (e.g., ['laptop', 'smartphone', 't-shirt']). Only returns orders containing products whose names contain these terms."
                        }
                    },
                    "required": ["user_id"]
                }
            }
        }
