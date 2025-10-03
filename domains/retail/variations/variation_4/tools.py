import json
from datetime import datetime
from typing import Any

from domains.dto import Tool


class ProcessPayment(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        user_id: str, 
        payment_method_source: str, 
        amount: float
    ) -> str:
        """
        Process payment for a customer order following retail rules validation
        """
        # Rule: Validate user identity exists before processing any user requests
        users = data.get("users", [])
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            payload = {"error": f"User {user_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Rule: Payment methods must be valid type: credit_card, paypal, or gift_card with sufficient balance
        payment_methods = user.get("payment_methods", {})
        pay_keys = list(payment_methods.keys())
        payment_method = None
        for key in pay_keys:
            if payment_method_source in key:
                payment_method = payment_methods[key]

        if not payment_method:
            payload = {
                "error": f"Payment method {payment_method_source} not found for user",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        payment_source = payment_method.get("source")
        if payment_source not in ["credit_card", "paypal", "gift_card"]:
            payload = {
                "error": f"Invalid payment method type: {payment_source}",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Rule: Gift card payments cannot exceed available balance - verify balance sufficiency before processing
        if payment_source == "gift_card":
            available_balance = payment_method.get("balance", 0)
            if amount > available_balance:
                print(
                    f"Insufficient gift card balance: {available_balance} for amount: {amount}"
                )
                payload = {
                    "error": f"Insufficient gift card balance. Available: ${available_balance}, Required: ${amount}",
                    "status": "failed",
                }
                out = json.dumps(payload)
                return out

        # Rule: Credit card payments must validate last_four digits and brand type match user's stored payment methods
        if payment_source == "credit_card":
            brand = payment_method.get("brand")
            last_four = payment_method.get("last_four")
            if not brand or not last_four:
                payload = {"error": "Invalid credit card information", "status": "failed"}
                out = json.dumps(payload)
                return out

        # Rule: High-value orders (>$1000 total) require payment verification before fulfillment
        verification_required = amount > 1000.0

        # Process payment successfully
        result = {
            "status": "success",
            "user_id": user_id,
            "payment_method_id": payment_method_source,
            "payment_source": payment_source,
            "amount": amount,
            "verification_required": verification_required,
            "transaction_id": f"TXN_{user_id}_{payment_method_source}_{int(amount)}",
        }

        # Add specific details based on payment type
        if payment_source == "gift_card":
            new_balance = payment_method.get("balance", 0) - amount
            result["remaining_gift_card_balance"] = new_balance
        elif payment_source == "credit_card":
            result["card_brand"] = payment_method.get("brand")
            result["card_last_four"] = payment_method.get("last_four")
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ProcessPayment",
                "description": "Process customer payment with validation according to retail business rules",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Customer identifier",
                        },
                        "payment_method_source": {
                            "type": "string",
                            "description": "Payment method identifier from customer's stored methods",
                        },
                        "amount": {
                            "type": "number",
                            "description": "Payment amount in dollars",
                        },
                    },
                    "required": ["user_id", "payment_method_source", "amount"],
                },
            },
        }


class AllocateInventory(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        item_id: str = None,
        item_ids: list[str] = None,
        quantity: int = 1,
    ) -> str:
        """
        Allocate inventory for order fulfillment with availability validation
        Supports both single item and batch processing with multiple items
        """
        # Validate input parameters
        if not item_id and not item_ids:
            payload = {
                "error": "Either item_id or item_ids must be provided",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        if item_id and item_ids:
            payload = {
                "error": "Cannot specify both item_id and item_ids. Use one or the other.",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Build list of items to process
        items_to_process = []
        if item_id:
            items_to_process.append(item_id)
        if item_ids:
            items_to_process.extend(item_ids)

        # Remove duplicates while preserving order
        items_to_process = list(dict.fromkeys(items_to_process))

        if not items_to_process:
            payload = {"error": "No valid item IDs provided", "status": "failed"}
            out = json.dumps(payload)
            return out

        if quantity <= 0:
            payload = {"error": "Quantity must be greater than 0", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Rule: Confirm item_id exists in product variants before including in orders
        products = data.get("products", [])
        allocation_results = []
        successful_allocations = []
        failed_allocations = []
        total_allocation_value = 0.0

        for current_item_id in items_to_process:
            product_found = None
            variant_found = None

            for product in products:
                variants = product.get("variants", {})
                if current_item_id in variants:
                    product_found = product
                    variant_found = variants[current_item_id]
                    break

            if not variant_found:
                failed_allocations.append(
                    {
                        "item_id": current_item_id,
                        "error": f"Item {current_item_id} not found in product catalog",
                        "status": "failed",
                    }
                )
                continue

            # Rule: Check product availability status before allocation - never allocate unavailable items
            is_available = variant_found.get("available", False)
            if not is_available:
                failed_allocations.append(
                    {
                        "item_id": current_item_id,
                        "error": f"Item {current_item_id} is not available for allocation",
                        "status": "failed",
                    }
                )
                continue

            # Rule: Use exact variant pricing from product catalog - no unauthorized price modifications
            unit_price = variant_found.get("price", 0)
            total_price = unit_price * quantity

            allocation_result = {
                "item_id": current_item_id,
                "product_name": product_found.get("name"),
                "product_id": product_found.get("product_id"),
                "quantity_allocated": quantity,
                "unit_price": unit_price,
                "total_price": total_price,
                "variant_options": variant_found.get("options", {}),
                "status": "success",
            }

            allocation_results.append(allocation_result)
            successful_allocations.append(allocation_result)
            total_allocation_value += total_price

        # Determine overall status
        overall_status = "success" if successful_allocations else "failed"
        if successful_allocations and failed_allocations:
            overall_status = "partial_success"

        result = {
            "status": overall_status,
            "batch_processing": len(items_to_process) > 1,
            "allocation_summary": {
                "total_items_processed": len(items_to_process),
                "successful_allocations": len(successful_allocations),
                "failed_allocations": len(failed_allocations),
                "total_allocation_value": round(total_allocation_value, 2),
                "quantity_per_item": quantity,
            },
            "successful_allocations": successful_allocations,
            "failed_allocations": failed_allocations,
            "allocation_details": allocation_results,
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AllocateInventory",
                "description": "Allocate inventory items for order fulfillment with availability checking. Supports both single item and batch processing with multiple items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {
                            "type": "string",
                            "description": "Single product variant identifier (cannot be used with item_ids)",
                        },
                        "item_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Array of product variant identifiers for batch processing (cannot be used with item_id)",
                        },
                        "quantity": {
                            "type": "integer",
                            "description": "Quantity to allocate for each item (applies to all items in batch processing)",
                            "default": 1,
                        },
                    },
                    "anyOf": [{"required": ["item_id"]}, {"required": ["item_ids"]}],
                },
            },
        }


class AssignCourier(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        destination_country: str,
        order_value: float = None,
        order_values: list[float] = None,
        location: dict[str, str] = None,
        tracking_ids: list[str] = None,
        courier_id: str = None,
        order_id: Any = None,
    ) -> str:
        """
        Assign appropriate courier for order delivery based on coverage and requirements
        Supports both single order value and multiple order values for batch processing
        Uses a single tracking ID for all scenarios (single order or multiple orders)

        Data Sources: couriers.json (courier_id, name, coverage_area, contact_info)
        """
        # Validate input parameters
        if order_value is not None and order_values is not None:
            payload = {
                "error": "Cannot specify both order_value and order_values. Use one or the other.",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        if order_value is None and order_values is None:
            payload = {
                "error": "Either order_value or order_values must be provided",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Validate tracking_ids parameter if provided
        if tracking_ids is not None:
            # For single tracking ID mode, accept either single tracking ID or require all to be the same
            if len(tracking_ids) == 1:
                # Single tracking ID for all orders - this is what we want
                single_tracking_id = tracking_ids[0]
            elif len(tracking_ids) > 1:
                # Check if all tracking IDs are the same
                if len(set(tracking_ids)) == 1:
                    single_tracking_id = tracking_ids[0]
                else:
                    payload = {
                        "error": "For single tracking ID mode, all tracking_ids must be the same or provide only one tracking_id",
                        "status": "failed",
                    }
                    out = json.dumps(payload)
                    return out
            else:
                payload = {
                    "error": "tracking_ids cannot be empty if provided",
                    "status": "failed",
                }
                out = json.dumps(payload)
                return out

        # Build list of order values to process
        values_to_process = []
        if order_value is not None:
            if order_value < 0:
                payload = {"error": "Order value cannot be negative", "status": "failed"}
                out = json.dumps(payload)
                return out
            values_to_process.append(order_value)

        if order_values is not None:
            if not order_values:
                payload = {"error": "Order values list cannot be empty", "status": "failed"}
                out = json.dumps(payload)
                return out
            for i, value in enumerate(order_values):
                if not isinstance(value, (int, float)) or value < 0:
                    payload = {
                        "error": f"Order value at index {i} must be a non-negative number: {value}",
                        "status": "failed",
                    }
                    out = json.dumps(payload)
                    return out
            values_to_process = order_values

        # Rule: Assign couriers only if destination country matches their coverage areas
        couriers = data.get("couriers", [])
        eligible_couriers = []

        for courier in couriers:
            coverage_area = courier.get("coverage_area", [])
            if destination_country in coverage_area:
                eligible_couriers.append(courier)

        if not eligible_couriers:
            payload = {
                "error": f"No couriers available for destination country: {destination_country}",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Select courier based on preference or use automatic selection
        selected_courier = eligible_couriers[0]  # Simple selection logic
        if courier_id is not None:
            selected_courier = next(
                (c for c in eligible_couriers if c.get("courier_id") == courier_id),
                selected_courier,
            )

        # Get courier's tracking pool for fallback generation
        tracking_ids_pool = selected_courier.get("tracking_ids", [])

        # Process location information if provided
        delivery_location = None
        if location:
            # Validate location has required fields
            required_location_fields = ["city", "country"]
            missing_fields = [
                field for field in required_location_fields if not location.get(field)
            ]

            if missing_fields:
                payload = {
                    "error": f"Location missing required fields: {', '.join(missing_fields)}",
                    "status": "failed",
                }
                out = json.dumps(payload)
                return out

            delivery_location = {
                "address1": location.get("address1", ""),
                "address2": location.get("address2", ""),
                "city": location.get("city"),
                "state": location.get("state", ""),
                "zip": location.get("zip", ""),
                "country": location.get("country"),
            }

            # Verify location country matches destination_country parameter
            if delivery_location["country"] != destination_country:
                payload = {
                    "error": f"Location country '{delivery_location['country']}' does not match destination_country '{destination_country}'",
                    "status": "failed",
                }
                out = json.dumps(payload)
                return out

        # Generate single tracking ID for all orders (whether single or multiple)
        batch_mode = len(values_to_process) > 1

        if tracking_ids is not None:
            # Use the provided single tracking ID
            assigned_tracking_id = single_tracking_id
            tracking_source = "custom_provided"
        else:
            # Generate single tracking ID
            if batch_mode:
                # For multiple orders, create a batch tracking ID
                batch_identifier = f"BATCH{len(values_to_process):02d}"
                courier_code = (
                    selected_courier.get("courier_id", "")
                    .replace("#", "")
                    .replace("COU", "C")
                )
                assigned_tracking_id = f"TRK{batch_identifier}{courier_code}"
            else:
                # For single order, use standard generation with single tracking
                base_tracking_id = (
                    tracking_ids_pool[0] if tracking_ids_pool else "TRK001"
                )
                total_value = values_to_process[0]
                assigned_tracking_id = f"{base_tracking_id}-{total_value}"
            tracking_source = "courier_pool_generated"

        # Process each order value with the same tracking ID
        courier_assignments = []
        total_order_value = sum(values_to_process)
        high_value_orders = 0

        for i, current_order_value in enumerate(values_to_process):
            # Rule: High-value orders (>$1000 total) require payment verification before fulfillment
            requires_insurance = current_order_value > 1000.0
            if requires_insurance:
                high_value_orders += 1

            courier_assignments.append(
                {
                    "order_index": i + 1 if batch_mode else None,
                    "order_value": current_order_value,
                    "assigned_tracking_id": assigned_tracking_id,  # Same tracking ID for all
                    "tracking_source": tracking_source,
                    "requires_insurance": requires_insurance,
                }
            )

        # Calculate batch metrics
        batch_metrics = {
            "total_orders": len(values_to_process),
            "total_order_value": round(total_order_value, 2),
            "high_value_orders": high_value_orders,
            "average_order_value": round(total_order_value / len(values_to_process), 2),
            "min_order_value": min(values_to_process),
            "max_order_value": max(values_to_process),
            "single_tracking_id_used": True,
            "tracking_id_sharing": True,  # Always true now since we always use single tracking
        }

        result = {
            "status": "success",
            "batch_processing": batch_mode,
            "courier_assignment": {
                "courier_id": selected_courier.get("courier_id"),
                "courier_name": selected_courier.get("name"),
                "contact_info": selected_courier.get("contact_info"),
                "destination_country": destination_country,
                "delivery_location": delivery_location,
            },
            "tracking_configuration": {
                "single_tracking_id": assigned_tracking_id,
                "shared_across_orders": True,  # Always true now
                "tracking_source": tracking_source,
                "custom_tracking_provided": tracking_ids is not None,
                "courier_tracking_pool_size": len(tracking_ids_pool),
            },
            "batch_metrics": batch_metrics,
            "order_assignments": courier_assignments,
            "processing_summary": {
                "total_assignments": len(courier_assignments),
                "high_value_assignments": high_value_orders,
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
                "name": "AssignCourier",
                "description": "Assign courier for order delivery based on destination and order requirements. Supports both single order value and batch processing with multiple order values. Always uses a single tracking ID for all orders (whether single or multiple).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "destination_country": {
                            "type": "string",
                            "description": "Destination country for delivery",
                        },
                        "order_value": {
                            "type": "number",
                            "description": "Single order value in dollars. Cannot be used with order_values. Uses single tracking ID.",
                        },
                        "order_values": {
                            "type": "array",
                            "items": {"type": "number"},
                            "description": "Array of order values in dollars for batch processing. Cannot be used with order_value. All orders will share a single tracking ID.",
                        },
                        "location": {
                            "type": "object",
                            "properties": {
                                "address1": {
                                    "type": "string",
                                    "description": "Primary street address",
                                },
                                "address2": {
                                    "type": "string",
                                    "description": "Secondary address line (apartment, suite, etc.)",
                                },
                                "city": {"type": "string", "description": "City name"},
                                "state": {
                                    "type": "string",
                                    "description": "State or province",
                                },
                                "zip": {
                                    "type": "string",
                                    "description": "ZIP or postal code",
                                },
                                "country": {
                                    "type": "string",
                                    "description": "Country name",
                                },
                            },
                            "required": ["city", "country"],
                            "description": "Optional detailed delivery address information",
                        },
                        "tracking_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional single tracking ID for all orders. Provide either one tracking ID (which will be used for all orders) or the same tracking ID repeated. Can be used with both single order and multiple orders.",
                        },
                        "courier_id": {
                            "type": "string",
                            "description": "Optional specific courier ID to assign, if known",
                        },
                    },
                    "required": ["destination_country"],
                    "anyOf": [
                        {"required": ["order_value"]},
                        {"required": ["order_values"]},
                    ],
                },
            },
        }


class ValidateOrderItems(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], item_list: list[dict[str, Any]], allocate_orders: bool = False) -> str:
        """
        Validate all items in an order before processing
        """
        products = data.get("products", [])
        validated_items = []
        total_order_value = 0.0

        # Rule: Multi-item orders need all items available before confirmation
        for item in item_list:
            item_id = item.get("item_id")
            quantity = item.get("quantity", 1)

            # Rule: Confirm item_id exists in product variants before including in orders
            variant_found = None
            product_found = None

            for product in products:
                variants = product.get("variants", {})
                if item_id in variants:
                    variant_found = variants[item_id]
                    product_found = product
                    break

            if not variant_found:
                payload = {
                    "error": f"Item {item_id} not found in catalog",
                    "status": "failed",
                }
                out = json.dumps(payload)
                return out

            # Rule: Check product availability status before allocation - never allocate unavailable items
            if allocate_orders:
                if not variant_found.get("available", False):
                    print(
                        f"Item {item_id} ({product_found.get('name')}) is not available"
                    )
                    payload = {
                        "error": f"Item {item_id} ({product_found.get('name')}) is not available",
                        "status": "failed",
                    }
                    out = json.dumps(payload)
                    return out

            # Rule: Use exact variant pricing from product catalog - no unauthorized price modifications
            unit_price = variant_found.get("price", 0)
            item_total = unit_price * quantity
            total_order_value += item_total

            validated_items.append(
                {
                    "item_id": item_id,
                    "product_name": product_found.get("name"),
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "item_total": item_total,
                    "options": variant_found.get("options", {}),
                    "availability": variant_found.get("available", False),
                }
            )

        # Rule: Maintain data integrity: order totals must match sum of item prices
        result = {
            "status": "success",
            "validated_items": validated_items,
            "total_items": len(validated_items),
            "total_order_value": total_order_value,
            "requires_verification": total_order_value > 1000.0,
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ValidateOrderItems",
                "description": "Validate all items in order for availability and pricing before processing",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_list": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "item_id": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                },
                                "required": ["item_id", "quantity"],
                            },
                            "description": "List of items to validate",
                        },
                        "allocate_orders": {
                            "type": "boolean",
                            "default": False,
                            "description": "Flag to indicate if items should be allocated for orders",
                        },
                    },
                    "required": ["item_list"],
                },
            },
        }


class ValidateShippingAddress(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        user_id: str, 
        custom_address: dict[str, str] = None
    ) -> str:
        """
        Validate shipping address for order fulfillment
        """
        # Rule: Validate user identity exists before processing any user requests
        users = data.get("users", [])
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            payload = {"error": f"User {user_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Use custom address if provided, otherwise use user's stored address
        address = custom_address if custom_address else user.get("address", {})

        # Rule: Validate all required address fields: address1, city, country, state, zip
        required_fields = ["address1", "city", "country", "state", "zip"]
        missing_fields = []

        for field in required_fields:
            if not address.get(field):
                missing_fields.append(field)

        if missing_fields:
            payload = {
                "error": f"Missing required address fields: {', '.join(missing_fields)}",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Additional validation for supported countries
        couriers = data.get("couriers", [])
        supported_countries = set()
        for courier in couriers:
            supported_countries.update(courier.get("coverage_area", []))

        destination_country = address.get("country")
        if destination_country not in supported_countries:
            payload = {
                "error": f"No delivery service available to {destination_country}",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        result = {
            "status": "success",
            "user_id": user_id,
            "validated_address": address,
            "destination_country": destination_country,
            "delivery_available": True,
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ValidateShippingAddress",
                "description": "Validate shipping address completeness and delivery availability",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Customer identifier",
                        },
                        "custom_address": {
                            "type": "object",
                            "properties": {
                                "address1": {"type": "string"},
                                "address2": {"type": "string"},
                                "city": {"type": "string"},
                                "country": {"type": "string"},
                                "state": {"type": "string"},
                                "zip": {"type": "string"},
                            },
                            "description": "Optional custom shipping address, uses user's stored address if not provided",
                        },
                    },
                    "required": ["user_id"],
                },
            },
        }


class CheckSupplyOrderStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], product_id: str) -> str:
        """
        Check supply order status for inventory replenishment planning
        """
        # Rule: Supply orders must reference valid supplier_id and existing product_id
        supply_orders = data.get("supply_orders", [])
        product_supply_orders = [
            so for so in supply_orders if so.get("product_id") == product_id
        ]

        if not product_supply_orders:
            payload = {
                "error": f"No supply orders found for product {product_id}",
                "status": "not_found",
            }
            out = json.dumps(payload)
            return out

        # Rule: Supply orders with status 'cancelled' require alternative sourcing and cannot be fulfilled
        active_orders = []
        cancelled_orders = []
        fulfilled_orders = []

        for order in product_supply_orders:
            status = order.get("status")
            if status == "cancelled":
                cancelled_orders.append(order)
            elif status == "fulfilled":
                fulfilled_orders.append(order)
            elif status == "pending":
                active_orders.append(order)

        # Calculate totals
        total_pending_quantity = sum(
            order.get("quantity", 0) for order in active_orders
        )
        total_fulfilled_quantity = sum(
            order.get("quantity", 0) for order in fulfilled_orders
        )
        total_cancelled_quantity = sum(
            order.get("quantity", 0) for order in cancelled_orders
        )

        result = {
            "status": "success",
            "product_id": product_id,
            "total_supply_orders": len(product_supply_orders),
            "pending_orders": len(active_orders),
            "fulfilled_orders": len(fulfilled_orders),
            "cancelled_orders": len(cancelled_orders),
            "pending_quantity": total_pending_quantity,
            "fulfilled_quantity": total_fulfilled_quantity,
            "cancelled_quantity": total_cancelled_quantity,
            "requires_alternative_sourcing": len(cancelled_orders) > 0,
            "recent_orders": (
                product_supply_orders[-3:]
                if len(product_supply_orders) >= 3
                else product_supply_orders
            ),
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckSupplyOrderStatus",
                "description": "Check supply order status and inventory replenishment for a product",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {
                            "type": "string",
                            "description": "Product identifier to check supply orders for",
                        }
                    },
                    "required": ["product_id"],
                },
            },
        }


class SearchProductsByFilter(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        category: str = None,
        min_price: float = None,
        max_price: float = None,
        available_only: bool = True,
        options: dict[str, Any] = None,
        show_all: bool = False,
        limit: int = None,
        price_flag: str = None,
    ) -> str:
        """
        Search products by category, price range, and availability status

        Data Sources: products.json (product_id, name, variants with price/available fields)
        """
        _categoryL = (category or '').lower()
        products = data.get("products", [])
        matching_products = []

        # Rule: Check product availability status before allocation - never allocate unavailable items
        for product in products:
            product_name = product.get("name", "").lower()
            product_id = product.get("product_id")
            variants = product.get("variants", {})

            # Filter by category if specified
            if category and category.lower() not in product_name:
                continue

            # Check variants for price and availability filtering
            valid_variants = []
            for variant_id, variant in variants.items():
                variant_price = variant.get("price", 0)
                variant_available = variant.get("available", False)
                variant_options = variant.get("options", {})

                # Rule: Check product availability status before allocation
                if not show_all:
                    if available_only and not variant_available:
                        continue

                # Apply price filters
                if min_price is not None and variant_price < min_price:
                    continue
                if max_price is not None and variant_price > max_price:
                    continue

                # Apply options filter if provided
                if options:
                    # Check if all specified options match the variant options
                    options_match = True
                    for option_key, option_value in options.items():
                        variant_option_value = variant_options.get(option_key)

                        if variant_option_value is None:
                            options_match = False
                            break

                        # Handle multiple values for the same option (e.g., color: ["red", "blue"])
                        if isinstance(option_value, list):
                            # Check if variant's option value matches any of the provided values
                            variant_value_str = (
                                str(variant_option_value).lower().strip()
                            )
                            value_matches = any(
                                variant_value_str == str(val).lower().strip()
                                for val in option_value
                            )
                            if not value_matches:
                                options_match = False
                                break
                        else:
                            # Single value comparison (existing logic)
                            variant_value_str = (
                                str(variant_option_value).lower().strip()
                            )
                            search_value_str = str(option_value).lower().strip()

                            if variant_value_str != search_value_str:
                                options_match = False
                                break

                    if not options_match:
                        continue

                valid_variants.append(
                    {
                        "item_id": variant_id,
                        "price": variant_price,
                        "available": variant_available,
                        "options": variant_options,
                    }
                )

            if valid_variants:
                matching_products.append(
                    {
                        "product_id": product_id,
                        "name": product.get("name"),
                        "variants_count": len(valid_variants),
                        "price_range": {
                            "min": min(v["price"] for v in valid_variants),
                            "max": max(v["price"] for v in valid_variants),
                        },
                        "sample_variants": valid_variants,
                    }
                )

        # Filter based on price flag if provided and return only a single product
        if price_flag == "cheapest":
            # Sort sample_variants within each product by price
            for product in matching_products:
                if "sample_variants" in product:
                    product["sample_variants"].sort(key=lambda v: v["price"])
                    product["sample_variants"] = product["sample_variants"][
                        :limit
                    ]  # Limit to cheapest variant

        elif price_flag == "expensive":
            # Sort sample_variants within each product by price in descending order
            for product in matching_products:
                if "sample_variants" in product:
                    product["sample_variants"].sort(
                        key=lambda v: v["price"], reverse=True
                    )
                    product["sample_variants"] = product["sample_variants"][:limit]

        result = {
            "status": "success",
            "search_criteria": {
                "category": category,
                "min_price": min_price,
                "max_price": max_price,
                "available_only": available_only,
                "options_filter": options,
            },
            "total_products_found": len(matching_products),
            "products": matching_products[:10],
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchProductsByFilter",
                "description": "Search products by category, price range, availability, and specific variant options from product catalog",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "Product category filter (e.g., 'laptop', 't-shirt', 'bluetooth speaker')",
                        },
                        "min_price": {
                            "type": "number",
                            "description": "Minimum price filter",
                        },
                        "max_price": {
                            "type": "number",
                            "description": "Maximum price filter",
                        },
                        "available_only": {
                            "type": "boolean",
                            "description": "Show only available products",
                            "default": True,
                        },
                        "options": {
                            "type": "object",
                            "description": "Filter by specific variant options. Values can be strings or arrays for multiple options (e.g., {'color': ['red', 'blue'], 'battery life': '20 hours', 'size': ['large', 'medium']})",
                            "additionalProperties": {
                                "oneOf": [
                                    {"type": "string"},
                                    {"type": "array", "items": {"type": "string"}},
                                ]
                            },
                        },
                        "price_flag": {
                            "type": "string",
                            "description": "Flag to indicate price preference (e.g., 'cheapest', 'expensive')",
                        },
                        "limit": {
                            "type": "integer",
                            "description": "Maximum number of variants to return per product",
                            "default": 1,
                        },
                        "show_all": {
                            "type": "boolean",
                            "description": "Flag to indicate if all matching products should be returned",
                            "default": False,
                        },
                    },
                },
            },
        }


class GetUserOrderHistory(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], user_id: str, product_type: list[str] = None
    ) -> str:
        """
        Retrieve customer order history and account summary, optionally filtered by product type

        Data Sources: users.json (user_id, orders, payment_methods, name, email, address), orders.json (order details), products.json (product names for filtering)
        """
        # Rule: Validate user identity exists before processing any user requests
        users = data.get("users", [])
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            payload = {"error": f"User {user_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Extract user information from users.json structure
        user_orders = user.get("orders", [])
        payment_methods = user.get("payment_methods", {})
        user_name = user.get("name", {})
        user_address = user.get("address", {})

        # Get detailed order information if product_type filter is specified
        filtered_orders = user_orders
        filter_applied = False

        if product_type:
            # Convert product_type to lowercase for case-insensitive matching
            product_type_lower = [ptype.lower() for ptype in product_type]
            filter_applied = True

            # Get product information for filtering
            products = data.get("products", [])
            product_name_map = {}
            for product in products:
                product_id = product.get("product_id")
                product_name = product.get("name", "").lower()
                if product_id:
                    product_name_map[product_id] = product_name

            # Get order details to filter by product type
            orders = data.get("orders", [])
            filtered_orders = []

            for order_id in user_orders:
                # Find the order details
                order_details = None
                for order in orders:
                    if (
                        order.get("order_id") == order_id
                        and order.get("user_id") == user_id
                    ):
                        order_details = order
                        break

                if order_details:
                    order_items = order_details.get("items", [])
                    order_has_matching_products = False

                    # Check if any item in the order matches the product type filter
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

                    # Include order if it has matching products
                    if order_has_matching_products:
                        filtered_orders.append(order_id)

        # Rule: Payment methods must be valid type: credit_card, paypal, or gift_card
        valid_payment_methods = []
        for method_id, method_details in payment_methods.items():
            payment_source = method_details.get("source")
            if payment_source in ["credit_card", "paypal", "gift_card"]:
                method_info = {"id": method_id, "source": payment_source}

                # Add specific details based on payment type
                if payment_source == "credit_card":
                    method_info["brand"] = method_details.get("brand")
                    method_info["last_four"] = method_details.get("last_four")
                elif payment_source == "gift_card":
                    method_info["balance"] = method_details.get("balance", 0)

                valid_payment_methods.append(method_info)

        # Rule: Validate all required address fields: address1, city, country, state, zip
        address_complete = all(
            user_address.get(field)
            for field in ["address1", "city", "country", "state", "zip"]
        )

        # Get detailed information about filtered orders (both with and without product type filter)
        order_details_summary = []
        orders = data.get("orders", [])

        # Get product information for item_ids mapping
        products = data.get("products", [])
        product_name_map = {}
        for product in products:
            product_id = product.get("product_id")
            product_name = product.get("name", "").lower()
            if product_id:
                product_name_map[product_id] = product_name

        for order_id in filtered_orders:
            for order in orders:
                if (
                    order.get("order_id") == order_id
                    and order.get("user_id") == user_id
                ):
                    if filter_applied and product_type:
                        # Get matching products in this order (filtered case)
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
                                        matching_products.append(
                                            {
                                                "product_id": item_product_id,
                                                "product_name": item.get("name"),
                                                "item_id": item.get("item_id"),
                                                "quantity": item.get("quantity", 1),
                                                "price": item.get("price", 0),
                                            }
                                        )

                        if matching_products:
                            order_details_summary.append(
                                {
                                    "order_id": order_id,
                                    "order_status": order.get("status"),
                                    "order_date": order.get("timestamp"),
                                    "matching_products": matching_products,
                                    "total_matching_items": len(matching_products),
                                }
                            )
                    else:
                        # Get all products in this order (no filter case)
                        all_products = []
                        order_items = order.get("items", [])

                        for item in order_items:
                            all_products.append(
                                {
                                    "product_id": item.get("product_id"),
                                    "product_name": item.get("name"),
                                    "item_id": item.get("item_id"),
                                    "quantity": item.get("quantity", 1),
                                    "price": item.get("price", 0),
                                }
                            )

                        order_details_summary.append(
                            {
                                "order_id": order_id,
                                "order_status": order.get("status"),
                                "order_date": order.get("timestamp"),
                                "all_products": all_products,
                                "total_items": len(all_products),
                            }
                        )
                    break

        result = {
            "status": "success",
            "user_id": user_id,
            "customer_info": {
                "name": f"{user_name.get('first_name', '')} {user_name.get('last_name', '')}".strip(),
                "email": user.get("email"),
                "address_complete": address_complete,
                "address": user_address,
            },
            "filter_info": {
                "product_type_filter": product_type,
                "filter_applied": filter_applied,
                "original_order_count": len(user_orders),
                "filtered_order_count": len(filtered_orders),
            },
            "order_history": {
                "total_orders": len(filtered_orders),
                "order_ids": filtered_orders,
                "order_details": order_details_summary,
            },
            "payment_methods": {
                "total_methods": len(valid_payment_methods),
                "methods": valid_payment_methods,
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
                "name": "GetUserOrderHistory",
                "description": "Retrieve customer order history and account information with detailed product and item information, optionally filtered by product type",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Customer identifier",
                        },
                        "product_type": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional list of product types to filter orders by (e.g., ['laptop', 'smartphone', 't-shirt']). Only returns orders containing products whose names contain these terms.",
                        },
                    },
                    "required": ["user_id"],
                },
            },
        }


class ValidateSupplierCapacity(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str) -> str:
        """
        Validate supplier capacity and order status for procurement planning

        Data Sources: supply_orders.json (supplier_id, status, quantity, total_cost, order_date)
        """
        supply_orders = data.get("supply_orders", [])
        supplier_orders = [
            order for order in supply_orders if order.get("supplier_id") == supplier_id
        ]

        if not supplier_orders:
            payload = {
                "error": f"No supply orders found for supplier {supplier_id}",
                "status": "not_found",
            }
            out = json.dumps(payload)
            return out

        # Rule: Supply orders must reference valid supplier_id and existing product_id
        # Rule: Supply orders with status 'cancelled' require alternative sourcing and cannot be fulfilled
        pending_orders = []
        fulfilled_orders = []
        cancelled_orders = []

        for order in supplier_orders:
            status = order.get("status")
            if status == "pending":
                pending_orders.append(order)
            elif status == "fulfilled":
                fulfilled_orders.append(order)
            elif status == "cancelled":
                cancelled_orders.append(order)

        # Calculate capacity metrics
        total_pending_quantity = sum(order.get("quantity", 0) for order in pending_orders)
        total_fulfilled_quantity = sum(order.get("quantity", 0) for order in fulfilled_orders)
        total_cancelled_quantity = sum(order.get("quantity", 0) for order in cancelled_orders)

        total_pending_cost = sum(order.get("total_cost", 0) for order in pending_orders)
        total_fulfilled_cost = sum(order.get("total_cost", 0) for order in fulfilled_orders)

        # Calculate reliability metrics
        total_completed_orders = len(fulfilled_orders) + len(cancelled_orders)
        fulfillment_rate = (
            (len(fulfilled_orders) / total_completed_orders * 100)
            if total_completed_orders > 0
            else 0
        )

        # Generate rating and feedback based on fulfillment rate
        def get_supplier_rating_and_feedback(fulfillment_rate_percent):
            if fulfillment_rate_percent >= 90:
                return {
                    "rating": "Excellent",
                    "numeric_score": 5.0,
                    "feedback": "Outstanding performance with exceptional reliability. This supplier consistently delivers on commitments and is highly recommended for critical orders.",
                    "recommendation": "Preferred supplier - suitable for all order types including high-priority items.",
                }
            elif fulfillment_rate_percent >= 80:
                return {
                    "rating": "Good",
                    "numeric_score": 4.0,
                    "feedback": "Strong performance with good reliability. Minor fulfillment issues but generally dependable for most orders.",
                    "recommendation": "Reliable supplier - good choice for standard orders with some monitoring recommended.",
                }
            elif fulfillment_rate_percent >= 70:
                return {
                    "rating": "Fair",
                    "numeric_score": 3.0,
                    "feedback": "Moderate performance with some reliability concerns. Fulfillment rate indicates room for improvement in delivery consistency.",
                    "recommendation": "Caution advised - suitable for non-critical orders with backup sourcing options.",
                }
            elif fulfillment_rate_percent >= 50:
                return {
                    "rating": "Poor",
                    "numeric_score": 2.0,
                    "feedback": "Below-average performance with significant reliability issues. High cancellation rate may impact supply chain stability.",
                    "recommendation": "High risk supplier - avoid for critical orders and consider alternative sourcing.",
                }
            else:
                return {
                    "rating": "Unacceptable",
                    "numeric_score": 1.0,
                    "feedback": "Unacceptable performance with very poor reliability. Frequent order cancellations pose serious supply chain risks.",
                    "recommendation": "Not recommended - seek immediate alternative suppliers for all future orders.",
                }

        # Get supplier rating and feedback
        rating_info = get_supplier_rating_and_feedback(fulfillment_rate)

        # Calculate additional performance insights
        def get_performance_insights(
            fulfillment_rate_percent, total_orders, cancelled_count
        ):
            insights = []

            if total_orders < 5:
                insights.append(
                    "Limited order history - rating based on small sample size"
                )

            if cancelled_count > 0:
                cancellation_rate = (
                    cancelled_count / (total_orders if total_orders > 0 else 1)
                ) * 100
                if cancellation_rate > 20:
                    insights.append(
                        f"High cancellation rate ({cancellation_rate:.1f}%) indicates potential capacity or reliability issues"
                    )
                elif cancellation_rate > 10:
                    insights.append(
                        f"Moderate cancellation rate ({cancellation_rate:.1f}%) requires monitoring"
                    )

            if fulfillment_rate_percent == 100 and total_orders >= 10:
                insights.append(
                    "Perfect fulfillment record demonstrates exceptional reliability"
                )

            if fulfillment_rate_percent > 0 and len(pending_orders) > 0:
                insights.append(
                    f"Currently has {len(pending_orders)} pending orders requiring attention"
                )

            return insights

        performance_insights = get_performance_insights(
            fulfillment_rate, len(supplier_orders), len(cancelled_orders)
        )

        result = {
            "status": "success",
            "supplier_id": supplier_id,
            "order_summary": {
                "total_orders": len(supplier_orders),
                "pending_orders": len(pending_orders),
                "fulfilled_orders": len(fulfilled_orders),
                "cancelled_orders": len(cancelled_orders),
            },
            "quantity_metrics": {
                "pending_quantity": total_pending_quantity,
                "fulfilled_quantity": total_fulfilled_quantity,
                "cancelled_quantity": total_cancelled_quantity,
            },
            "cost_metrics": {
                "pending_value": round(total_pending_cost, 2),
                "fulfilled_value": round(total_fulfilled_cost, 2),
            },
            "reliability": {
                "fulfillment_rate_percent": round(fulfillment_rate, 1),
                "requires_alternative_sourcing": len(cancelled_orders) > 0,
            },
            "performance_rating": {
                "overall_rating": rating_info["rating"],
                "numeric_score": rating_info["numeric_score"],
                "performance_feedback": rating_info["feedback"],
                "sourcing_recommendation": rating_info["recommendation"],
                "performance_insights": performance_insights,
            },
            "recent_orders": (
                supplier_orders[-5:] if len(supplier_orders) >= 5 else supplier_orders
            ),
        }
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ValidateSupplierCapacity",
                "description": "Validate supplier capacity and reliability for procurement planning with performance rating based on fulfillment rate",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier identifier (e.g., '#SUP0001')",
                        }
                    },
                    "required": ["supplier_id"],
                },
            },
        }


class CalculateShippingCost(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        destination_country: str,
        total_items: int,
        order_value: float,
        location: dict[str, str] = None,
        courier_id: str = None
,
    address: Any = None,
    ) -> str:
        """
        Calculate shipping cost based on destination, weight, order value, optional detailed location, and specific courier selection

        Data Sources: couriers.json (courier_id, name, coverage_area, contact_info, base_cost, rating, service_types)
        """
        pass
        #Rule: Assign couriers only if destination country matches their coverage areas
        couriers = data.get("couriers", [])
        eligible_couriers = []

        for courier in couriers:
            coverage_area = courier.get("coverage_area", [])
            if destination_country in coverage_area:
                eligible_couriers.append(courier)

        if not eligible_couriers:
            payload = {
                    "error": f"No shipping service available to {destination_country}",
                    "status": "failed",
                }
            out = json.dumps(
                payload)
            return out

        #Select courier based on courier_id parameter or use automatic selection
        selected_courier = None
        courier_selection_method = "automatic"

        if courier_id:
            #Find the specific courier if provided
            selected_courier = next(
                (c for c in eligible_couriers if c.get("courier_id") == courier_id),
                None,
            )

            if not selected_courier:
                payload = {
                        "error": f"Courier {courier_id} not available for destination {destination_country} or does not exist",
                        "status": "failed",
                        "available_couriers": [
                            {"courier_id": c.get("courier_id"), "name": c.get("name")}
                            for c in eligible_couriers
                        ],
                    }
                out = json.dumps(
                    payload)
                return out
            courier_selection_method = "specific"
        else:
            #Use automatic selection logic (first available courier)
            selected_courier = eligible_couriers[0]

        #Process location information if provided
        delivery_location = None
        location_surcharge = 0.0

        if location:
            #Validate location has required fields
            required_location_fields = ["city", "country"]
            missing_fields = [
                field for field in required_location_fields if not location.get(field)
            ]

            if missing_fields:
                payload = {
                        "error": f"Location missing required fields: {', '.join(missing_fields)}",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out

            delivery_location = {
                "address1": location.get("address1", ""),
                "address2": location.get("address2", ""),
                "city": location.get("city"),
                "state": location.get("state", ""),
                "zip": location.get("zip", ""),
                "country": location.get("country"),
            }

            #Verify location country matches destination_country parameter
            if delivery_location["country"] != destination_country:
                payload = {
                        "error": f"Location country '{delivery_location['country']}' does not match destination_country '{destination_country}'",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out

            #Apply location-based surcharges (simplified logic)
            city = delivery_location["city"].lower()
            delivery_location.get("state", "").lower()

            #Remote area surcharge for certain locations
            remote_cities = ["anchorage", "honolulu", "fairbanks", "juneau"]
            if city in remote_cities:
                location_surcharge += 25.0

            #Rural area surcharge based on ZIP code patterns (simplified)
            zip_code = delivery_location.get("zip", "")
            if zip_code and len(zip_code) >= 5:
                #Example: certain ZIP code ranges might be considered rural
                if zip_code.startswith(("9999", "0000")):  #Placeholder logic
                    location_surcharge += 10.0

        #Get courier-specific pricing information
        courier_base_cost = selected_courier.get("base_cost", 9.99)
        courier_rating = selected_courier.get("rating", 0)
        courier_service_types = selected_courier.get("service_types", ["standard"])
        courier_specialties = selected_courier.get("specialties", [])

        #Calculate courier-specific adjustments
        courier_adjustment = 0.0
        service_quality_bonus = 0.0

        #Premium pricing for high-rated couriers
        if courier_rating >= 4.5:
            service_quality_bonus = 2.00  #Premium service surcharge
        elif courier_rating >= 4.0:
            service_quality_bonus = 1.00  #Good service slight surcharge
        elif courier_rating < 3.0:
            courier_adjustment = -1.00  #Discount for lower-rated couriers

        #Service type adjustments
        service_type_surcharge = 0.0
        courier_service_types[0] if courier_service_types else "standard"

        if "express" in courier_service_types:
            service_type_surcharge = 5.00
        elif "overnight" in courier_service_types:
            service_type_surcharge = 15.00
        elif "same-day" in courier_service_types:
            service_type_surcharge = 25.00

        #Specialty service adjustments
        specialty_adjustment = 0.0
        if "urban" in courier_specialties and location:
            city = delivery_location["city"].lower()
            major_cities = ["new york", "los angeles", "chicago", "houston", "phoenix"]
            if city in major_cities:
                specialty_adjustment = (
                    -2.00
                )  #Discount for urban specialists in major cities

        if "rural" in courier_specialties and location:
            zip_code = delivery_location.get("zip", "")
            if zip_code and len(zip_code) >= 5:
                #Rural areas benefit from rural specialists
                if not zip_code.startswith(
                    ("100", "200", "300", "400", "500")
                ):  #Non-major metro areas
                    specialty_adjustment = -3.00

        #Basic shipping cost calculation with courier-specific base cost
        base_cost = courier_base_cost
        weight_cost = total_items * 2.50  #$2.50 per unit weight

        #Rule: High-value orders (>$1000 total) require payment verification before fulfillment
        insurance_required = order_value > 1000.0
        insurance_cost = (
            (order_value * 0.015) if insurance_required else 0
        )  #1.5% of order value

        #International shipping surcharge
        international_surcharge = 15.00 if destination_country != "USA" else 0

        #Calculate total shipping cost with all adjustments
        total_shipping_cost = (
            base_cost
            + weight_cost
            + insurance_cost
            + international_surcharge
            + location_surcharge
            + courier_adjustment
            + service_quality_bonus
            + service_type_surcharge
            + specialty_adjustment
        )

        #Ensure minimum shipping cost
        total_shipping_cost = max(total_shipping_cost, 5.00)  #Minimum $5.00 shipping

        result = {
            "status": "success",
            "destination_country": destination_country,
            "delivery_location": delivery_location,
            "courier_selection": {
                "selected_courier": {
                    "courier_id": selected_courier.get("courier_id"),
                    "name": selected_courier.get("name"),
                    "rating": courier_rating,
                    "service_types": courier_service_types,
                    "specialties": courier_specialties,
                    "contact_info": selected_courier.get("contact_info"),
                },
                "selection_method": courier_selection_method,
                "courier_requested": courier_id is not None,
                "alternative_couriers_available": len(eligible_couriers) - 1,
            },
            "shipping_breakdown": {
                "base_cost": courier_base_cost,
                "weight_cost": round(weight_cost, 2),
                "insurance_cost": round(insurance_cost, 2),
                "international_surcharge": international_surcharge,
                "location_surcharge": round(location_surcharge, 2),
                "courier_adjustments": {
                    "courier_base_adjustment": round(courier_adjustment, 2),
                    "service_quality_bonus": round(service_quality_bonus, 2),
                    "service_type_surcharge": round(service_type_surcharge, 2),
                    "specialty_adjustment": round(specialty_adjustment, 2),
                },
                "total_cost": round(total_shipping_cost, 2),
            },
            "order_details": {
                "item_total": total_items,
                "value": order_value,
                "requires_insurance": insurance_required,
            },
            "courier_comparison": {
                "selected_courier_cost": round(total_shipping_cost, 2),
                "available_alternatives": len(eligible_couriers) - 1,
                "cost_factors": {
                    "courier_rating_impact": (
                        f"+${service_quality_bonus:.2f}"
                        if service_quality_bonus > 0
                        else f"${courier_adjustment:.2f}"
                    )
                }
            }
        }
        
        payload = result
        out = json.dumps(payload, indent=2)
        return out
        eligible_couriers = []

        for courier in couriers:
            coverage_area = courier.get("coverage_area", [])
            if destination_country in coverage_area:
                eligible_couriers.append(courier)

        if not eligible_couriers:
            payload = {
                    "error": f"No shipping service available to {destination_country}",
                    "status": "failed",
                }
            out = json.dumps(
                payload)
            return out

        #Select courier based on courier_id parameter or use automatic selection
        selected_courier = None
        courier_selection_method = "automatic"

        if courier_id:
            #Find the specific courier if provided
            selected_courier = next(
                (c for c in eligible_couriers if c.get("courier_id") == courier_id),
                None,
            )

            if not selected_courier:
                payload = {
                        "error": f"Courier {courier_id} not available for destination {destination_country} or does not exist",
                        "status": "failed",
                        "available_couriers": [
                            {"courier_id": c.get("courier_id"), "name": c.get("name")}
                            for c in eligible_couriers
                        ],
                    }
                out = json.dumps(
                    payload)
                return out
            courier_selection_method = "specific"
        else:
            #Use automatic selection logic (first available courier)
            selected_courier = eligible_couriers[0]

        #Process location information if provided
        delivery_location = None
        location_surcharge = 0.0

        if location:
            #Validate location has required fields
            required_location_fields = ["city", "country"]
            missing_fields = [
                field for field in required_location_fields if not location.get(field)
            ]

            if missing_fields:
                payload = {
                        "error": f"Location missing required fields: {', '.join(missing_fields)}",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out

            delivery_location = {
                "address1": location.get("address1", ""),
                "address2": location.get("address2", ""),
                "city": location.get("city"),
                "state": location.get("state", ""),
                "zip": location.get("zip", ""),
                "country": location.get("country"),
            }

            #Verify location country matches destination_country parameter
            if delivery_location["country"] != destination_country:
                payload = {
                        "error": f"Location country '{delivery_location['country']}' does not match destination_country '{destination_country}'",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out

            #Apply location-based surcharges (simplified logic)
            city = delivery_location["city"].lower()
            delivery_location.get("state", "").lower()

            #Remote area surcharge for certain locations
            remote_cities = ["anchorage", "honolulu", "fairbanks", "juneau"]
            if city in remote_cities:
                location_surcharge += 25.0

            #Rural area surcharge based on ZIP code patterns (simplified)
            zip_code = delivery_location.get("zip", "")
            if zip_code and len(zip_code) >= 5:
                #Example: certain ZIP code ranges might be considered rural
                if zip_code.startswith(("9999", "0000")):  #Placeholder logic
                    location_surcharge += 10.0

        #Get courier-specific pricing information
        courier_base_cost = selected_courier.get("base_cost", 9.99)
        courier_rating = selected_courier.get("rating", 0)
        courier_service_types = selected_courier.get("service_types", ["standard"])
        courier_specialties = selected_courier.get("specialties", [])

        #Calculate courier-specific adjustments
        courier_adjustment = 0.0
        service_quality_bonus = 0.0

        #Premium pricing for high-rated couriers
        if courier_rating >= 4.5:
            service_quality_bonus = 2.00  #Premium service surcharge
        elif courier_rating >= 4.0:
            service_quality_bonus = 1.00  #Good service slight surcharge
        elif courier_rating < 3.0:
            courier_adjustment = -1.00  #Discount for lower-rated couriers

        #Service type adjustments
        service_type_surcharge = 0.0
        courier_service_types[0] if courier_service_types else "standard"

        if "express" in courier_service_types:
            service_type_surcharge = 5.00
        elif "overnight" in courier_service_types:
            service_type_surcharge = 15.00
        elif "same-day" in courier_service_types:
            service_type_surcharge = 25.00

        #Specialty service adjustments
        specialty_adjustment = 0.0
        if "urban" in courier_specialties and location:
            city = delivery_location["city"].lower()
            major_cities = ["new york", "los angeles", "chicago", "houston", "phoenix"]
            if city in major_cities:
                specialty_adjustment = (
                    -2.00
                )  #Discount for urban specialists in major cities

        if "rural" in courier_specialties and location:
            zip_code = delivery_location.get("zip", "")
            if zip_code and len(zip_code) >= 5:
                #Rural areas benefit from rural specialists
                if not zip_code.startswith(
                    ("100", "200", "300", "400", "500")
                ):  #Non-major metro areas
                    specialty_adjustment = -3.00

        #Basic shipping cost calculation with courier-specific base cost
        base_cost = courier_base_cost
        weight_cost = total_items * 2.50  #$2.50 per unit weight

        #Rule: High-value orders (>$1000 total) require payment verification before fulfillment
        insurance_required = order_value > 1000.0
        insurance_cost = (
            (order_value * 0.015) if insurance_required else 0
        )  #1.5% of order value

        #International shipping surcharge
        international_surcharge = 15.00 if destination_country != "USA" else 0

        #Calculate total shipping cost with all adjustments
        total_shipping_cost = (
            base_cost
            + weight_cost
            + insurance_cost
            + international_surcharge
            + location_surcharge
            + courier_adjustment
            + service_quality_bonus
            + service_type_surcharge
            + specialty_adjustment
        )

        #Ensure minimum shipping cost
        total_shipping_cost = max(total_shipping_cost, 5.00)  #Minimum $5.00 shipping

        result = {
            "status": "success",
            "destination_country": destination_country,
            "delivery_location": delivery_location,
            "courier_selection": {
                "selected_courier": {
                    "courier_id": selected_courier.get("courier_id"),
                    "name": selected_courier.get("name"),
                    "rating": courier_rating,
                    "service_types": courier_service_types,
                    "specialties": courier_specialties,
                    "contact_info": selected_courier.get("contact_info"),
                },
                "selection_method": courier_selection_method,
                "courier_requested": courier_id is not None,
                "alternative_couriers_available": len(eligible_couriers) - 1,
            },
            "shipping_breakdown": {
                "base_cost": courier_base_cost,
                "weight_cost": round(weight_cost, 2),
                "insurance_cost": round(insurance_cost, 2),
                "international_surcharge": international_surcharge,
                "location_surcharge": round(location_surcharge, 2),
                "courier_adjustments": {
                    "courier_base_adjustment": round(courier_adjustment, 2),
                    "service_quality_bonus": round(service_quality_bonus, 2),
                    "service_type_surcharge": round(service_type_surcharge, 2),
                    "specialty_adjustment": round(specialty_adjustment, 2),
                },
                "total_cost": round(total_shipping_cost, 2),
            },
            "order_details": {
                "item_total": total_items,
                "value": order_value,
                "requires_insurance": insurance_required,
            },
            "courier_comparison": {
                "selected_courier_cost": round(total_shipping_cost, 2),
                "available_alternatives": len(eligible_couriers) - 1,
                "cost_factors": {
                    "courier_rating_impact": (
                        f"+${service_quality_bonus:.2f}"
                        if service_quality_bonus > 0
                        else f"${courier_adjustment:.2f}"
                    ),
                    "service_type_impact": (
                        f"+${service_type_surcharge:.2f}"
                        if service_type_surcharge > 0
                        else "$0.00"
                    ),
                    "specialty_discount": (
                        f"${specialty_adjustment:.2f}"
                        if specialty_adjustment != 0
                        else "$0.00"
                    ),
                },
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
                "name": "CalculateShippingCost",
                "description": "Calculate shipping cost based on destination, order characteristics, optional detailed location, and optional specific courier selection with courier-specific pricing",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "destination_country": {
                            "type": "string",
                            "description": "Destination country for shipping",
                        },
                        "total_items": {
                            "type": "number",
                            "description": "Total number of items",
                        },
                        "order_value": {
                            "type": "number",
                            "description": "Order value in dollars",
                        },
                        "location": {
                            "type": "object",
                            "properties": {
                                "address1": {
                                    "type": "string",
                                    "description": "Primary street address",
                                },
                                "address2": {
                                    "type": "string",
                                    "description": "Secondary address line (apartment, suite, etc.)",
                                },
                                "city": {"type": "string", "description": "City name"},
                                "state": {
                                    "type": "string",
                                    "description": "State or province",
                                },
                                "zip": {
                                    "type": "string",
                                    "description": "ZIP or postal code",
                                },
                                "country": {
                                    "type": "string",
                                    "description": "Country name",
                                },
                            },
                            "required": ["city", "country"],
                            "description": "Optional detailed delivery address for location-based pricing",
                        },
                        "courier_id": {
                            "type": "string",
                            "description": "Optional specific courier ID to use for shipping calculation. If provided, calculates cost using that courier's specific pricing, ratings, and service capabilities.",
                        },
                    },
                    "required": ["destination_country", "total_items", "order_value"],
                },
            },
        }

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateShippingCost",
                "description": "Calculate shipping cost based on destination, order characteristics, optional detailed location, and optional specific courier selection with courier-specific pricing",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "destination_country": {
                            "type": "string",
                            "description": "Destination country for shipping",
                        },
                        "total_items": {
                            "type": "number",
                            "description": "Total number of items",
                        },
                        "order_value": {
                            "type": "number",
                            "description": "Order value in dollars",
                        },
                        "location": {
                            "type": "object",
                            "properties": {
                                "address1": {
                                    "type": "string",
                                    "description": "Primary street address",
                                },
                                "address2": {
                                    "type": "string",
                                    "description": "Secondary address line (apartment, suite, etc.)",
                                },
                                "city": {"type": "string", "description": "City name"},
                                "state": {
                                    "type": "string",
                                    "description": "State or province",
                                },
                                "zip": {
                                    "type": "string",
                                    "description": "ZIP or postal code",
                                },
                                "country": {
                                    "type": "string",
                                    "description": "Country name",
                                },
                            },
                            "required": ["city", "country"],
                            "description": "Optional detailed delivery address for location-based pricing",
                        },
                        "courier_id": {
                            "type": "string",
                            "description": "Optional specific courier ID to use for shipping calculation. If provided, calculates cost using that courier's specific pricing, ratings, and service capabilities.",
                        },
                    },
                    "required": ["destination_country", "total_items", "order_value"],
                },
            },
        }


class GenerateOrderSummary(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str,
        item_list: list[dict[str, Any]],
        payment_methods_source: list[str],
        shipping_cost: float = 0.0,
    ) -> str:
        """
        Generate comprehensive order summary with pricing, taxes, and fulfillment requirements

        Data Sources: users.json (user_id, payment_methods), products.json (variants, pricing)
        """
        pass
        #Rule: Validate user identity exists before processing any user requests
        users = data.get("users", [])
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            payload = {"error": f"User {user_id} not found", "status": "failed"}
            out = json.dumps(
                payload)
            return out

        #Validate payment methods and prepare payment breakdown
        payment_methods = user.get("payment_methods", {})
        selected_payments = []

        for payment_method_id in payment_methods_source:
            selected_payment = None

            #Find payment method by ID
            for method_id in payment_methods:
                if payment_method_id in method_id or method_id in payment_method_id:
                    selected_payment = payment_methods[method_id]
                    break

            if not selected_payment:
                payload = {
                        "error": f"Payment method {payment_method_id} not found",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out

            payment_source = selected_payment.get("source")
            if payment_source not in ["credit_card", "paypal", "gift_card"]:
                payload = {
                        "error": f"Invalid payment method type: {payment_source}",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out

            payment_info = {
                "payment_method_id": payment_method_id,
                "payment_source": payment_source,
                "payment_details": selected_payment,
            }
            selected_payments.append(payment_info)

        #Validate and price all items
        products = data.get("products", [])
        order_items = []
        subtotal = 0.0

        #Rule: Multi-item orders need all items available before confirmation
        for item in item_list:
            item_id = item.get("item_id")
            quantity = item.get("quantity", 1)

            #Rule: Confirm item_id exists in product variants before including in orders
            variant_found = None
            product_found = None

            for product in products:
                variants = product.get("variants", {})
                if item_id in variants:
                    variant_found = variants[item_id]
                    product_found = product
                    break

            if not variant_found:
                payload = {"error": f"Item {item_id} not found", "status": "failed"}
                out = json.dumps(
                    payload)
                return out

            #Rule: Use exact variant pricing from product catalog - no unauthorized price modifications
            unit_price = variant_found.get("price", 0)
            line_total = unit_price * quantity
            subtotal += line_total

            order_items.append(
                {
                    "item_id": item_id,
                    "product_name": product_found.get("name"),
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "line_total": line_total,
                    "options": variant_found.get("options", {}),
                }
            )

        #Calculate taxes and fees (simplified)
        tax_rate = 0.08  #8% sales tax
        tax_amount = subtotal * tax_rate
        total_amount = subtotal + tax_amount

        total_amount += shipping_cost

        #Rule: High-value orders (>$1000 total) require payment verification before fulfillment
        requires_verification = total_amount > 1000.0

        #Calculate payment allocation across multiple payment methods with smart allocation
        remaining_amount = total_amount
        payment_breakdown = []
        payment_validation = {"overall_valid": True, "messages": []}

        for i, payment_info in enumerate(selected_payments):
            payment_source = payment_info["payment_source"]
            payment_details = payment_info["payment_details"]

            #Determine how much to allocate to this payment method
            if payment_source == "gift_card":
                #For gift cards, allocate up to available balance
                available_balance = payment_details.get("balance", 0)
                allocated_amount = min(available_balance, remaining_amount)

                #Validate gift card has some balance
                if available_balance == 0:
                    payment_validation["overall_valid"] = False
                    payment_validation["messages"].append(
                        f"{payment_info['payment_method_id']}: Gift card has no available balance"
                    )
            else:
                #For other payment methods, allocate remaining amount or even distribution
                if (
                    i == len(selected_payments) - 1
                ):  #Last payment method gets remaining amount
                    allocated_amount = remaining_amount
                else:
                    #Calculate even distribution among remaining non-gift-card methods
                    remaining_methods = len(selected_payments) - i
                    allocated_amount = round(remaining_amount / remaining_methods, 2)
                    if allocated_amount > remaining_amount:
                        allocated_amount = remaining_amount

            #Validate payment method
            method_validation = {"valid": True, "message": "Payment method validated"}
            if payment_source == "gift_card":
                available_balance = payment_details.get("balance", 0)
                if available_balance == 0:
                    method_validation = {
                        "valid": False,
                        "message": "Gift card has no available balance",
                    }
                    allocated_amount = 0
                elif (
                    allocated_amount < remaining_amount
                    and allocated_amount == available_balance
                ):
                    #Gift card doesn't cover full remaining amount, but this is handled by allocation logic
                    method_validation["message"] = (
                        f"Gift card covers ${allocated_amount:.2f} of remaining ${remaining_amount:.2f}"
                    )

            payment_breakdown.append(
                {
                    "payment_method_id": payment_info["payment_method_id"],
                    "payment_source": payment_source,
                    "allocated_amount": round(allocated_amount, 2),
                    "validation": method_validation,
                    "payment_details": {
                        "brand": (
                            payment_details.get("brand")
                            if payment_source == "credit_card"
                            else None
                        ),
                        "last_four": (
                            payment_details.get("last_four")
                            if payment_source == "credit_card"
                            else None
                        ),
                        "balance": (
                            payment_details.get("balance")
                            if payment_source == "gift_card"
                            else None
                        ),
                        "remaining_balance": (
                            (payment_details.get("balance", 0) - allocated_amount)
                            if payment_source == "gift_card"
                            else None
                        ),
                    },
                }
            )

            remaining_amount -= allocated_amount
            if not method_validation["valid"]:
                payment_validation["overall_valid"] = False

            #Break if we've allocated the full amount
            if remaining_amount <= 0.01:  #Account for floating point precision
                break

        #Check if we still have remaining amount after all allocations
        if remaining_amount > 0.01:
            payment_validation["overall_valid"] = False
            payment_validation["messages"].append(
                f"Insufficient payment methods to cover ${remaining_amount:.2f}"
            )

        #Rule: Maintain data integrity: order totals must match sum of item prices
        calculated_subtotal = sum(item["line_total"] for item in order_items)
        calculated_payment_total = sum(
            payment["allocated_amount"] for payment in payment_breakdown
        )
        integrity_check = abs(calculated_subtotal - subtotal) < 0.01
        payment_allocation_check = (
            abs(calculated_payment_total - (total_amount - max(0, remaining_amount)))
            < 0.01
        )

        result = {
            "status": "success",
            "order_summary": {
                "user_id": user_id,
                "pricing": {
                    "subtotal": round(subtotal, 2),
                    "tax_amount": round(tax_amount, 2),
                    "shipping_cost": round(shipping_cost, 2),
                    "total_amount": round(total_amount, 2),
                },
                "total_items": len(order_items),
                "items": order_items,
                "payment_breakdown": {
                    "total_payment_methods": len(payment_breakdown),
                    "payment_methods": payment_breakdown,
                    "total_allocated": round(calculated_payment_total, 2),
                    "remaining_amount": round(max(0, remaining_amount), 2),
                    "validation": payment_validation,
                },
                "fulfillment_requirements": {
                    "requires_verification": requires_verification,
                    "high_value_order": total_amount > 1000.0,
                },
                "data_integrity": {
                    "totals_match": integrity_check,
                    "calculated_subtotal": round(calculated_subtotal, 2),
                    "payment_allocation_correct": payment_allocation_check,
                },
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
                "name": "GenerateOrderSummary",
                "description": "Generate comprehensive order summary with pricing and payment breakdown across multiple methods",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Customer identifier",
                        },
                        "item_list": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "item_id": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                },
                                "required": ["item_id", "quantity"],
                            },
                            "description": "List of items in the order",
                        },
                        "payment_methods_source": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of payment method identifiers to use for payment",
                        },
                        "shipping_cost": {
                            "type": "number",
                            "description": "Optional shipping cost to include in order summary, if applicable",
                        },
                    },
                    "required": ["user_id", "item_list", "payment_methods_source"],
                },
            },
        }


class CreateOrder(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str,
        items: list[dict[str, Any]],
        payment_method_sources: list[str],
        return_refund_amount: float = None,
        return_order_id: str = None,
        shipping_cost: float = 0.0,
        tax_amount: float = 0.0,
    ) -> str:
        """
        Create a new order for a customer with items, address, and payment processing using multiple payment methods
        Supports replacement orders with automatic refund deduction

        Writes to: orders.json (creates new order entry)
        Data Sources: users.json, products.json for validation
        """
        pass
        #Validate return parameters if provided
        if return_refund_amount is not None and return_refund_amount < 0:
            payload = {"error": "Return refund amount cannot be negative", "status": "failed"}
            out = json.dumps(
                payload)
            return out

        #Rule: Validate user identity exists before processing any user requests
        users = data.get("users", [])
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            payload = {"error": f"User {user_id} not found", "status": "failed"}
            out = json.dumps(
                payload)
            return out

        #Validate return order exists if return_order_id is provided
        if return_order_id:
            orders = data.get("orders", [])
            return_order_found = False
            for order in orders:
                if (
                    order.get("order_id") == return_order_id
                    and order.get("user_id") == user_id
                ):
                    return_order_found = True
                    break

            if not return_order_found:
                payload = {
                        "error": f"Return order {return_order_id} not found or does not belong to user {user_id}",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out

        #Validate payment methods and prepare payment breakdown
        payment_methods = user.get("payment_methods", {})
        selected_payments = []

        for payment_method_source in payment_method_sources:
            selected_payment = None

            #Find payment method by ID
            for method_id in payment_methods:
                if payment_method_source in method_id:
                    selected_payment = payment_methods[method_id]
                    break

            if not selected_payment:
                payload = {
                        "error": f"Payment method {payment_method_source} not found",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out

            payment_source = selected_payment.get("source")
            if payment_source not in ["credit_card", "paypal", "gift_card"]:
                payload = {
                        "error": f"Invalid payment method type: {payment_source}",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out

            payment_info = {
                "payment_method_id": payment_method_source,
                "payment_source": payment_source,
                "payment_details": selected_payment,
            }
            selected_payments.append(payment_info)

        #Validate and process items
        products = data.get("products", [])
        order_items = []
        subtotal_amount = 0.0

        #Rule: Multi-item orders need all items available before confirmation
        for item in items:
            item_id = item.get("item_id")
            quantity = item.get("quantity", 1)

            #Rule: Confirm item_id exists in product variants before including in orders
            variant_found = None
            product_found = None

            for product in products:
                variants = product.get("variants", {})
                if item_id in variants:
                    variant_found = variants[item_id]
                    product_found = product
                    break

            if not variant_found:
                payload = {
                        "error": f"Item {item_id} not found in catalog",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out

            #Rule: Check product availability status before allocation - never allocate unavailable items
            if not variant_found.get("available", False):
                payload = {
                        "error": f"Item {item_id} ({product_found.get('name')}) is not available",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out

            #Rule: Use exact variant pricing from product catalog
            unit_price = variant_found.get("price", 0)
            line_total = unit_price * quantity
            subtotal_amount += line_total

            order_items.append(
                {
                    "name": product_found.get("name"),
                    "product_id": product_found.get("product_id"),
                    "item_id": item_id,
                    "price": unit_price,
                    "options": variant_found.get("options", {}),
                    "quantity": quantity,
                }
            )

        #Calculate total before refund deduction
        total_before_refund = subtotal_amount

        #Add shipping costs if provided
        if shipping_cost < 0:
            payload = {"error": "Shipping cost cannot be negative", "status": "failed"}
            out = json.dumps(
                payload)
            return out
        total_before_refund += shipping_cost

        if tax_amount < 0:
            payload = {"error": "Tax amount cannot be negative", "status": "failed"}
            out = json.dumps(
                payload)
            return out
        total_before_refund += tax_amount

        #Apply return refund deduction
        refund_applied = 0.0
        customer_refund_due = 0.0
        total_amount = total_before_refund

        if return_refund_amount is not None and return_refund_amount > 0:
            refund_applied = min(return_refund_amount, total_before_refund)
            total_amount = max(0, total_before_refund - return_refund_amount)

            #Calculate customer refund if return refund exceeds order total
            if return_refund_amount > total_before_refund:
                customer_refund_due = return_refund_amount - total_before_refund

        #Only proceed with payment processing if there's a remaining amount to pay
        payment_breakdown = []
        payment_validation = {"overall_valid": True, "messages": []}

        if total_amount > 0:
            #Calculate payment allocation across multiple payment methods with smart allocation
            remaining_amount = total_amount

            for i, payment_info in enumerate(selected_payments):
                payment_source = payment_info["payment_source"]
                payment_details = payment_info["payment_details"]

                #Determine how much to allocate to this payment method
                if payment_source == "gift_card":
                    #For gift cards, allocate up to available balance
                    available_balance = payment_details.get("balance", 0)
                    allocated_amount = min(available_balance, remaining_amount)

                    #Validate gift card has some balance
                    if available_balance == 0:
                        payment_validation["overall_valid"] = False
                        payment_validation["messages"].append(
                            f"{payment_info['payment_method_id']}: Gift card has no available balance"
                        )
                        allocated_amount = 0
                else:
                    #For other payment methods, allocate remaining amount
                    if (
                        i == len(selected_payments) - 1
                    ):  #Last payment method gets remaining amount
                        allocated_amount = remaining_amount
                    else:
                        #Calculate even distribution among remaining non-gift-card methods
                        remaining_methods = len(selected_payments) - i
                        allocated_amount = round(
                            remaining_amount / remaining_methods, 2
                        )
                        if allocated_amount > remaining_amount:
                            allocated_amount = remaining_amount

                #Validate payment method
                method_validation = {
                    "valid": True,
                    "message": "Payment method validated",
                }
                if payment_source == "gift_card":
                    available_balance = payment_details.get("balance", 0)
                    if available_balance == 0:
                        method_validation = {
                            "valid": False,
                            "message": "Gift card has no available balance",
                        }
                    elif (
                        allocated_amount < remaining_amount
                        and allocated_amount == available_balance
                    ):
                        #Gift card doesn't cover full remaining amount, but this is handled by allocation logic
                        method_validation["message"] = (
                            f"Gift card covers ${allocated_amount:.2f} of remaining ${remaining_amount:.2f}"
                        )

                if (
                    allocated_amount > 0
                ):  #Only add payment methods that have allocated amounts
                    payment_breakdown.append(
                        {
                            "payment_method_id": payment_info["payment_method_id"],
                            "payment_source": payment_source,
                            "allocated_amount": round(allocated_amount, 2),
                            "validation": method_validation,
                        }
                    )

                remaining_amount -= allocated_amount
                if not method_validation["valid"]:
                    payment_validation["overall_valid"] = False

                #Break if we've allocated the full amount
                if remaining_amount <= 0.01:  #Account for floating point precision
                    break

            #Check if we still have remaining amount after all allocations
            if remaining_amount > 0.01:
                payment_validation["overall_valid"] = False
                payment_validation["messages"].append(
                    f"Insufficient payment methods to cover ${remaining_amount:.2f}"
                )
                payload = {
                        "error": f"Insufficient payment methods to cover total amount of ${total_amount:.2f}. Remaining: ${remaining_amount:.2f}",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out

            if not payment_validation["overall_valid"]:
                payload = {
                        "error": "Payment validation failed: "
                        + "; ".join(payment_validation["messages"]),
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out

        #Generate new order ID
        existing_orders = data.get("orders", [])
        order_number = len(existing_orders) + 1
        new_order_id = f"#W{str(order_number).zfill(7)}"

        #Rule: High-value orders (>$1000 total) require payment verification before fulfillment
        requires_verification = total_before_refund > 1000.0

        #Create payment history entries for all payment methods
        payment_history = []

        #Add refund deduction entry if applicable
        if refund_applied > 0:
            payment_history.append(
                {
                    "transaction_type": "refund_deduction",
                    "amount": refund_applied,
                    "return_order_id": return_order_id,
                    "processed_date": datetime.now().isoformat(),
                    "description": f"Refund deduction from return order {return_order_id}",
                }
            )

        #Add payment entries for remaining amount
        for payment in payment_breakdown:
            if payment["allocated_amount"] > 0:
                payment_history.append(
                    {
                        "transaction_type": "payment",
                        "amount": payment["allocated_amount"],
                        "payment_method_id": payment["payment_method_id"],
                        "payment_source": payment["payment_source"],
                        "processed_date": datetime.now().isoformat(),
                    }
                )

        #Create new order object
        new_order = {
            "order_id": new_order_id,
            "user_id": user_id,
            "address": user.get("address", {}),
            "items": order_items,
            "fulfillments": [],
            "status": "pending",
            "payment_history": payment_history,
            "payment_breakdown": payment_breakdown,
            "order_type": (
                "replacement" if return_refund_amount is not None else "standard"
            ),
            "timestamp": datetime.now().isoformat(),
        }

        #Add return-related information if this is a replacement order
        if return_refund_amount is not None:
            new_order["return_replacement_info"] = {
                "original_return_order_id": return_order_id,
                "refund_amount_applied": refund_applied,
                "customer_refund_due": customer_refund_due,
                "replacement_order": True,
            }

        #WRITE OPERATION: Add new order to orders.json
        if "orders" not in data:
            data["orders"] = []
        data["orders"].append(new_order)

        #WRITE OPERATION: Update user's order list in users.json
        if "orders" not in user:
            user["orders"] = []
        user["orders"].append(new_order_id)

        #Calculate final amounts for response
        final_payment_amount = sum(p["allocated_amount"] for p in payment_breakdown)

        result = {
            "status": "success",
            "order_created": new_order_id,
            "user_id": user_id,
            "order_type": new_order["order_type"],
            "pricing_breakdown": {
                "subtotal": round(subtotal_amount, 2),
                "shipping_cost": round(shipping_cost, 2),
                "tax_amount": round(tax_amount, 2),
                "total_before_refund": round(total_before_refund, 2),
                "refund_applied": round(refund_applied, 2),
                "final_order_amount": round(total_amount, 2),
            },
            "total_items": len(order_items),
            "payment_breakdown": {
                "total_payment_methods": len(payment_breakdown),
                "payment_methods": payment_breakdown,
                "total_payment_amount": round(final_payment_amount, 2),
                "validation": payment_validation,
            },
            "return_replacement_details": (
                {
                    "return_order_id": return_order_id,
                    "refund_amount_applied": round(refund_applied, 2),
                    "for_customer_refund": round(customer_refund_due, 2),
                    "customer_refund_due": customer_refund_due > 0,
                }
                if return_refund_amount is not None
                else None
            ),
            "requires_verification": requires_verification,
            "order_status": "pending",
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateOrder",
                "description": "Create a new customer order with items and multiple payment methods processing. Supports replacement orders with automatic refund deduction.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Customer identifier",
                        },
                        "items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "item_id": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                },
                                "required": ["item_id", "quantity"],
                            },
                            "description": "List of items to include in order",
                        },
                        "payment_method_sources": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of payment method sources to use for payment",
                        },
                        "return_refund_amount": {
                            "type": "number",
                            "description": "Optional refund amount from returned items to deduct from this order. If greater than order total, excess will be refunded to customer.",
                        },
                        "return_order_id": {
                            "type": "string",
                            "description": "Optional order ID that generated the return/refund (for tracking purposes)",
                        },
                        "shipping_cost": {
                            "type": "number",
                            "description": "Shipping costs to include in the order",
                        },
                        "tax_amount": {
                            "type": "number",
                            "description": "Optional tax amount to include in the order",
                        },
                    },
                    "required": ["user_id", "items", "payment_method_sources"],
                },
            },
        }


class UpdateOrderStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str = None,
        order_ids: list[str] = None,
        new_status: str = None,
        tracking_id: str = None,
        courier_id: str = None,
    ) -> str:
        """
        Update order status and add fulfillment tracking information
        Supports both single order and batch processing

        Writes to: orders.json (updates existing order status and fulfillments)
        Data Sources: couriers.json for tracking validation
        """
        # Validate input parameters
        if not order_id and not order_ids:
            payload = {
                "error": "Either order_id or order_ids must be provided",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        if order_id and order_ids:
            payload = {
                "error": "Cannot specify both order_id and order_ids. Use one or the other.",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        if not new_status:
            payload = {"error": "new_status is required", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Rule: Only process orders with valid status: pending, processed, delivered, cancelled
        valid_statuses = [
            "pending",
            "processed",
            "delivered",
            "cancelled",
            "for return",
        ]
        if new_status not in valid_statuses:
            payload = {
                "error": f"Invalid status '{new_status}'. Valid statuses: {', '.join(valid_statuses)}",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Build list of orders to process
        orders_to_process = []
        if order_id:
            orders_to_process.append(order_id.strip())
        if order_ids:
            orders_to_process.extend(
                [oid.strip() for oid in order_ids if oid and oid.strip()]
            )

        if not orders_to_process:
            payload = {"error": "No valid order IDs provided", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Validate tracking and courier if provided
        selected_courier = None
        if tracking_id and courier_id:
            couriers = data.get("couriers", [])

            for courier in couriers:
                if courier.get("courier_id") == courier_id:
                    selected_courier = courier
                    break

            if not selected_courier:
                payload = {"error": f"Courier {courier_id} not found", "status": "failed"}
                out = json.dumps(payload)
                return out

            # Rule: Cross-reference tracking_id assignments with courier's tracking pools to prevent duplicates
            courier_tracking_ids = selected_courier.get("tracking_ids", [])
            if tracking_id not in courier_tracking_ids:
                payload = {
                    "error": f"Tracking ID {tracking_id} not available for courier {courier_id}",
                    "status": "failed",
                }
                out = json.dumps(payload)
                return out
        elif (tracking_id and not courier_id) or (not tracking_id and courier_id):
            payload = {
                "error": "Both tracking_id and courier_id must be provided together, or neither",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Find and process all orders
        orders = data.get("orders", [])
        successful_updates = []
        failed_updates = []

        for order_id_input in orders_to_process:
            # Add # prefix if not provided (for convenience)
            formatted_order_id = (
                order_id_input
                if order_id_input.startswith("#")
                else f"#{order_id_input}"
            )

            order_found = False
            for i, order in enumerate(orders):
                if order.get("order_id") == formatted_order_id:
                    order_found = True
                    old_status = order.get("status")

                    # Add fulfillment information if tracking details provided
                    if tracking_id and courier_id and selected_courier:
                        fulfillment_entry = {
                            "tracking_id": tracking_id,
                            "courier_id": courier_id,
                            "courier_name": selected_courier.get("name"),
                            "status": new_status,
                            "timestamp": datetime.now().isoformat(),
                        }

                        # WRITE OPERATION: Update fulfillments array
                        if "fulfillments" not in order:
                            order["fulfillments"] = []
                        order["fulfillments"].append(fulfillment_entry)

                    # WRITE OPERATION: Update order status in orders.json
                    order["status"] = new_status
                    order["last_updated"] = datetime.now().isoformat()

                    # Update the order in the data structure
                    data["orders"][i] = order

                    successful_updates.append(
                        {
                            "order_id": formatted_order_id,
                            "user_id": order.get("user_id"),
                            "previous_status": old_status,
                            "new_status": new_status,
                            "tracking_info": (
                                {
                                    "tracking_id": tracking_id,
                                    "courier_id": courier_id,
                                    "courier_name": (
                                        selected_courier.get("name")
                                        if selected_courier
                                        else None
                                    ),
                                }
                                if tracking_id and courier_id
                                else None
                            ),
                            "fulfillments_count": len(order.get("fulfillments", [])),
                            "last_updated": order["last_updated"],
                        }
                    )
                    break

            if not order_found:
                failed_updates.append(
                    {"order_id": formatted_order_id, "error": "Order not found"}
                )

        # Prepare comprehensive response
        result = {
            "status": "success" if successful_updates else "failed",
            "batch_processing": len(orders_to_process) > 1,
            "processing_summary": {
                "total_processed": len(orders_to_process),
                "successful_updates": len(successful_updates),
                "failed_updates": len(failed_updates),
            },
            "new_status": new_status,
            "tracking_assignment": (
                {
                    "tracking_id": tracking_id,
                    "courier_id": courier_id,
                    "courier_name": (
                        selected_courier.get("name") if selected_courier else None
                    ),
                }
                if tracking_id and courier_id
                else None
            ),
            "successful_updates": successful_updates,
            "failed_updates": failed_updates,
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateOrderStatus",
                "description": "Update order status and add tracking information. Supports both single order and batch processing.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Single order identifier to update. Cannot be used with order_ids.",
                        },
                        "order_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Array of order identifiers for batch processing. Cannot be used with order_id.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status (pending, processed, delivered, cancelled)",
                        },
                        "tracking_id": {
                            "type": "string",
                            "description": "Tracking number for shipment (optional, requires courier_id)",
                        },
                        "courier_id": {
                            "type": "string",
                            "description": "Courier identifier (required if tracking_id provided)",
                        },
                    },
                    "anyOf": [
                        {"required": ["order_id", "new_status"]},
                        {"required": ["order_ids", "new_status"]},
                    ],
                },
            },
        }


class UpdateSupplyOrderStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        supply_order_id: str = None,
        new_status: str = None,
        delivery_date: str = None,
    ) -> str:
        """
        Update supply order status for inventory management and procurement tracking

        Writes to: supply_orders.json (updates existing supply order status)
        """
        pass
        # Rule: Supply orders with status 'cancelled' require alternative sourcing and cannot be fulfilled
        valid_statuses = ["pending", "fulfilled", "cancelled"]
        if new_status not in valid_statuses:
            payload = {
                "error": f"Invalid status '{new_status}'. Valid statuses: {', '.join(valid_statuses)}",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Find the supply order to update
        supply_orders = data.get("supply_orders", [])
        supply_order_to_update = None
        order_index = None

        for i, order in enumerate(supply_orders):
            if order.get("supply_order_id") == supply_order_id:
                supply_order_to_update = order
                order_index = i
                break

        if not supply_order_to_update:
            payload = {
                "error": f"Supply order {supply_order_id} not found",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Rule: Supply orders must reference valid supplier_id and existing product_id
        supplier_id = supply_order_to_update.get("supplier_id")
        product_id = supply_order_to_update.get("product_id")

        if not supplier_id or not product_id:
            payload = {
                "error": f"Supply order {supply_order_id} has invalid supplier or product reference",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # WRITE OPERATION: Update supply order status in supply_orders.json
        old_status = supply_order_to_update.get("status")
        supply_order_to_update["status"] = new_status
        supply_order_to_update["last_updated"] = datetime.now().isoformat()

        # Add delivery information if provided and status is fulfilled
        if delivery_date and new_status == "fulfilled":
            supply_order_to_update["delivery_date"] = delivery_date
            supply_order_to_update["fulfilled_date"] = datetime.now().isoformat()

        # Track cancellation reason for alternative sourcing
        if new_status == "cancelled" and old_status != "cancelled":
            supply_order_to_update["cancelled_date"] = datetime.now().isoformat()
            supply_order_to_update["requires_alternative_sourcing"] = True

        # Update the supply order in the data structure
        data["supply_orders"][order_index] = supply_order_to_update

        # Calculate impact metrics
        quantity = supply_order_to_update.get("quantity", 0)
        total_cost = supply_order_to_update.get("total_cost", 0)

        result = {
            "status": "success",
            "supply_order_id": supply_order_id,
            "supplier_id": supplier_id,
            "product_id": product_id,
            "item_id": supply_order_to_update.get("item_id"),
            "status_change": {"previous_status": old_status, "new_status": new_status},
            "order_details": {"quantity": quantity, "total_cost": total_cost},
            "fulfillment_info": (
                {
                    "delivery_date": delivery_date,
                    "fulfilled_date": supply_order_to_update.get("fulfilled_date"),
                }
                if new_status == "fulfilled"
                else None
            ),
            "requires_alternative_sourcing": supply_order_to_update.get(
                "requires_alternative_sourcing", False
            ),
            "last_updated": supply_order_to_update["last_updated"],
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateSupplyOrderStatus",
                "description": "Update supply order status for inventory management and procurement tracking",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {
                            "type": "string",
                            "description": "Supply order identifier (e.g., '#SO9359')",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status (pending, fulfilled, cancelled)",
                        },
                        "delivery_date": {
                            "type": "string",
                            "description": "Expected/actual delivery date (optional, ISO format)",
                        },
                    },
                    "required": ["supply_order_id", "new_status"],
                },
            },
        }


class UpdateProductAvailability(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        product_id: str = None,
        item_id: str = None,
        available: bool = True,
        new_price: float = None,
    ) -> str:
        """
        Update product variant availability status and optionally price

        Writes to: products.json (updates variant availability and price)
        """
        products = data.get("products", [])
        product_to_update = None
        product_index = None

        # Find the product
        for i, product in enumerate(products):
            if product.get("product_id") == product_id:
                product_to_update = product
                product_index = i
                break

        if not product_to_update:
            payload = {"error": f"Product {product_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Rule: Confirm item_id exists in product variants before including in orders
        variants = product_to_update.get("variants", {})
        if item_id not in variants:
            payload = {
                "error": f"Item variant {item_id} not found in product {product_id}",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        variant_to_update = variants[item_id]
        old_availability = variant_to_update.get("available", False)
        old_price = variant_to_update.get("price", 0)

        # WRITE OPERATION: Update variant availability in products.json
        variant_to_update["available"] = available
        variant_to_update["last_updated"] = datetime.now().isoformat()

        # Rule: Use exact variant pricing from product catalog - authorized price modification
        price_updated = False
        if new_price is not None:
            if new_price < 0:
                payload = {"error": "Price cannot be negative", "status": "failed"}
                out = json.dumps(payload)
                return out
            variant_to_update["price"] = new_price
            price_updated = True

        # Update the product in the data structure
        data["products"][product_index] = product_to_update

        result = {
            "status": "success",
            "product_id": product_id,
            "product_name": product_to_update.get("name"),
            "item_id": item_id,
            "availability_update": {
                "previous_available": old_availability,
                "new_available": available,
            },
            "price_update": (
                {
                    "updated": price_updated,
                    "previous_price": old_price,
                    "new_price": new_price,
                }
                if price_updated
                else {"updated": False}
            ),
            "variant_options": variant_to_update.get("options", {}),
            "last_updated": variant_to_update["last_updated"],
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateProductAvailability",
                "description": "Update product variant availability status and optionally price",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {
                            "type": "string",
                            "description": "Product identifier",
                        },
                        "item_id": {
                            "type": "string",
                            "description": "Product variant identifier",
                        },
                        "available": {
                            "type": "boolean",
                            "description": "New availability status",
                        },
                        "new_price": {
                            "type": "number",
                            "description": "New price (optional)",
                        },
                    },
                    "required": ["product_id", "item_id"],
                },
            },
        }

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


class ValidateUserIdentity(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str = None,
        first_name: str = None,
        last_name: str = None,
    ) -> str:
        """
        Simple validation to check if user exists in the system with optional name verification
        Can search by user_id OR by first_name and last_name combination
        Always includes comprehensive user location details in the response

        Data Sources: users.json (user_id, name, address)
        """
        _first_nameL = first_name or ''.lower()
        _last_nameL = last_name or ''.lower()
        pass
        #Validate input parameters
        if not user_id and (not first_name or not last_name):
            payload = {
                    "error": "Either user_id must be provided, or both first_name and last_name must be provided",
                    "status": "failed",
                }
            out = json.dumps(
                payload)
            return out

        users = data.get("users", [])
        target_user = None
        search_method = "user_id" if user_id else "name_search"

        if user_id:
            #Rule: Validate user identity exists before processing any user requests
            target_user = next((u for u in users if u.get("user_id") == user_id), None)

            if not target_user:
                payload = {
                        "error": f"User {user_id} not found",
                        "status": "failed",
                        "user_exists": False,
                        "search_method": search_method,
                    }
                out = json.dumps(
                    payload)
                return out
        else:
            #Search by first_name and last_name
            matching_users = []

            for user in users:
                user_name = user.get("name", {})
                stored_first_name = user_name.get("first_name", "").lower().strip()
                stored_last_name = user_name.get("last_name", "").lower().strip()

                provided_first_name = first_name.lower().strip()
                provided_last_name = last_name.lower().strip()

                if (
                    stored_first_name == provided_first_name
                    and stored_last_name == provided_last_name
                ):
                    matching_users.append(user)

            if not matching_users:
                payload = {
                        "error": f"No user found with name '{first_name} {last_name}'",
                        "status": "failed",
                        "user_exists": False,
                        "search_method": search_method,
                        "search_criteria": {
                            "first_name": first_name,
                            "last_name": last_name,
                        },
                    }
                out = json.dumps(
                    payload)
                return out

            if len(matching_users) > 1:
                #Multiple users found with same name
                user_ids = [user.get("user_id") for user in matching_users]
                payload = {
                        "error": f"Multiple users found with name '{first_name} {last_name}'. Please specify user_id.",
                        "status": "multiple_matches",
                        "matching_user_ids": user_ids,
                        "total_matches": len(matching_users),
                        "search_method": search_method,
                        "search_criteria": {
                            "first_name": first_name,
                            "last_name": last_name,
                        },
                    }
                out = json.dumps(
                    payload)
                return out

            #Single user found
            target_user = matching_users[0]
            user_id = target_user.get("user_id")  #Set user_id for response

        #Additional validation for first_name and last_name if provided when searching by user_id
        validation_details = {"user_id_valid": True}
        user_name = target_user.get("name", {})
        stored_first_name = user_name.get("first_name", "")
        stored_last_name = user_name.get("last_name", "")
        stored_email = target_user.get("email", "")

        #Only validate names if user_id was provided and names were also provided (for additional verification)
        if search_method == "user_id":
            if first_name is not None:
                if stored_first_name.lower() != first_name.lower():
                    payload = {
                            "error": f"First name mismatch for user {user_id}",
                            "status": "failed",
                            "user_exists": True,
                            "first_name_valid": False,
                            "search_method": search_method,
                        }
                    out = json.dumps(
                        payload)
                    return out
                validation_details["first_name_valid"] = True

            if last_name is not None:
                if stored_last_name.lower() != last_name.lower():
                    payload = {
                            "error": f"Last name mismatch for user {user_id}",
                            "status": "failed",
                            "user_exists": True,
                            "last_name_valid": False,
                            "search_method": search_method,
                        }
                    out = json.dumps(
                        payload)
                    return out
                validation_details["last_name_valid"] = True
        else:
            #For name search, names are automatically valid since we found the user by name
            validation_details["first_name_valid"] = True
            validation_details["last_name_valid"] = True

        #Always include comprehensive user location details in the response
        user_address = target_user.get("address", {})

        user_location_details = {
            "address1": user_address.get("address1", ""),
            "address2": user_address.get("address2", ""),
            "city": user_address.get("city", ""),
            "state": user_address.get("state", ""),
            "zip": user_address.get("zip", ""),
            "country": user_address.get("country", ""),
        }

        #Check if address is complete
        required_address_fields = ["address1", "city", "state", "zip", "country"]
        address_complete = all(
            user_address.get(field) for field in required_address_fields
        )
        missing_fields = [
            field for field in required_address_fields if not user_address.get(field)
        ]

        #Determine address quality/completeness status
        address_status = "complete" if address_complete else "incomplete"
        if len(missing_fields) >= 4:
            address_status = "minimal"
        elif len(missing_fields) >= 2:
            address_status = "partial"

        #Check if location supports delivery (based on available couriers)
        couriers = data.get("couriers", [])
        supported_countries = set()
        for courier in couriers:
            supported_countries.update(courier.get("coverage_area", []))

        destination_country = user_address.get("country", "")
        delivery_available = (
            destination_country in supported_countries if destination_country else False
        )
        payload = {
                "status": "success",
                "user_exists": True,
                "user_id": user_id,
                "search_method": search_method,
                "validation_details": validation_details,
                "user_name": {
                    "first_name": stored_first_name,
                    "last_name": stored_last_name,
                    "full_name": f"{stored_first_name} {stored_last_name}".strip(),
                },
                "user_email": {"email": stored_email},
                "user_location": {
                    "address_details": user_location_details,
                    "address_status": address_status,
                    "address_complete": address_complete,
                    "missing_fields": missing_fields,
                    "delivery_available": delivery_available,
                    "supported_country": (
                        destination_country in supported_countries
                        if destination_country
                        else None
                    ),
                },
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ValidateUserIdentity",
                "description": "Check if user exists in the system with optional name verification. Can search by user_id OR by first_name and last_name combination. Always returns comprehensive user details including complete location information and delivery availability.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Customer identifier to validate (optional if first_name and last_name are provided)",
                        },
                        "first_name": {
                            "type": "string",
                            "description": "First name for user search or additional validation (required if user_id not provided)",
                        },
                        "last_name": {
                            "type": "string",
                            "description": "Last name for user search or additional validation (required if user_id not provided)",
                        },
                    },
                    "anyOf": [
                        {"required": ["user_id"]},
                        {"required": ["first_name", "last_name"]},
                    ],
                },
            },
        }


class CancelOrder(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str,
        order_id: str,
        cancellation_reason: str = "customer_request",
    ) -> str:
        """
        Cancel a customer order and process refund if applicable

        Writes to: orders.json (updates order status to cancelled)
        Data Sources: users.json for validation
        """
        # Rule: Validate user identity exists before processing any user requests
        users = data.get("users", [])
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            payload = {"error": f"User {user_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Find the order to cancel
        orders = data.get("orders", [])
        order_to_cancel = None
        order_index = None

        for i, order in enumerate(orders):
            if order.get("order_id") == order_id and order.get("user_id") == user_id:
                order_to_cancel = order
                order_index = i
                break

        if not order_to_cancel:
            payload = {
                "error": f"Order {order_id} not found or does not belong to user {user_id}",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        current_status = order_to_cancel.get("status")

        # Rule: Only process orders with valid status - can't cancel delivered orders
        if current_status == "cancelled":
            payload = {"error": f"Order {order_id} is already cancelled", "status": "failed"}
            out = json.dumps(payload)
            return out

        if current_status == "delivered":
            payload = {
                "error": f"Cannot cancel delivered order {order_id}. Please contact customer service for returns.",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Calculate refund amount from payment history
        payment_history = order_to_cancel.get("payment_history", [])
        total_paid = sum(
            payment.get("amount", 0)
            for payment in payment_history
            if payment.get("transaction_type") == "payment"
        )

        # WRITE OPERATION: Update order status to cancelled
        order_to_cancel["status"] = "cancelled"
        order_to_cancel["cancellation_info"] = {
            "cancelled_by": "customer",
            "cancellation_reason": cancellation_reason,
            "cancelled_date": datetime.now().isoformat(),
            "previous_status": current_status,
        }

        # Add refund transaction to payment history
        if total_paid > 0:
            refund_transaction = {
                "transaction_type": "refund",
                "amount": total_paid,
                "refund_reason": "order_cancellation",
                "processed_date": datetime.now().isoformat(),
            }
            order_to_cancel["payment_history"].append(refund_transaction)

        order_to_cancel["last_updated"] = datetime.now().isoformat()

        # Update the order in the data structure
        data["orders"][order_index] = order_to_cancel

        result = {
            "status": "success",
            "order_id": order_id,
            "user_id": user_id,
            "cancellation_status": "cancelled",
            "previous_order_status": current_status,
            "refund_info": {
                "refund_amount": total_paid,
                "refund_processed": total_paid > 0,
            },
            "cancellation_reason": cancellation_reason,
            "cancelled_date": order_to_cancel["cancellation_info"]["cancelled_date"],
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CancelOrder",
                "description": "Cancel a customer order and process refund",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Customer identifier",
                        },
                        "order_id": {
                            "type": "string",
                            "description": "Order identifier to cancel",
                        },
                        "cancellation_reason": {
                            "type": "string",
                            "description": "Reason for cancellation (optional)",
                        },
                    },
                    "required": ["user_id", "order_id"],
                },
            },
        }


class UpdateDeliveryAddress(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], user_id: str, order_id: str, new_address: dict[str, str]
    ) -> str:
        """
        Update delivery address for an existing order (if not yet shipped)

        Writes to: orders.json (updates order address)
        Data Sources: couriers.json for delivery validation
        """
        # Rule: Validate user identity exists before processing any user requests
        users = data.get("users", [])
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            payload = {"error": f"User {user_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Find the order to update
        orders = data.get("orders", [])
        order_to_update = None
        order_index = None

        for i, order in enumerate(orders):
            if order.get("order_id") == order_id and order.get("user_id") == user_id:
                order_to_update = order
                order_index = i
                break

        if not order_to_update:
            payload = {
                "error": f"Order {order_id} not found or does not belong to user {user_id}",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        current_status = order_to_update.get("status")

        # Can only update address for pending orders
        if current_status not in ["pending"]:
            payload = {
                "error": f"Cannot update address for order with status '{current_status}'. Address can only be changed for pending orders.",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Rule: Validate all required address fields: address1, city, country, state, zip
        required_fields = ["address1", "city", "country", "state", "zip"]
        missing_fields = []

        for field in required_fields:
            if not new_address.get(field):
                missing_fields.append(field)

        if missing_fields:
            payload = {
                "error": f"Missing required address fields: {', '.join(missing_fields)}",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Rule: Assign couriers only if destination country matches their coverage areas
        couriers = data.get("couriers", [])
        supported_countries = set()
        for courier in couriers:
            supported_countries.update(courier.get("coverage_area", []))

        destination_country = new_address.get("country")
        if destination_country not in supported_countries:
            payload = {
                "error": f"No delivery service available to {destination_country}",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # WRITE OPERATION: Update order address
        old_address = order_to_update.get("address", {})
        order_to_update["address"] = new_address
        order_to_update["address_updated"] = {
            "updated_date": datetime.now().isoformat(),
            "updated_by": "customer",
            "previous_address": old_address,
        }
        order_to_update["last_updated"] = datetime.now().isoformat()

        # Update the order in the data structure
        data["orders"][order_index] = order_to_update

        result = {
            "status": "success",
            "order_id": order_id,
            "user_id": user_id,
            "address_update": {
                "previous_address": old_address,
                "new_address": new_address,
                "delivery_available": True,
                "destination_country": destination_country,
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
                "name": "UpdateDeliveryAddress",
                "description": "Update delivery address for a pending order",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Customer identifier",
                        },
                        "order_id": {
                            "type": "string",
                            "description": "Order identifier to update",
                        },
                        "new_address": {
                            "type": "object",
                            "properties": {
                                "address1": {"type": "string"},
                                "address2": {"type": "string"},
                                "city": {"type": "string"},
                                "country": {"type": "string"},
                                "state": {"type": "string"},
                                "zip": {"type": "string"},
                            },
                            "required": ["address1", "city", "country", "state", "zip"],
                            "description": "New delivery address",
                        },
                    },
                    "required": ["user_id", "order_id", "new_address"],
                },
            },
        }


class AddPaymentMethod(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str,
        payment_type: str,
        payment_details: dict[str, Any],
    ) -> str:
        """
        Add a new payment method to customer account

        Writes to: users.json (adds new payment method to user)
        """
        pass
        #Rule: Validate user identity exists before processing any user requests
        users = data.get("users", [])
        user_to_update = None
        user_index = None

        for i, user in enumerate(users):
            if user.get("user_id") == user_id:
                user_to_update = user
                user_index = i
                break

        if not user_to_update:
            payload = {"error": f"User {user_id} not found", "status": "failed"}
            out = json.dumps(
                payload)
            return out

        #Rule: Payment methods must be valid type: credit_card, paypal, or gift_card
        if payment_type not in ["credit_card", "paypal", "gift_card"]:
            payload = {
                    "error": f"Invalid payment type '{payment_type}'. Valid types: credit_card, paypal, gift_card",
                    "status": "failed",
                }
            out = json.dumps(
                payload)
            return out

        #Generate unique payment method ID
        existing_payment_methods = user_to_update.get("payment_methods", {})
        method_count = len(existing_payment_methods) + 1
        new_payment_id = f"{payment_type}_{method_count}{user_id.split('_')[-1]}"

        #Validate payment details based on type
        new_payment_method = {
            "source": payment_type,
            "id": new_payment_id,
        }

        if payment_type == "credit_card":
            #Rule: Credit card payments must validate last_four digits and brand type
            required_fields = ["brand", "last_four"]
            for field in required_fields:
                if field not in payment_details:
                    payload = {
                            "error": f"Missing required field '{field}' for credit card",
                            "status": "failed",
                        }
                    out = json.dumps(
                        payload)
                    return out

            if payment_details["brand"] not in ["visa", "mastercard", "amex"]:
                payload = {
                        "error": f"Invalid card brand '{payment_details['brand']}'",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out

            new_payment_method["brand"] = payment_details["brand"]
            new_payment_method["last_four"] = payment_details["last_four"]

        elif payment_type == "gift_card":
            #Rule: Gift card payments cannot exceed available balance
            balance = payment_details.get("balance", 0)
            if balance < 0:
                payload = {
                        "error": "Gift card balance cannot be negative",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out
            new_payment_method["balance"] = balance

        #WRITE OPERATION: Add new payment method to users.json
        if "payment_methods" not in user_to_update:
            user_to_update["payment_methods"] = {}

        user_to_update["payment_methods"][new_payment_id] = new_payment_method
        user_to_update["last_updated"] = datetime.now().isoformat()

        #Update the user in the data structure
        data["users"][user_index] = user_to_update

        result = {
            "status": "success",
            "user_id": user_id,
            "payment_method_added": {
                "payment_method_id": new_payment_id,
                "payment_type": payment_type,
                "details": new_payment_method,
            },
            "total_payment_methods": len(user_to_update["payment_methods"]),
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddPaymentMethod",
                "description": "Add a new payment method to customer account",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Customer identifier",
                        },
                        "payment_type": {
                            "type": "string",
                            "description": "Payment method type (credit_card, paypal, gift_card)",
                        },
                        "payment_details": {
                            "type": "object",
                            "description": "Payment method details (brand/last_four for credit_card, balance for gift_card)",
                        },
                    },
                    "required": ["user_id", "payment_type", "payment_details"],
                },
            },
        }


class UpdateUserProfile(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        user_id: str, 
        profile_updates: dict[str, Any]
    ) -> str:
        """
        Update customer profile information (name, email, default address)

        Writes to: users.json (updates user profile fields)
        """
        pass
        # Rule: Validate user identity exists before processing any user requests
        users = data.get("users", [])
        user_to_update = None
        user_index = None

        for i, user in enumerate(users):
            if user.get("user_id") == user_id:
                user_to_update = user
                user_index = i
                break

        if not user_to_update:
            payload = {"error": f"User {user_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Track what was updated
        updates_applied = {}

        # Update name if provided
        if "name" in profile_updates:
            name_update = profile_updates["name"]
            if isinstance(name_update, dict):
                if "first_name" in name_update or "last_name" in name_update:
                    old_name = user_to_update.get("name", {})
                    new_name = old_name.copy()

                    if "first_name" in name_update:
                        new_name["first_name"] = name_update["first_name"]
                    if "last_name" in name_update:
                        new_name["last_name"] = name_update["last_name"]

                    user_to_update["name"] = new_name
                    updates_applied["name"] = {"old": old_name, "new": new_name}

        # Update email if provided
        if "email" in profile_updates:
            new_email = profile_updates["email"]
            if "@" not in new_email:
                payload = {"error": "Invalid email format", "status": "failed"}
                out = json.dumps(payload)
                return out

            old_email = user_to_update.get("email")
            user_to_update["email"] = new_email
            updates_applied["email"] = {"old": old_email, "new": new_email}

        # Update address if provided
        if "address" in profile_updates:
            address_update = profile_updates["address"]
            if isinstance(address_update, dict):
                # Rule: Validate all required address fields: address1, city, country, state, zip
                required_fields = ["address1", "city", "country", "state", "zip"]
                missing_fields = []

                for field in required_fields:
                    if field in address_update and not address_update.get(field):
                        missing_fields.append(field)

                if missing_fields:
                    payload = {
                        "error": f"Invalid address fields: {', '.join(missing_fields)} cannot be empty",
                        "status": "failed",
                    }
                    out = json.dumps(payload)
                    return out

                old_address = user_to_update.get("address", {})
                new_address = old_address.copy()
                new_address.update(address_update)

                user_to_update["address"] = new_address
                updates_applied["address"] = {"old": old_address, "new": new_address}

        if not updates_applied:
            payload = {
                "error": "No valid updates provided. Supported fields: name, email, address",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # WRITE OPERATION: Update user profile in users.json
        user_to_update["profile_updated"] = datetime.now().isoformat()
        user_to_update["last_updated"] = datetime.now().isoformat()

        # Update the user in the data structure
        data["users"][user_index] = user_to_update

        result = {
            "status": "success",
            "user_id": user_id,
            "updates_applied": updates_applied,
            "total_updates": len(updates_applied),
            "profile_updated": user_to_update["profile_updated"],
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateUserProfile",
                "description": "Update customer profile information",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Customer identifier",
                        },
                        "profile_updates": {
                            "type": "object",
                            "properties": {
                                "name": {
                                    "type": "object",
                                    "properties": {
                                        "first_name": {"type": "string"},
                                        "last_name": {"type": "string"},
                                    },
                                },
                                "email": {"type": "string"},
                                "address": {
                                    "type": "object",
                                    "properties": {
                                        "address1": {"type": "string"},
                                        "address2": {"type": "string"},
                                        "city": {"type": "string"},
                                        "country": {"type": "string"},
                                        "state": {"type": "string"},
                                        "zip": {"type": "string"},
                                    },
                                },
                            },
                            "description": "Profile fields to update",
                        },
                    },
                    "required": ["user_id", "profile_updates"],
                },
            },
        }


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
                    "oneOf": [
                        {"required": ["return_items", "return_reason"]},
                        {"required": ["item_id"]},
                    ],
                },
            },
        }


class GetPurchasedItems(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, order_id: str = None) -> str:
        """
        Retrieve detailed list of purchased items from a specific order

        Data Sources: orders.json (order items), products.json (additional product details), users.json (user validation)
        """
        if not user_id or not order_id:
            payload = {"error": "user_id and order_id are required", "status": "failed"}
            out = json.dumps(payload)
            return out
            
        # Rule: Validate user identity exists before processing any user requests
        users = data.get("users", [])
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            payload = {"error": f"User {user_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Find the specific order
        orders = data.get("orders", [])
        target_order = None

        for order in orders:
            if order.get("order_id") == order_id and order.get("user_id") == user_id:
                target_order = order
                break

        if not target_order:
            payload = {
                "error": f"Order {order_id} not found or does not belong to user {user_id}",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Get order details
        order_status = target_order.get("status")
        order_timestamp = target_order.get("timestamp")
        order_items = target_order.get("items", [])
        payment_history = target_order.get("payment_history", [])
        fulfillments = target_order.get("fulfillments", [])

        if not order_items:
            payload = {"error": f"No items found in order {order_id}", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Enrich item details with additional product information
        products = data.get("products", [])
        detailed_items = []
        total_order_value = 0.0

        for order_item in order_items:
            item_id = order_item.get("item_id")
            product_id = order_item.get("product_id")
            item_price = order_item.get("price", 0)
            item_name = order_item.get("name")
            item_options = order_item.get("options", {})

            # Find additional product details from products.json
            additional_details = {}
            for product in products:
                if product.get("product_id") == product_id:
                    variants = product.get("variants", {})
                    if item_id in variants:
                        variant_info = variants[item_id]
                        additional_details = {
                            "current_availability": variant_info.get("available", False),
                            "current_price": variant_info.get("price", 0),
                            "full_options": variant_info.get("options", {}),
                            "supplier_id": product.get("supplier_id"),
                        }
                    break

            # Calculate if price has changed since purchase
            current_price = additional_details.get("current_price", item_price)
            price_change = (
                current_price - item_price if current_price != item_price else 0
            )

            # Build comprehensive item details
            item_detail = {
                "item_id": item_id,
                "product_id": product_id,
                "product_name": item_name,
                "purchase_details": {
                    "purchased_price": item_price,
                    "purchased_options": item_options,
                    "purchase_date": order_timestamp,
                },
                "current_details": {
                    "current_price": current_price,
                    "price_change": round(price_change, 2),
                    "currently_available": additional_details.get(
                        "current_availability", False
                    ),
                    "supplier_id": additional_details.get("supplier_id"),
                },
                "product_specifications": additional_details.get(
                    "full_options", item_options
                ),
            }

            detailed_items.append(item_detail)
            total_order_value += item_price

        # Calculate order summary information
        total_paid = sum(
            payment.get("amount", 0)
            for payment in payment_history
            if payment.get("transaction_type") == "payment"
        )
        total_refunded = sum(
            payment.get("amount", 0)
            for payment in payment_history
            if payment.get("transaction_type") == "refund"
        )

        # Get tracking information if available
        tracking_info = []
        for fulfillment in fulfillments:
            tracking_info.append(
                {
                    "tracking_id": fulfillment.get("tracking_id"),
                    "courier_name": fulfillment.get("courier_name"),
                    "courier_id": fulfillment.get("courier_id"),
                    "status": fulfillment.get("status"),
                    "timestamp": fulfillment.get("timestamp"),
                }
            )

        # Rule: Maintain data integrity: order totals must match sum of item prices
        price_integrity_check = abs(total_order_value - total_paid + total_refunded) < 0.01

        result = {
            "status": "success",
            "order_info": {
                "order_id": order_id,
                "user_id": user_id,
                "order_status": order_status,
                "order_date": order_timestamp,
                "delivery_address": target_order.get("address", {}),
            },
            "financial_summary": {
                "total_order_value": round(total_order_value, 2),
                "total_paid": round(total_paid, 2),
                "total_refunded": round(total_refunded, 2),
                "net_amount": round(total_paid - total_refunded, 2),
                "price_integrity_verified": price_integrity_check,
            },
            "purchased_items": {
                "total_items": len(detailed_items),
                "items": detailed_items,
            },
            "fulfillment_info": {
                "tracking_available": len(tracking_info) > 0,
                "tracking_details": tracking_info,
            },
            "returns_info": {
                "returns_requested": "returns" in target_order,
                "return_requests": target_order.get("returns", []),
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
                "name": "GetPurchasedItems",
                "description": "Retrieve detailed list of purchased items from a specific customer order",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Customer identifier",
                        },
                        "order_id": {
                            "type": "string",
                            "description": "Order identifier to retrieve items from",
                        },
                    },
                    "required": ["user_id", "order_id"],
                },
            },
        }


class GetCourier(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], tracking_id: str) -> str:
        """
        Get courier ID based on tracking ID

        Data Sources: couriers.json (courier tracking pools)
        """
        if not tracking_id or not tracking_id.strip():
            payload = {"error": "Tracking ID is required", "status": "failed"}
            out = json.dumps(payload)
            return out

        tracking_id = tracking_id.strip()

        # Find which courier has this tracking ID
        couriers = data.get("couriers", [])

        for courier in couriers:
            courier_tracking_ids = courier.get("tracking_ids", [])
            if tracking_id in courier_tracking_ids:
                result = {
                    "status": "success",
                    "tracking_id": tracking_id,
                    "courier_id": courier.get("courier_id"),
                }
                payload = result
                out = json.dumps(payload)
                return out
        payload = {"error": f"Tracking ID {tracking_id} not found", "status": "not_found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCourier",
                "description": "Get courier ID based on tracking ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {
                            "type": "string",
                            "description": "Package tracking identifier",
                        }
                    },
                    "required": ["tracking_id"],
                },
            },
        }


class VerifyGiftCardBalance(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], first_name: str, last_name: str, user_id: str
    ) -> str:
        """
        Verify gift card balance using customer name and user ID authentication

        Data Sources: users.json (user verification and gift card balances)
        """
        _first_nameL = first_name or ''.lower()
        _last_nameL = last_name or ''.lower()
        pass
        if not first_name or not last_name or not user_id:
            payload = {
                    "error": "First name, last name, and user ID are required",
                    "status": "failed",
                }
            out = json.dumps(
                payload)
            return out

        #Rule: Validate user identity exists before processing any user requests
        users = data.get("users", [])
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            payload = {"error": f"User {user_id} not found", "status": "failed"}
            out = json.dumps(
                payload)
            return out

        #Verify name matches user record
        user_name = user.get("name", {})
        stored_first_name = user_name.get("first_name", "").lower().strip()
        stored_last_name = user_name.get("last_name", "").lower().strip()

        provided_first_name = first_name.lower().strip()
        provided_last_name = last_name.lower().strip()

        if (
            stored_first_name != provided_first_name
            or stored_last_name != provided_last_name
        ):
            payload = {
                    "error": "Name verification failed. Please check your first and last name.",
                    "status": "authentication_failed",
                }
            out = json.dumps(
                payload)
            return out

        #Rule: Payment methods must be valid type: credit_card, paypal, or gift_card
        payment_methods = user.get("payment_methods", {})
        gift_cards = []

        for method_id, method_details in payment_methods.items():
            if method_details.get("source") == "gift_card":
                balance = method_details.get("balance", 0)
                gift_cards.append(
                    {
                        "gift_card_id": method_id,
                        "balance": balance,
                        "last_updated": method_details.get("last_updated", "N/A"),
                    }
                )

        if not gift_cards:
            payload = {
                    "status": "success",
                    "user_id": user_id,
                    "customer_name": f"{first_name} {last_name}",
                    "gift_cards_found": 0,
                    "message": "No gift cards found for this account",
                }
            out = json.dumps(
                payload)
            return out

        #Calculate total gift card balance
        total_balance = sum(card["balance"] for card in gift_cards)

        result = {
            "status": "success",
            "user_id": user_id,
            "customer_name": f"{first_name} {last_name}",
            "gift_cards_found": len(gift_cards),
            "total_balance": round(total_balance, 2),
            "gift_cards": gift_cards,
            "verification_timestamp": datetime.now().isoformat(),
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "VerifyGiftCardBalance",
                "description": "Verify gift card balance using customer name and user ID authentication",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {
                            "type": "string",
                            "description": "Customer's first name",
                        },
                        "last_name": {
                            "type": "string",
                            "description": "Customer's last name",
                        },
                        "user_id": {
                            "type": "string",
                            "description": "Customer identifier",
                        },
                    },
                    "required": ["first_name", "last_name", "user_id"],
                },
            },
        }


class CheckOrderStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str) -> str:
        """
        Check order status and details based on order ID

        Data Sources: orders.json (order status, fulfillment, payment info)
        """
        if not order_id or not order_id.strip():
            payload = {"error": "Order ID is required", "status": "failed"}
            out = json.dumps(payload)
            return out

        order_id = order_id.strip()

        # Add # prefix if not provided (for convenience)
        if not order_id.startswith("#"):
            order_id = f"#{order_id}"

        # Find the order
        orders = data.get("orders", [])
        target_order = None

        for order in orders:
            if order.get("order_id") == order_id:
                target_order = order
                break

        if not target_order:
            payload = {"error": f"Order {order_id} not found", "status": "not_found"}
            out = json.dumps(payload)
            return out

        # Rule: Only process orders with valid status: pending, processed, delivered, cancelled
        order_status = target_order.get("status")
        order_timestamp = target_order.get("timestamp")
        user_id = target_order.get("user_id")

        # Get fulfillment information
        fulfillments = target_order.get("fulfillments", [])
        tracking_info = None
        if fulfillments:
            latest_fulfillment = fulfillments[-1]  # Get most recent fulfillment
            tracking_info = {
                "tracking_id": latest_fulfillment.get("tracking_id"),
                "courier_id": latest_fulfillment.get("courier_id"),
                "courier_name": latest_fulfillment.get("courier_name"),
                "fulfillment_status": latest_fulfillment.get("status"),
                "timestamp": latest_fulfillment.get("timestamp"),
            }

        # Get payment information
        payment_history = target_order.get("payment_history", [])
        total_paid = sum(
            payment.get("amount", 0)
            for payment in payment_history
            if payment.get("transaction_type") == "payment"
        )
        total_refunded = sum(
            payment.get("amount", 0)
            for payment in payment_history
            if payment.get("transaction_type") == "refund"
        )

        # Get order items summary
        order_items = target_order.get("items", [])
        items_summary = {
            "total_items": len(order_items),
            "item_names": [item.get("name") for item in order_items],
            "item_ids": [item.get("item_id") for item in order_items],
        }

        # Get delivery address
        delivery_address = target_order.get("address", {})

        # Check for cancellation info
        cancellation_info = target_order.get("cancellation_info")

        # Check for returns
        returns = target_order.get("returns", [])
        return_info = None
        if returns:
            return_info = {
                "return_requests": len(returns),
                "latest_return": returns[-1] if returns else None,
            }

        result = {
            "status": "success",
            "order_id": order_id,
            "order_details": {
                "user_id": user_id,
                "order_status": order_status,
                "order_date": order_timestamp,
                "last_updated": target_order.get("last_updated", order_timestamp),
            },
            "items_summary": items_summary,
            "payment_info": {
                "total_paid": round(total_paid, 2),
                "total_refunded": round(total_refunded, 2),
                "net_amount": round(total_paid - total_refunded, 2),
            },
            "delivery_info": {"address": delivery_address, "tracking": tracking_info},
            "cancellation_info": cancellation_info,
            "return_info": return_info,
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckOrderStatus",
                "description": "Check order status and details based on order ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Order identifier (e.g., 'W6893533' or '#W6893533')",
                        }
                    },
                    "required": ["order_id"],
                },
            },
        }


class GetUserInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        """
        Get basic user information
        Data Sources: users.json (user_id, name, email, address)
        """
        users = data.get("users", [])
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            payload = {"error": f"User {user_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        payload = {
            "status": "success",
            "user_id": user_id,
            "name": user.get("name", {}),
            "email": user.get("email", ""),
            "address": user.get("address", {}),
            "total_orders": len(user.get("orders", [])),
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getUserInfo",
                "description": "Get basic user information",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "User identifier (e.g., 'liam_wilson_6720')",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }


class GetProductInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], item_id: str) -> str:
        """
        Get basic product information by item ID
        Data Sources: products.json
        """
        products = data.get("products", [])
        for product in products:
            variants = product.get("variants", {})
            if item_id in variants:
                variant = variants[item_id]
                payload = {
                    "status": "success",
                    "item_id": item_id,
                    "product_id": product.get("product_id"),
                    "product_name": product.get("name"),
                    "price": variant.get("price"),
                    "available": variant.get("available"),
                    "options": variant.get("options", {}),
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Item {item_id} not found", "status": "failed"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductInfo",
                "description": "Get basic product information by item ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {
                            "type": "string",
                            "description": "Product item identifier (e.g., 'ITEM12345')",
                        }
                    },
                    "required": ["item_id"],
                },
            },
        }


class CheckUserPaymentMethods(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        """
        List user's available payment methods
        Data Sources: users.json (payment_methods)
        """
        users = data.get("users", [])
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            payload = {"error": f"User {user_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        payment_methods = user.get("payment_methods", {})
        method_list = []

        for method_id, method_info in payment_methods.items():
            method_data = {
                "payment_method_id": method_id,
                "source": method_info.get("source"),
            }
            if method_info.get("source") == "credit_card":
                method_data["brand"] = method_info.get("brand")
                method_data["last_four"] = method_info.get("last_four")
            elif method_info.get("source") == "gift_card":
                method_data["balance"] = method_info.get("balance")

            method_list.append(method_data)
        payload = {
            "status": "success",
            "user_id": user_id,
            "payment_methods": method_list,
            "total_methods": len(method_list),
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckUserPaymentMethods",
                "description": "List user's available payment methods",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "User identifier (e.g., 'liam_wilson_6720')",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }


class UpdateSupplierInfo(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        supplier_id: str,
        contact_updates: dict[str, str] = None,
        performance_rating: float = None,
        notes: str = None,
    ) -> str:
        """
        Update supplier contact information and performance metrics

        Writes to: suppliers.json (updates existing supplier contact_info and adds performance data)
        Data Sources: suppliers.json (supplier_id, name, contact_info)
        """
        suppliers = data.get("suppliers", [])
        supplier_to_update = None
        supplier_index = None

        # Find the supplier
        for i, supplier in enumerate(suppliers):
            if supplier.get("supplier_id") == supplier_id:
                supplier_to_update = supplier
                supplier_index = i
                break

        if not supplier_to_update:
            payload = {"error": f"Supplier {supplier_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        # WRITE OPERATION: Update supplier information
        updates_applied = []

        if contact_updates:
            current_contact = supplier_to_update.get("contact_info", {})

            if "phone" in contact_updates:
                current_contact["phone"] = contact_updates["phone"]
                updates_applied.append("phone")

            if "email" in contact_updates:
                current_contact["email"] = contact_updates["email"]
                updates_applied.append("email")

            supplier_to_update["contact_info"] = current_contact

        # Add performance tracking
        if performance_rating is not None:
            if not (0.0 <= performance_rating <= 5.0):
                payload = {
                    "error": "Performance rating must be between 0.0 and 5.0",
                    "status": "failed",
                }
                out = json.dumps(payload)
                return out

            if "performance_metrics" not in supplier_to_update:
                supplier_to_update["performance_metrics"] = {}

            supplier_to_update["performance_metrics"]["rating"] = performance_rating
            supplier_to_update["performance_metrics"][
                "last_updated"
            ] = datetime.now().isoformat()
            updates_applied.append("performance_rating")

        if notes:
            supplier_to_update["notes"] = notes
            updates_applied.append("notes")

        supplier_to_update["last_updated"] = datetime.now().isoformat()

        # Update the supplier in the data structure
        data["suppliers"][supplier_index] = supplier_to_update

        result = {
            "status": "success",
            "supplier_id": supplier_id,
            "supplier_name": supplier_to_update.get("name"),
            "updates_applied": updates_applied,
            "updated_contact_info": supplier_to_update.get("contact_info", {}),
            "performance_rating": supplier_to_update.get("performance_metrics", {}).get(
                "rating"
            ),
            "last_updated": supplier_to_update["last_updated"],
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateSupplierInfo",
                "description": "Update supplier contact information and performance metrics",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier identifier (e.g., '#SUP0001')",
                        },
                        "contact_updates": {
                            "type": "object",
                            "properties": {
                                "phone": {"type": "string"},
                                "email": {"type": "string"},
                            },
                            "description": "Contact information updates",
                        },
                        "performance_rating": {
                            "type": "number",
                            "description": "Performance rating between 0.0 and 5.0",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Additional notes about supplier",
                        },
                    },
                    "required": ["supplier_id"],
                },
            },
        }


class UpdateInventoryStock(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        supplier_id: str,
        item_id: str = None,
        item_ids: list[str] = None,
        new_stock_level: int = None,
        new_stock_levels: list[int] = None,
        stock_action: str = "set",
        exclude_unavailable: bool = False,
    ) -> str:
        """
        Update inventory stock levels for supplier items (single item or batch update)
        Optionally excludes non-available items from processing

        Writes to: suppliers.json (updates item_stock levels)
        Data Sources: suppliers.json (supplier_id, item_stock), products.json (item availability)
        """
        pass
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

        #Handle stock levels - can be single value or list
        stock_levels_list = []
        if new_stock_level is not None and new_stock_levels is not None:
            payload = {
                    "error": "Cannot specify both new_stock_level and new_stock_levels. Use one or the other.",
                    "status": "failed",
                }
            out = json.dumps(
                payload)
            return out
        elif new_stock_level is not None:
            if new_stock_level < 0:
                payload = {"error": "Stock level cannot be negative", "status": "failed"}
                out = json.dumps(
                    payload)
                return out
            #Single stock level for all items
            stock_levels_list = [new_stock_level] * len(items_to_process)
        elif new_stock_levels is not None:
            if len(new_stock_levels) != len(items_to_process):
                payload = {
                        "error": f"Number of stock levels ({len(new_stock_levels)}) must match number of items ({len(items_to_process)})",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out
            #Validate all stock levels are non-negative
            for i, level in enumerate(new_stock_levels):
                if level < 0:
                    payload = {
                            "error": f"Stock level at index {i} cannot be negative: {level}",
                            "status": "failed",
                        }
                    out = json.dumps(
                        payload)
                    return out
            stock_levels_list = new_stock_levels
        else:
            payload = {
                    "error": "Either new_stock_level or new_stock_levels must be provided",
                    "status": "failed",
                }
            out = json.dumps(
                payload)
            return out

        valid_actions = ["set", "add", "subtract"]
        if stock_action not in valid_actions:
            payload = {
                    "error": f"Invalid stock action '{stock_action}'. Valid actions: {', '.join(valid_actions)}",
                    "status": "failed",
                }
            out = json.dumps(
                payload)
            return out

        suppliers = data.get("suppliers", [])
        supplier_to_update = None
        supplier_index = None

        #Find the supplier
        for i, supplier in enumerate(suppliers):
            if supplier.get("supplier_id") == supplier_id:
                supplier_to_update = supplier
                supplier_index = i
                break

        if not supplier_to_update:
            payload = {"error": f"Supplier {supplier_id} not found", "status": "failed"}
            out = json.dumps(
                payload)
            return out

        #Get product availability information if exclude_unavailable is True
        item_availability_map = {}
        if exclude_unavailable:
            products = data.get("products", [])
            for product in products:
                variants = product.get("variants", {})
                for variant_id, variant_info in variants.items():
                    item_availability_map[variant_id] = variant_info.get(
                        "available", False
                    )

        #Validate all items exist in supplier's stock and filter by availability if needed
        item_stock = supplier_to_update.get("item_stock", {})
        missing_items = []
        unavailable_items = []
        filtered_items = []

        for i, item in enumerate(items_to_process):
            if item not in item_stock:
                missing_items.append(item)
                continue

            #Check availability if exclude_unavailable is True
            if exclude_unavailable:
                is_available = item_availability_map.get(item, False)
                if not is_available:
                    unavailable_items.append(item)
                    continue

            #Item passes all filters
            filtered_items.append((item, stock_levels_list[i]))

        if missing_items:
            payload = {
                    "error": f"Items not found in supplier {supplier_id} inventory: {', '.join(missing_items)}",
                    "status": "failed",
                }
            out = json.dumps(
                payload)
            return out

        if not filtered_items:
            error_message = "No items to process"
            if exclude_unavailable and unavailable_items:
                error_message += f". All items are marked as unavailable: {', '.join(unavailable_items)}"
            payload = {
                    "error": error_message,
                    "status": "failed",
                    "unavailable_items": (
                        unavailable_items if exclude_unavailable else []
                    ),
                }
            out = json.dumps(
                payload)
            return out

        #WRITE OPERATION: Update stock levels for filtered items
        update_results = []
        for item, stock_level_to_apply in filtered_items:
            old_stock = item_stock[item]

            #Handle different stock statuses
            if old_stock in ["discontinued", "out_of_stock"]:
                if stock_action in ["add", "subtract"]:
                    update_results.append(
                        {
                            "item_id": item,
                            "status": "error",
                            "message": f"Cannot modify stock for {old_stock} item",
                            "previous_stock": old_stock,
                            "new_stock": old_stock,  #No change
                        }
                    )
                    continue
                #Allow "set" to restore from discontinued/out_of_stock
                item_stock[item] = stock_level_to_apply
                new_stock_value = stock_level_to_apply
            else:
                #Numeric stock levels
                old_stock_num = (
                    int(old_stock)
                    if isinstance(old_stock, (int, str)) and str(old_stock).isdigit()
                    else 0
                )

                if stock_action == "set":
                    item_stock[item] = stock_level_to_apply
                    new_stock_value = stock_level_to_apply
                elif stock_action == "add":
                    new_value = old_stock_num + stock_level_to_apply
                    item_stock[item] = new_value
                    new_stock_value = new_value
                elif stock_action == "subtract":
                    new_value = max(0, old_stock_num - stock_level_to_apply)
                    item_stock[item] = new_value if new_value > 0 else "out_of_stock"
                    new_stock_value = item_stock[item]

            update_results.append(
                {
                    "item_id": item,
                    "status": "success",
                    "previous_stock": old_stock,
                    "new_stock": new_stock_value,
                    "action_performed": stock_action,
                    "action_value": stock_level_to_apply,
                }
            )

        supplier_to_update["item_stock"] = item_stock
        supplier_to_update["stock_updated"] = datetime.now().isoformat()

        #Update the supplier in the data structure
        data["suppliers"][supplier_index] = supplier_to_update

        #Calculate summary statistics
        successful_updates = [r for r in update_results if r["status"] == "success"]
        failed_updates = [r for r in update_results if r["status"] == "error"]

        result = {
            "status": "success",
            "supplier_id": supplier_id,
            "supplier_name": supplier_to_update.get("name"),
            "filtering_summary": {
                "exclude_unavailable": exclude_unavailable,
                "total_items_requested": len(items_to_process),
                "items_filtered_out": (
                    len(unavailable_items) if exclude_unavailable else 0
                ),
                "unavailable_items": unavailable_items if exclude_unavailable else [],
                "items_processed": len(filtered_items),
            },
            "batch_update_summary": {
                "total_items_processed": len(filtered_items),
                "successful_updates": len(successful_updates),
                "failed_updates": len(failed_updates),
                "stock_action": stock_action,
            },
            "update_details": update_results,
            "stock_updated": supplier_to_update["stock_updated"],
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateInventoryStock",
                "description": "Update inventory stock levels for supplier items (single item or batch update). Optionally excludes non-available items from processing.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier identifier (e.g., '#SUP0001')",
                        },
                        "item_id": {
                            "type": "string",
                            "description": "Single item identifier (optional if using item_ids)",
                        },
                        "item_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of item identifiers for batch update (optional if using item_id)",
                        },
                        "new_stock_level": {
                            "type": "integer",
                            "description": "New stock level for single item or all items (optional if using new_stock_levels)",
                        },
                        "new_stock_levels": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "List of stock levels corresponding to each item in item_ids (optional if using new_stock_level)",
                        },
                        "stock_action": {
                            "type": "string",
                            "description": "Action: 'set', 'add', or 'subtract'",
                            "default": "set",
                        },
                        "exclude_unavailable": {
                            "type": "boolean",
                            "description": "Optional flag to exclude items marked as unavailable in the product catalog from stock updates",
                            "default": False,
                        },
                    },
                    "required": ["supplier_id"],
                },
            },
        }


class UpdateSupplyOrderTerms(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        supply_order_id: str,
        new_unit_cost: float = None,
        payment_terms: str = None,
        delivery_deadline: str = None,
    ) -> str:
        """
        Update supply order terms and conditions

        Writes to: supply_orders.json (updates existing supply order terms)
        Data Sources: supply_orders.json (supply_order_id, unit_cost, quantity)
        """
        if new_unit_cost is not None and new_unit_cost < 0:
            payload = {"error": "Unit cost cannot be negative", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Find the supply order to update
        supply_orders = data.get("supply_orders", [])
        supply_order_to_update = None
        order_index = None

        for i, order in enumerate(supply_orders):
            if order.get("supply_order_id") == supply_order_id:
                supply_order_to_update = order
                order_index = i
                break

        if not supply_order_to_update:
            payload = {
                "error": f"Supply order {supply_order_id} not found",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Rule: Supply orders with status 'cancelled' require alternative sourcing and cannot be fulfilled
        current_status = supply_order_to_update.get("status")
        if current_status == "fulfilled":
            payload = {
                "error": f"Cannot modify terms for fulfilled supply order {supply_order_id}",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # WRITE OPERATION: Update supply order terms
        updates_applied = []
        old_unit_cost = supply_order_to_update.get("unit_cost", 0)
        quantity = supply_order_to_update.get("quantity", 0)

        if new_unit_cost is not None:
            supply_order_to_update["unit_cost"] = new_unit_cost
            supply_order_to_update["total_cost"] = round(new_unit_cost * quantity, 2)
            updates_applied.append("unit_cost")
            updates_applied.append("total_cost")

        if payment_terms:
            supply_order_to_update["payment_terms"] = payment_terms
            updates_applied.append("payment_terms")

        if delivery_deadline:
            supply_order_to_update["delivery_deadline"] = delivery_deadline
            updates_applied.append("delivery_deadline")

        supply_order_to_update["terms_updated"] = datetime.now().isoformat()

        # Update the supply order in the data structure
        data["supply_orders"][order_index] = supply_order_to_update

        result = {
            "status": "success",
            "supply_order_id": supply_order_id,
            "supplier_id": supply_order_to_update.get("supplier_id"),
            "item_id": supply_order_to_update.get("item_id"),
            "product_id": supply_order_to_update.get("product_id"),
            "updates_applied": updates_applied,
            "cost_changes": (
                {
                    "previous_unit_cost": old_unit_cost,
                    "new_unit_cost": supply_order_to_update.get("unit_cost"),
                    "new_total_cost": supply_order_to_update.get("total_cost"),
                }
                if new_unit_cost is not None
                else None
            ),
            "terms_updated": supply_order_to_update["terms_updated"],
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateSupplyOrderTerms",
                "description": "Update supply order terms and conditions",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {
                            "type": "string",
                            "description": "Supply order identifier (e.g., '#SO9359')",
                        },
                        "new_unit_cost": {
                            "type": "number",
                            "description": "New unit cost",
                        },
                        "payment_terms": {
                            "type": "string",
                            "description": "Payment terms (e.g., 'NET30', 'COD')",
                        },
                        "delivery_deadline": {
                            "type": "string",
                            "description": "Delivery deadline (ISO format)",
                        },
                    },
                    "required": ["supply_order_id"],
                },
            },
        }

#=== READ OPERATIONS ===


class GetSupplierDetails(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        supplier_id: str,
        name: str = None,
        contact_info: dict[str, Any] = None,
        performance_metrics: dict[str, Any] = None,
        notes: str = "",
        products: list[str] = None,
        item_stock: dict[str, Any] = None,
        last_updated: str = "Never"
    ) -> str:
        """
        Retrieve comprehensive supplier information and performance metrics

        Data Sources: suppliers.json (supplier_id, name, contact_info, products, item_stock)
        """
        suppliers = data.get("suppliers", [])
        supplier_found = None

        for supplier in suppliers:
            if supplier.get("supplier_id") == supplier_id:
                supplier_found = supplier
                break

        if not supplier_found:
            payload = {"error": f"Supplier {supplier_id} not found", "status": "not_found"}
            out = json.dumps(payload)
            return out

        # Calculate stock metrics
        item_stock = supplier_found.get("item_stock", {})
        total_items = len(item_stock)
        available_items = 0
        out_of_stock_items = 0
        discontinued_items = 0
        total_stock_value = 0

        for item_id, stock_level in item_stock.items():
            if stock_level == "out_of_stock":
                out_of_stock_items += 1
            elif stock_level == "discontinued":
                discontinued_items += 1
            elif isinstance(stock_level, (int, str)) and str(stock_level).isdigit():
                available_items += 1
                total_stock_value += int(stock_level)

        # Calculate availability rate
        availability_rate = (
            (available_items / total_items * 100) if total_items > 0 else 0
        )

        result = {
            "status": "success",
            "supplier_id": supplier_id,
            "supplier_info": {
                "name": supplier_found.get("name"),
                "contact_info": supplier_found.get("contact_info", {}),
                "performance_metrics": supplier_found.get("performance_metrics", {}),
                "notes": supplier_found.get("notes", ""),
            },
            "product_portfolio": {
                "total_products": len(supplier_found.get("products", [])),
                "product_ids": supplier_found.get("products", []),
            },
            "inventory_summary": {
                "total_items": total_items,
                "available_items": available_items,
                "out_of_stock_items": out_of_stock_items,
                "discontinued_items": discontinued_items,
                "availability_rate_percent": round(availability_rate, 1),
                "total_stock_units": total_stock_value,
            },
            "last_updated": supplier_found.get("last_updated", "Never"),
        }
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSupplierDetails",
                "description": "Retrieve comprehensive supplier information and performance metrics",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier identifier (e.g., '#SUP0001')",
                        }
                    },
                    "required": ["supplier_id"],
                },
            },
        }


class GetSupplyOrderDetails(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        supply_order_id: str,
        supplier_id: str = None,
        product_id: str = None,
        item_id: str = None,
        quantity: int = None,
        status: str = None,
        costs: float = None,
        dates: dict[str, str] = None,
        order_date: str = None,
        unit_cost: float = None,
        total_cost: float = None,
        delivery_date: str = None,
        fulfilled_date: str = None,
        cancelled_date: str = None,
        payment_terms: str = "Standard",
        delivery_deadline: str = None,
        requires_alternative_sourcing: bool = False,
        last_updated: str = None
    ) -> str:
        """
        Retrieve detailed information about a specific supply order

        Data Sources: supply_orders.json (supply_order_id, supplier_id, product_id, item_id, quantity, status, costs, dates)
        """
        supply_orders = data.get("supply_orders", [])
        supply_order_found = None

        for order in supply_orders:
            if order.get("supply_order_id") == supply_order_id:
                supply_order_found = order
                break

        if not supply_order_found:
            payload = {
                    "error": f"Supply order {supply_order_id} not found",
                    "status": "not_found",
                }
            out = json.dumps(
                payload)
            return out

        # Enrich with supplier information
        supplier_id = supply_order_found.get("supplier_id")
        suppliers = data.get("suppliers", [])
        supplier_info = {}

        for supplier in suppliers:
            if supplier.get("supplier_id") == supplier_id:
                supplier_info = {
                    "name": supplier.get("name"),
                    "contact_info": supplier.get("contact_info", {}),
                }
                break

        # Calculate order metrics
        order_date = supply_order_found.get("order_date", "")
        status = supply_order_found.get("status")

        # Calculate days since order
        days_since_order = 0
        if order_date:
            try:
                order_datetime = datetime.fromisoformat(
                    order_date.replace("Z", "+00:00")
                )
                days_since_order = (datetime.now() - order_datetime).days
            except:
                days_since_order = 0

        # Determine urgency based on status and age
        urgency = "normal"
        if status == "pending" and days_since_order > 30:
            urgency = "high"
        elif status == "pending" and days_since_order > 14:
            urgency = "medium"

        result = {
            "status": "success",
            "supply_order_id": supply_order_id,
            "order_details": {
                "supplier_id": supplier_id,
                "supplier_info": supplier_info,
                "product_id": supply_order_found.get("product_id"),
                "item_id": supply_order_found.get("item_id"),
                "quantity": supply_order_found.get("quantity"),
                "unit_cost": supply_order_found.get("unit_cost"),
                "total_cost": supply_order_found.get("total_cost"),
            },
            "order_status": {
                "current_status": status,
                "order_date": order_date,
                "days_since_order": days_since_order,
                "urgency_level": urgency,
                "delivery_date": supply_order_found.get("delivery_date"),
                "fulfilled_date": supply_order_found.get("fulfilled_date"),
                "cancelled_date": supply_order_found.get("cancelled_date"),
            },
            "order_terms": {
                "payment_terms": supply_order_found.get("payment_terms", "Standard"),
                "delivery_deadline": supply_order_found.get("delivery_deadline"),
                "requires_alternative_sourcing": supply_order_found.get(
                    "requires_alternative_sourcing", False
                ),
            },
            "last_updated": supply_order_found.get(
                "last_updated", supply_order_found.get("order_date")
            ),
        }
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSupplyOrderDetails",
                "description": "Retrieve detailed information about a specific supply order",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {
                            "type": "string",
                            "description": "Supply order identifier (e.g., '#SO9359')",
                        }
                    },
                    "required": ["supply_order_id"],
                },
            },
        }


class SearchSuppliersByProduct:
    @staticmethod
    def invoke(
        data: dict[str, Any],
        product_id: str = None,
        item_id: str = None,
        min_stock_level: int = 0,
        exclude_statuses: list[str] = None,
        supplier_id: str = None,
        product_type: list[str] = None,
        stock_level_preference: str = None,
        available_only: bool = False,
    ) -> str:
        """
        Search suppliers by product availability and stock levels with optional product type filtering, stock level preference, and availability filtering

        Data Sources: suppliers.json (supplier_id, name, products, item_stock), products.json (product names for filtering and availability status)
        """
        if exclude_statuses is None:
            exclude_statuses = ["discontinued", "out_of_stock"]

        # Validate stock_level_preference parameter
        if stock_level_preference and stock_level_preference not in [
            "highest",
            "lowest",
        ]:
            payload = {
                "error": "Invalid stock_level_preference. Valid options: 'highest', 'lowest'",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Get product information for type filtering and availability checking
        products = data.get("products", [])
        product_name_map = {}
        item_availability_map = {}

        for product in products:
            product_id_key = product.get("product_id")
            product_name = product.get("name", "").lower()
            variants = product.get("variants", {})

            if product_id_key:
                product_name_map[product_id_key] = product_name

                # Map item availability from product variants
                for variant_id, variant_info in variants.items():
                    item_availability_map[variant_id] = variant_info.get(
                        "available", False
                    )

        # Convert product_type to lowercase for case-insensitive matching
        product_type_lower = []
        if product_type:
            product_type_lower = [ptype.lower() for ptype in product_type]

        # Apply product type filter to the provided product_id if specified
        if product_id and product_type_lower:
            product_name = product_name_map.get(product_id, "")
            if product_name:
                type_matches = any(
                    ptype in product_name for ptype in product_type_lower
                )
                if not type_matches:
                    payload = {
                        "status": "success",
                        "search_criteria": {
                            "product_id": product_id,
                            "item_id": item_id,
                            "min_stock_level": min_stock_level,
                            "excluded_statuses": exclude_statuses,
                            "supplier_id_filter": supplier_id,
                            "product_type_filter": product_type,
                            "stock_level_preference": stock_level_preference,
                            "available_only": available_only,
                            "filter_applied": True,
                        },
                        "total_suppliers_found": 0,
                        "suppliers": [],
                        "message": f"Product {product_id} does not match the specified product type filter",
                    }
                    out = json.dumps(payload)
                    return out

        suppliers = data.get("suppliers", [])
        matching_suppliers = []

        for supplier in suppliers:
            current_supplier_id = supplier.get("supplier_id")
            supplier_name = supplier.get("name")
            supplier_products = supplier.get("products", [])
            item_stock = supplier.get("item_stock", {})

            # Filter by supplier_id if provided
            if supplier_id and current_supplier_id != supplier_id:
                continue

            # Check if supplier has the product
            if product_id and product_id not in supplier_products:
                continue

            # Check item stock if item_id provided
            supplier_match = {
                "supplier_id": current_supplier_id,
                "supplier_name": supplier_name,
                "contact_info": supplier.get("contact_info", {}),
                "matching_items": [],
            }

            if item_id:
                # Specific item search
                if item_id in item_stock:
                    stock_level = item_stock[item_id]

                    # Skip if status is excluded
                    if stock_level in exclude_statuses:
                        continue

                    # Check availability filter ONLY if available_only is True
                    if available_only:
                        item_is_available = item_availability_map.get(item_id, False)
                        if not item_is_available:
                            continue

                    # Check minimum stock level
                    if (
                        isinstance(stock_level, (int, str))
                        and str(stock_level).isdigit()
                    ):
                        if int(stock_level) >= min_stock_level:
                            # Apply product type filtering for item_id search
                            item_matches_type = True
                            if product_type_lower:
                                # Find the product this item belongs to
                                item_product_id = None
                                for prod in products:
                                    if item_id in prod.get("variants", {}):
                                        item_product_id = prod.get("product_id")
                                        break

                                if item_product_id:
                                    item_product_name = product_name_map.get(
                                        item_product_id, ""
                                    )
                                    item_matches_type = any(
                                        ptype in item_product_name
                                        for ptype in product_type_lower
                                    )

                            if item_matches_type:
                                supplier_match["matching_items"].append(
                                    {
                                        "item_id": item_id,
                                        "stock_level": stock_level,
                                        "numeric_stock_level": int(stock_level),
                                        "status": "available",
                                        "product_available": item_availability_map.get(
                                            item_id, False
                                        ),
                                    }
                                )

                    if supplier_match["matching_items"]:
                        matching_suppliers.append(supplier_match)
            else:
                # Product-level search - find all items for this product
                candidate_items = []

                for stock_item_id, stock_level in item_stock.items():
                    # Skip if status is excluded
                    if stock_level in exclude_statuses:
                        continue

                    # Check availability filter ONLY if available_only is True
                    if available_only:
                        item_is_available = item_availability_map.get(
                            stock_item_id, False
                        )
                        if not item_is_available:
                            continue

                    # Check minimum stock level
                    if (
                        isinstance(stock_level, (int, str))
                        and str(stock_level).isdigit()
                    ):
                        if int(stock_level) >= min_stock_level:
                            # Apply product type filtering for each item
                            item_matches_type = True
                            if product_type_lower:
                                # Find the product this item belongs to
                                item_product_id = None
                                for prod in products:
                                    if stock_item_id in prod.get("variants", {}):
                                        item_product_id = prod.get("product_id")
                                        break

                                if item_product_id:
                                    item_product_name = product_name_map.get(
                                        item_product_id, ""
                                    )
                                    item_matches_type = any(
                                        ptype in item_product_name
                                        for ptype in product_type_lower
                                    )

                            if item_matches_type:
                                candidate_items.append(
                                    {
                                        "item_id": stock_item_id,
                                        "stock_level": stock_level,
                                        "numeric_stock_level": int(stock_level),
                                        "status": "available",
                                        "product_available": item_availability_map.get(
                                            stock_item_id, False
                                        ),
                                    }
                                )

                # Apply stock level preference filtering
                if candidate_items and stock_level_preference:
                    if stock_level_preference == "highest":
                        # Find the maximum stock level
                        max_stock = max(
                            item["numeric_stock_level"] for item in candidate_items
                        )
                        candidate_items = [
                            item
                            for item in candidate_items
                            if item["numeric_stock_level"] == max_stock
                        ]
                    elif stock_level_preference == "lowest":
                        # Find the minimum stock level
                        min_stock = min(
                            item["numeric_stock_level"] for item in candidate_items
                        )
                        candidate_items = [
                            item
                            for item in candidate_items
                            if item["numeric_stock_level"] == min_stock
                        ]

                supplier_match["matching_items"] = candidate_items

                if supplier_match["matching_items"]:
                    matching_suppliers.append(supplier_match)

        # Sort by total available stock (descending)
        for supplier in matching_suppliers:
            total_stock = sum(
                item["numeric_stock_level"] for item in supplier["matching_items"]
            )
            supplier["total_available_stock"] = total_stock

        matching_suppliers.sort(key=lambda x: x["total_available_stock"], reverse=True)

        result = {
            "status": "success",
            "search_criteria": {
                "product_id": product_id,
                "item_id": item_id,
                "min_stock_level": min_stock_level,
                "supplier_id_filter": supplier_id,
                "product_type_filter": product_type,
                "available_only": available_only,
                "filter_applied": product_type is not None
                or stock_level_preference is not None
                or available_only,
            },
            "total_suppliers_found": len(matching_suppliers),
            "suppliers": (
                matching_suppliers[:3] if not supplier_id else matching_suppliers
            ),
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchSuppliersByProduct",
                "description": "Search suppliers by product availability and stock levels with optional supplier, product type filtering, stock level preference, and availability filtering",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {
                            "type": "string",
                            "description": "Product identifier to search for",
                        },
                        "item_id": {
                            "type": "string",
                            "description": "Specific item identifier to search for",
                        },
                        "min_stock_level": {
                            "type": "integer",
                            "description": "Minimum stock level required",
                            "default": 0,
                        },
                        "exclude_statuses": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Stock statuses to exclude from results",
                            "default": ["discontinued", "out_of_stock"],
                        },
                        "supplier_id": {
                            "type": "string",
                            "description": "Optional specific supplier ID to filter results (e.g., '#SUP0001')",
                        },
                        "product_type": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional list of product types to filter by (e.g., ['laptop', 'bluetooth speaker', 't-shirt']). Matches product names containing these terms.",
                        },
                        "stock_level_preference": {
                            "type": "string",
                            "description": "Optional preference for stock levels: 'highest' returns items with maximum stock, 'lowest' returns items with minimum stock",
                            "enum": ["highest", "lowest"],
                        },
                        "available_only": {
                            "type": "boolean",
                            "description": "Optional filter to show only items that are marked as available in the product catalog. When not specified, includes all items regardless of availability status.",
                            "default": False,
                        },
                    },
                },
            },
        }

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
        users = data.get("users", [])
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            payload = {"error": f"User {user_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        if not order_ids:
            payload = {"error": "Order IDs list cannot be empty", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Find all specified orders for the user
        orders = data.get("orders", [])
        found_orders = []
        not_found_orders = []

        for order_id in order_ids:
            # Add # prefix if not provided (for convenience)
            formatted_order_id = (
                order_id if order_id.startswith("#") else f"#{order_id}"
            )

            order_found = False
            for order in orders:
                if (
                    order.get("order_id") == formatted_order_id
                    and order.get("user_id") == user_id
                ):
                    found_orders.append(order)
                    order_found = True
                    break

            if not order_found:
                not_found_orders.append(formatted_order_id)

        if not found_orders:
            payload = {
                "error": f"No valid orders found for user {user_id}",
                "not_found_orders": not_found_orders,
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Get product information for filtering
        products = data.get("products", [])
        product_name_map = {}
        for product in products:
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


class GetSupplierByProduct:
    @staticmethod
    def invoke(
        data: dict[str, Any], product_ids: list[str], product_type: list[str] = None
    ) -> str:
        """
        Get suppliers associated with specified product IDs, optionally filtered by product type

        Data Sources: suppliers.json (supplier_id, name, products, contact_info), products.json (product names for filtering)
        """
        if not product_ids:
            payload = {"error": "Product IDs list cannot be empty", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Get product information for type filtering
        products = data.get("products", [])
        product_name_map = {}
        for product in products:
            product_id = product.get("product_id")
            product_name = product.get("name", "").lower()
            if product_id:
                product_name_map[product_id] = product_name

        # Convert product_type to lowercase for case-insensitive matching
        product_type_lower = []
        if product_type:
            product_type_lower = [ptype.lower() for ptype in product_type]

        # Filter product_ids by product_type if specified
        filtered_product_ids = []
        if product_type_lower:
            for product_id in product_ids:
                product_name = product_name_map.get(product_id, "")
                if product_name:
                    type_matches = any(
                        ptype in product_name for ptype in product_type_lower
                    )
                    if type_matches:
                        filtered_product_ids.append(product_id)
        else:
            filtered_product_ids = product_ids

        if not filtered_product_ids:
            payload = {
                "status": "success",
                "search_criteria": {
                    "requested_product_ids": product_ids,
                    "product_type_filter": product_type,
                    "filter_applied": product_type is not None,
                },
                "filtered_product_ids": filtered_product_ids,
                "product_supplier_mapping": {},
                "message": "No products matched the specified product type filter",
            }
            out = json.dumps(payload)
            return out

        suppliers = data.get("suppliers", [])
        matching_suppliers = []
        product_supplier_map = {}

        # Search through all suppliers to find matches for filtered products
        for supplier in suppliers:
            supplier_id = supplier.get("supplier_id")
            supplier_name = supplier.get("name")
            supplier_products = supplier.get("products", [])
            contact_info = supplier.get("contact_info", {})

            # Check which filtered products this supplier has
            matching_products = []
            for product_id in filtered_product_ids:
                if product_id in supplier_products:
                    matching_products.append(product_id)

                    # Build product to supplier mapping
                    if product_id not in product_supplier_map:
                        product_supplier_map[product_id] = []
                    product_supplier_map[product_id].append(
                        {"supplier_id": supplier_id, "supplier_name": supplier_name}
                    )

            # If supplier has any matching products, include them
            if matching_products:
                supplier_info = {
                    "supplier_id": supplier_id,
                    "supplier_name": supplier_name,
                    "contact_info": contact_info,
                    "matching_products": matching_products,
                    "total_matching_products": len(matching_products),
                    "performance_metrics": supplier.get("performance_metrics", {}),
                    "last_updated": supplier.get("last_updated", "Never"),
                }

                # Add stock information for matching products if available
                item_stock = supplier.get("item_stock", {})
                if item_stock:
                    stock_summary = {
                        "total_items_in_stock": len(item_stock),
                        "available_items": 0,
                        "out_of_stock_items": 0,
                        "discontinued_items": 0,
                    }

                    for stock_level in item_stock.values():
                        if stock_level == "out_of_stock":
                            stock_summary["out_of_stock_items"] += 1
                        elif stock_level == "discontinued":
                            stock_summary["discontinued_items"] += 1
                        elif (
                            isinstance(stock_level, (int, str))
                            and str(stock_level).isdigit()
                        ):
                            stock_summary["available_items"] += 1

                    supplier_info["stock_summary"] = stock_summary

                matching_suppliers.append(supplier_info)

        # Find products with no suppliers
        products_not_found = []
        for product_id in filtered_product_ids:
            if product_id not in product_supplier_map:
                products_not_found.append(product_id)

        # Sort suppliers by number of matching products (descending)
        matching_suppliers.sort(
            key=lambda x: x["total_matching_products"], reverse=True
        )

        result = {
            "status": "success",
            "search_criteria": {
                "requested_product_ids": product_ids,
                "product_type_filter": product_type,
                "filter_applied": product_type is not None,
            },
            "filtered_product_ids": filtered_product_ids,
            "supplier_results": {
                "total_suppliers_found": len(matching_suppliers),
                "suppliers": matching_suppliers,
            },
            "product_supplier_mapping": product_supplier_map,
            "products_without_suppliers": products_not_found,
            "coverage_summary": {
                "products_with_suppliers": len(filtered_product_ids)
                - len(products_not_found),
                "products_without_suppliers": len(products_not_found),
                "coverage_percentage": (
                    round(
                        (
                            (len(filtered_product_ids) - len(products_not_found))
                            / len(filtered_product_ids)
                            * 100
                        ),
                        1,
                    )
                    if filtered_product_ids
                    else 0
                ),
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
                "name": "getSupplierByProduct",
                "description": "Get suppliers associated with specified product IDs, optionally filtered by product type",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of product identifiers to find suppliers for (e.g., ['PROD001', 'PROD002'])",
                        },
                        "product_type": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional list of product types to filter by (e.g., ['laptop', 'bluetooth speaker', 't-shirt']). Matches product names containing these terms.",
                        },
                    },
                    "required": ["product_ids"],
                },
            },
        }

class GetItemIdByProduct:
    @staticmethod
    def invoke(
        data: dict[str, Any],
        product_ids: list[str],
        product_type: list[str] = None,
        show_available: bool = None,
        exclude_no_stock: bool = True,
    ) -> str:
        """
        Get list of item IDs (variants) from specified product IDs, optionally filtered by product type and availability
        Excludes items with no stock (out_of_stock, discontinued) by default

        Data Sources: products.json (product_id, name, variants), suppliers.json (item_stock for stock validation)
        """
        if not product_ids:
            payload = {"error": "Product IDs list cannot be empty", "status": "failed"}
            out = json.dumps(payload)
            return out

        products = data.get("products", [])
        suppliers = data.get("suppliers", [])

        # Build stock information map from all suppliers
        stock_info_map = {}
        for supplier in suppliers:
            item_stock = supplier.get("item_stock", {})
            for item_id, stock_level in item_stock.items():
                # Track all suppliers that have this item and their stock levels
                if item_id not in stock_info_map:
                    stock_info_map[item_id] = []
                stock_info_map[item_id].append(
                    {
                        "supplier_id": supplier.get("supplier_id"),
                        "stock_level": stock_level,
                    }
                )

        # Convert product_type to lowercase for case-insensitive matching
        product_type_lower = []
        if product_type:
            product_type_lower = [ptype.lower() for ptype in product_type]

        matching_items = []
        product_item_map = {}
        total_variants_found = 0
        total_available_variants = 0
        total_unavailable_variants = 0
        total_excluded_no_stock = 0
        products_not_found = []

        for requested_product_id in product_ids:
            product_found = False

            for product in products:
                product_id = product.get("product_id")
                product_name = product.get("name", "").lower()
                variants = product.get("variants", {})

                if product_id == requested_product_id:
                    product_found = True

                    # Apply product type filter if specified
                    if product_type_lower:
                        # Check if product name contains any of the specified types
                        type_matches = any(
                            ptype in product_name for ptype in product_type_lower
                        )

                        if not type_matches:
                            # Product doesn't match type filter, skip it
                            continue

                    # Extract all item IDs (variant IDs) for this product with availability and stock filtering
                    product_items = []
                    for item_id, variant_info in variants.items():
                        is_available = variant_info.get("available", False)

                        # Check stock status across all suppliers
                        item_stock_info = stock_info_map.get(item_id, [])
                        has_stock = False
                        best_stock_level = "not_in_inventory"
                        supplier_count = 0

                        # Check if any supplier has this item with actual stock
                        for supplier_stock in item_stock_info:
                            stock_level = supplier_stock["stock_level"]
                            supplier_count += 1

                            # Consider item as having stock if any supplier has numeric stock > 0
                            if (
                                isinstance(stock_level, (int, str))
                                and str(stock_level).isdigit()
                                and int(stock_level) > 0
                            ):
                                has_stock = True
                                if best_stock_level == "not_in_inventory" or (
                                    isinstance(best_stock_level, (int, str))
                                    and int(stock_level) > int(best_stock_level)
                                ):
                                    best_stock_level = stock_level
                            elif not has_stock:
                                if best_stock_level == "not_in_inventory":
                                    best_stock_level = stock_level

                        # Apply stock exclusion filter if enabled
                        if exclude_no_stock and not has_stock:
                            # Item has no stock or is out_of_stock/discontinued across all suppliers
                            total_excluded_no_stock += 1
                            continue

                        # Apply availability filter if show_available is specified
                        if show_available is not None:
                            if show_available and not is_available:
                                # Want available items only, but this item is not available
                                total_unavailable_variants += 1
                                continue
                            elif not show_available and is_available:
                                # Want unavailable items only, but this item is available
                                total_available_variants += 1
                                continue

                        # Track totals for summary
                        if is_available:
                            total_available_variants += 1
                        else:
                            total_unavailable_variants += 1

                        # Determine stock status description
                        stock_status = "not_in_inventory"
                        total_stock_across_suppliers = 0

                        if has_stock:
                            stock_status = "in_stock"
                            # Calculate total stock across all suppliers
                            for supplier_stock in item_stock_info:
                                stock_level = supplier_stock["stock_level"]
                                if (
                                    isinstance(stock_level, (int, str))
                                    and str(stock_level).isdigit()
                                ):
                                    total_stock_across_suppliers += int(stock_level)
                        elif item_stock_info:
                            # Has stock entries but no actual stock
                            stock_statuses = [s["stock_level"] for s in item_stock_info]
                            if all(
                                status == "out_of_stock" for status in stock_statuses
                            ):
                                stock_status = "out_of_stock"
                            elif all(
                                status == "discontinued" for status in stock_statuses
                            ):
                                stock_status = "discontinued"
                            elif any(
                                status in ["out_of_stock", "discontinued"]
                                for status in stock_statuses
                            ):
                                stock_status = "mixed_no_stock"

                        item_detail = {
                            "item_id": item_id,
                            "price": variant_info.get("price", 0),
                            "available": is_available,
                            "options": variant_info.get("options", {}),
                            "stock_info": {
                                "stock_status": stock_status,
                                "total_stock_across_suppliers": total_stock_across_suppliers,
                                "suppliers_with_item": supplier_count,
                                "best_stock_level": best_stock_level,
                                "supplier_stock_details": item_stock_info,
                            },
                        }
                        product_items.append(item_detail)
                        total_variants_found += 1

                    if product_items:
                        product_info = {
                            "product_id": product_id,
                            "product_name": product.get("name"),
                            "total_variants": len(product_items),
                            "available_variants": len(
                                [item for item in product_items if item["available"]]
                            ),
                            "unavailable_variants": len(
                                [
                                    item
                                    for item in product_items
                                    if not item["available"]
                                ]
                            ),
                            "in_stock_variants": len(
                                [
                                    item
                                    for item in product_items
                                    if item["stock_info"]["stock_status"] == "in_stock"
                                ]
                            ),
                            "out_of_stock_variants": len(
                                [
                                    item
                                    for item in product_items
                                    if item["stock_info"]["stock_status"]
                                    in [
                                        "out_of_stock",
                                        "discontinued",
                                        "mixed_no_stock",
                                    ]
                                ]
                            ),
                            "item_ids": product_items,
                        }
                        matching_items.append(product_info)
                        product_item_map[product_id] = [
                            item["item_id"] for item in product_items
                        ]

                    break

            if not product_found:
                products_not_found.append(requested_product_id)

        # Create a flat list of all item IDs for easy access
        all_item_ids = []
        for product_info in matching_items:
            all_item_ids.extend([item["item_id"] for item in product_info["item_ids"]])

        # Determine filter description for response
        availability_filter_description = "all items"
        if show_available is True:
            availability_filter_description = "available items only"
        elif show_available is False:
            availability_filter_description = "unavailable items only"

        stock_filter_description = (
            "items with stock only"
            if exclude_no_stock
            else "all items regardless of stock"
        )

        result = {
            "status": "success",
            "search_criteria": {
                "requested_product_ids": product_ids,
                "product_type_filter": product_type,
                "show_available": show_available,
                "exclude_no_stock": exclude_no_stock,
                "filter_applied": product_type is not None
                or show_available is not None
                or exclude_no_stock,
                "availability_filter": availability_filter_description,
                "stock_filter": stock_filter_description,
            },
            "summary": {
                "products_found": len(matching_items),
                "products_not_found": len(products_not_found),
                "total_variants_found": total_variants_found,
                "total_available_variants": total_available_variants,
                "total_unavailable_variants": total_unavailable_variants,
                "total_excluded_no_stock": total_excluded_no_stock,
                "availability_breakdown": {
                    "available_percentage": (
                        round(
                            (
                                total_available_variants
                                / (
                                    total_available_variants
                                    + total_unavailable_variants
                                )
                                * 100
                            ),
                            1,
                        )
                        if (total_available_variants + total_unavailable_variants) > 0
                        else 0
                    ),
                    "unavailable_percentage": (
                        round(
                            (
                                total_unavailable_variants
                                / (
                                    total_available_variants
                                    + total_unavailable_variants
                                )
                                * 100
                            ),
                            1,
                        )
                        if (total_available_variants + total_unavailable_variants) > 0
                        else 0
                    ),
                },
                "stock_filtering": {
                    "items_excluded_no_stock": total_excluded_no_stock,
                    "items_with_stock": len(
                        [
                            item
                            for product in matching_items
                            for item in product["item_ids"]
                            if item["stock_info"]["stock_status"] == "in_stock"
                        ]
                    ),
                    "exclusion_rate_percent": (
                        round(
                            (
                                total_excluded_no_stock
                                / (total_variants_found + total_excluded_no_stock)
                                * 100
                            ),
                            1,
                        )
                        if (total_variants_found + total_excluded_no_stock) > 0
                        else 0
                    ),
                },
            },
            "item_ids": {
                "all_item_ids": all_item_ids,
                "products_with_items": matching_items,
            },
            "product_item_mapping": product_item_map,
            "products_not_found": products_not_found,
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetItemIdsByProduct",
                "description": "Get list of item IDs (variants) from specified product IDs, optionally filtered by product type and availability status. Excludes items with no stock (out_of_stock, discontinued) by default.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of product identifiers to get item IDs from (e.g., ['PROD001', 'PROD002'])",
                        },
                        "product_type": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional list of product types to filter by (e.g., ['laptop', 'bluetooth speaker', 't-shirt']). Matches product names containing these terms.",
                        },
                        "show_available": {
                            "type": "boolean",
                            "description": "Optional availability filter: true = only available items, false = only unavailable/out-of-stock items, null/undefined = all items regardless of availability",
                        },
                        "exclude_no_stock": {
                            "type": "boolean",
                            "description": "Optional stock filter: true = exclude items with no stock (out_of_stock, discontinued), false = include all items regardless of stock status",
                            "default": True,
                        },
                    },
                    "required": ["product_ids"],
                },
            },
        }


class GetProductItemsPerSupplier:
    @staticmethod
    def invoke(
        data: dict[str, Any],
        supplier_id: str = None,
        stock_available: bool = None,
        product_type=None,
    ) -> str:
        """
        Get products and items for a specific supplier with optional stock filtering and product type filtering
        Maps each item to its corresponding product

        Data Sources: suppliers.json (supplier_id, products, item_stock), products.json (product details, variants)
        """
        if not supplier_id:
            payload = {"error": "supplier_id is required", "status": "failed"}
            out = json.dumps(payload)
            return out
            
        # Find the specified supplier
        suppliers = data.get("suppliers", [])
        target_supplier = None

        for supplier in suppliers:
            if supplier.get("supplier_id") == supplier_id:
                target_supplier = supplier
                break

        if not target_supplier:
            payload = {"error": f"Supplier {supplier_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Get product information for mapping items to products
        products = data.get("products", [])
        product_details_map = {}
        item_to_product_map = {}

        # Handle product_type parameter - convert string to list if needed
        product_type_list = []
        if product_type is not None:
            if isinstance(product_type, str):
                product_type_list = [product_type]
            elif isinstance(product_type, list):
                product_type_list = product_type
            else:
                payload = {
                    "error": "product_type must be a string or list of strings",
                    "status": "failed",
                }
                out = json.dumps(payload)
                return out

        # Convert product_type to lowercase for case-insensitive matching
        product_type_lower = []
        if product_type_list:
            product_type_lower = [ptype.lower() for ptype in product_type_list]

        for product in products:
            product_id = product.get("product_id")
            product_name = product.get("name", "").lower()

            if product_id:
                # Apply product type filter if specified
                if product_type_lower:
                    type_matches = any(
                        ptype in product_name for ptype in product_type_lower
                    )
                    if not type_matches:
                        continue  # Skip this product if it doesn't match the type filter

                product_details_map[product_id] = {
                    "product_id": product_id,
                    "name": product.get("name"),
                    "category": product.get("category"),
                    "variants": product.get("variants", {}),
                }

                # Map each item to its product
                variants = product.get("variants", {})
                for item_id in variants.keys():
                    item_to_product_map[item_id] = product_id

        # Get supplier information
        supplier_item_stock = target_supplier.get("item_stock", {})

        # Process items based on stock_available filter and product type filter
        filtered_items = {}
        stock_summary = {
            "total_items": len(supplier_item_stock),
            "available_items": 0,
            "out_of_stock_items": 0,
            "discontinued_items": 0,
            "unmapped_items": 0,
            "filtered_out_items": 0,
        }

        for item_id, stock_level in supplier_item_stock.items():
            # Apply stock filter
            include_item = True

            if stock_available is True:
                # Only include items with numeric stock levels
                include_item = (
                    isinstance(stock_level, (int, str))
                    and str(stock_level).isdigit()
                    and int(stock_level) > 0
                )
            elif stock_available is False:
                # Only include out_of_stock or discontinued items
                include_item = stock_level in ["out_of_stock", "discontinued"]
            # If stock_available is None, include all items

            # Update stock summary
            if stock_level == "out_of_stock":
                stock_summary["out_of_stock_items"] += 1
            elif stock_level == "discontinued":
                stock_summary["discontinued_items"] += 1
            elif isinstance(stock_level, (int, str)) and str(stock_level).isdigit():
                stock_summary["available_items"] += 1

            if include_item:
                # Find which product this item belongs to
                product_id = item_to_product_map.get(item_id)

                if product_id:
                    # Check if product passes the type filter (it should already be in product_details_map if it passes)
                    if product_id in product_details_map:
                        if product_id not in filtered_items:
                            filtered_items[product_id] = []

                        # Get item details from product variants
                        product_info = product_details_map.get(product_id, {})
                        variants = product_info.get("variants", {})
                        item_variant_info = variants.get(item_id, {})

                        filtered_items[product_id].append(
                            {
                                "item_id": item_id,
                                "stock_level": stock_level,
                                "numeric_stock_level": (
                                    int(stock_level)
                                    if isinstance(stock_level, (int, str))
                                    and str(stock_level).isdigit()
                                    else 0
                                ),
                                "stock_status": (
                                    "available"
                                    if isinstance(stock_level, (int, str))
                                    and str(stock_level).isdigit()
                                    and int(stock_level) > 0
                                    else stock_level
                                ),
                                "variant_info": {
                                    "price": item_variant_info.get("price", 0),
                                    "available": item_variant_info.get(
                                        "available", False
                                    ),
                                    "options": item_variant_info.get("options", {}),
                                },
                            }
                        )
                    else:
                        # Item belongs to a product that was filtered out by product type
                        stock_summary["filtered_out_items"] += 1
                else:
                    # Item not mapped to any product
                    stock_summary["unmapped_items"] += 1
                    if "unmapped_items" not in filtered_items:
                        filtered_items["unmapped_items"] = []

                    filtered_items["unmapped_items"].append(
                        {
                            "item_id": item_id,
                            "stock_level": stock_level,
                            "numeric_stock_level": (
                                int(stock_level)
                                if isinstance(stock_level, (int, str))
                                and str(stock_level).isdigit()
                                else 0
                            ),
                            "stock_status": (
                                "available"
                                if isinstance(stock_level, (int, str))
                                and str(stock_level).isdigit()
                                and int(stock_level) > 0
                                else stock_level
                            ),
                            "variant_info": {
                                "price": 0,
                                "available": False,
                                "options": {},
                            },
                        }
                    )

        # Build detailed product information (only for products that match the type filter)
        products_with_items = []

        # Instead of iterating through supplier_products, iterate through filtered_items
        for product_id, product_items in filtered_items.items():
            # Skip unmapped_items key
            if product_id == "unmapped_items":
                continue

            # Only process products that are in our filtered product_details_map
            if product_id in product_details_map:
                product_info = product_details_map.get(product_id)

                # Only include products that have items after filtering
                if product_items:
                    # Calculate product-level stock summary
                    product_stock_summary = {
                        "total_items": len(product_items),
                        "available_items": len(
                            [
                                item
                                for item in product_items
                                if item["stock_status"] == "available"
                            ]
                        ),
                        "out_of_stock_items": len(
                            [
                                item
                                for item in product_items
                                if item["stock_status"] == "out_of_stock"
                            ]
                        ),
                        "discontinued_items": len(
                            [
                                item
                                for item in product_items
                                if item["stock_status"] == "discontinued"
                            ]
                        ),
                        "total_stock": sum(
                            item["numeric_stock_level"] for item in product_items
                        ),
                    }

                    products_with_items.append(
                        {
                            "product_id": product_id,
                            "product_name": product_info["name"],
                            "product_category": product_info["category"],
                            "stock_summary": product_stock_summary,
                            "items": product_items,
                        }
                    )

        result = {"status": "success", "products_with_items": products_with_items}
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductItemsPerSupplier",
                "description": "Get products and items for a specific supplier with optional stock filtering and product type filtering. Maps each item to its corresponding product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier identifier (e.g., '#SUP0001')",
                        },
                        "stock_available": {
                            "type": "boolean",
                            "description": "Optional stock filter: true = only items with stock, false = only out_of_stock/discontinued items, null/undefined = all items",
                        },
                        "product_type": {
                            "oneOf": [
                                {"type": "string"},
                                {"type": "array", "items": {"type": "string"}},
                            ],
                            "description": "Optional product type(s) to filter by. Can be a single string (e.g., 'headphones') or list of strings (e.g., ['smartphone', 'laptop']). Matches product names containing these terms.",
                        },
                    },
                    "required": ["supplier_id"],
                },
            },
        }


class UpdateSupplierProduct(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        supplier_id: str = None,
        product_id: str = None,
        item_ids: list[str] = None,
        stock_levels: list[int] = None,
    ) -> str:
        """
        Update supplier with new products and item IDs along with their stock levels
        Adds product to supplier's product list and updates item stock levels

        Writes to: suppliers.json (updates products list and item_stock)
        Data Sources: suppliers.json (supplier_id, products, item_stock), products.json (product validation)
        """
        if not supplier_id or not product_id or not item_ids or not stock_levels:
            payload = {"error": "supplier_id, product_id, item_ids, and stock_levels are required", "status": "failed"}
            out = json.dumps(payload)
            return out
            
        if not item_ids:
            payload = {"error": "Item IDs list cannot be empty", "status": "failed"}
            out = json.dumps(payload)
            return out

        if not stock_levels:
            payload = {"error": "Stock levels list cannot be empty", "status": "failed"}
            out = json.dumps(payload)
            return out

        if len(item_ids) != len(stock_levels):
            payload = {
                "error": f"Number of item IDs ({len(item_ids)}) must match number of stock levels ({len(stock_levels)})",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Validate all stock levels are non-negative
        for i, level in enumerate(stock_levels):
            if not isinstance(level, int) or level < 0:
                payload = {
                    "error": f"Stock level at index {i} must be a non-negative integer: {level}",
                    "status": "failed",
                }
                out = json.dumps(payload)
                return out

        # Validate product exists in products.json
        products = data.get("products", [])
        target_product = None

        for product in products:
            if product.get("product_id") == product_id:
                target_product = product
                break

        if not target_product:
            payload = {
                "error": f"Product {product_id} not found in product catalog",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Validate all item IDs exist in the product's variants
        product_variants = target_product.get("variants", {})
        invalid_items = []
        valid_items = []

        for item_id in item_ids:
            if item_id in product_variants:
                valid_items.append(item_id)
            else:
                invalid_items.append(item_id)

        if invalid_items:
            payload = {
                "error": f"Item IDs not found in product {product_id} variants: {', '.join(invalid_items)}",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Find the supplier
        suppliers = data.get("suppliers", [])
        supplier_to_update = None
        supplier_index = None

        for i, supplier in enumerate(suppliers):
            if supplier.get("supplier_id") == supplier_id:
                supplier_to_update = supplier
                supplier_index = i
                break

        if not supplier_to_update:
            payload = {"error": f"Supplier {supplier_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        # WRITE OPERATION: Update supplier products and item stock
        supplier_products = supplier_to_update.get("products", [])
        item_stock = supplier_to_update.get("item_stock", {})

        # Add product to supplier's product list if not already present
        product_added = False
        if product_id not in supplier_products:
            supplier_products.append(product_id)
            supplier_to_update["products"] = supplier_products
            product_added = True

        # Update item stock levels for all provided items
        stock_updates = []
        items_added = 0
        items_updated = 0

        for i, item_id in enumerate(item_ids):
            stock_level = stock_levels[i]
            old_stock = item_stock.get(item_id, "not_in_inventory")

            # Set new stock level
            item_stock[item_id] = stock_level

            if old_stock == "not_in_inventory":
                items_added += 1
                status = "added"
            else:
                items_updated += 1
                status = "updated"

            # Get variant details for additional info
            variant_info = product_variants.get(item_id, {})

            stock_updates.append(
                {
                    "item_id": item_id,
                    "status": status,
                    "previous_stock": old_stock,
                    "new_stock": stock_level,
                    "variant_info": {
                        "price": variant_info.get("price", 0),
                        "available": variant_info.get("available", False),
                        "options": variant_info.get("options", {}),
                    },
                }
            )

        supplier_to_update["item_stock"] = item_stock
        supplier_to_update["product_updated"] = datetime.now().isoformat()
        supplier_to_update["last_updated"] = datetime.now().isoformat()

        # Update the supplier in the data structure
        data["suppliers"][supplier_index] = supplier_to_update

        # Calculate summary metrics
        total_stock_added = sum(stock_levels)

        result = {
            "status": "success",
            "supplier_id": supplier_id,
            "supplier_name": supplier_to_update.get("name"),
            "product_updates": {
                "product_id": product_id,
                "product_name": target_product.get("name"),
                "product_added_to_supplier": product_added,
                "total_products_in_portfolio": len(supplier_products),
            },
            "item_updates": {
                "total_items_processed": len(item_ids),
                "items_added": items_added,
                "items_updated": items_updated,
                "total_stock_units_added": total_stock_added,
                "stock_details": stock_updates,
            },
            "supplier_summary": {
                "total_products": len(supplier_products),
                "total_items_in_stock": len(item_stock),
                "total_stock_value": sum(
                    level for level in item_stock.values() if isinstance(level, int)
                ),
            },
            "last_updated": supplier_to_update["last_updated"],
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateSupplierProduct",
                "description": "Update supplier with new products and item IDs along with their stock levels. Adds product to supplier's portfolio and sets stock levels for specified items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier identifier (e.g., '#SUP0001')",
                        },
                        "product_id": {
                            "type": "string",
                            "description": "Product identifier to add to supplier's portfolio",
                        },
                        "item_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of item identifiers (product variants) to add to supplier's inventory",
                        },
                        "stock_levels": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "List of stock levels corresponding to each item in item_ids (same order, must be non-negative integers)",
                        },
                    },
                    "required": [
                        "supplier_id",
                        "product_id",
                        "item_ids",
                        "stock_levels",
                    ],
                },
            },
        }


class GetCourierByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], courier_name: str = None) -> str:
        """
        Get courier details based on courier name (case-insensitive search)

        Data Sources: couriers.json (courier_id, name, coverage_area, contact_info, tracking_ids)
        """
        if not courier_name or not courier_name.strip():
            payload = {"error": "Courier name is required", "status": "failed"}
            out = json.dumps(payload)
            return out

        courier_name = courier_name.strip()

        # Find courier by name (case-insensitive search)
        couriers = data.get("couriers", [])
        matching_couriers = []

        for courier in couriers:
            stored_name = courier.get("name", "")

            # Exact match (case-insensitive)
            if stored_name.lower() == courier_name.lower():
                matching_couriers.insert(0, courier)  # Put exact matches first
            # Partial match (case-insensitive)
            elif courier_name.lower() in stored_name.lower():
                matching_couriers.append(courier)

        if not matching_couriers:
            payload = {
                "error": f"No courier found with name containing '{courier_name}'",
                "status": "not_found",
                "search_term": courier_name,
            }
            out = json.dumps(payload)
            return out

        # Return the first (best) match with detailed information
        best_match = matching_couriers[0]

        # Calculate courier metrics
        tracking_ids = best_match.get("tracking_ids", [])
        coverage_area = best_match.get("coverage_area", [])

        # Determine service capabilities based on coverage
        service_capabilities = {
            "domestic_delivery": "USA" in coverage_area,
            "international_delivery": len(
                [country for country in coverage_area if country != "USA"]
            )
            > 0,
            "total_coverage_countries": len(coverage_area),
            "available_tracking_ids": len(tracking_ids),
        }

        result = {
            "status": "success",
            "search_term": courier_name,
            "exact_match": best_match.get("name", "").lower() == courier_name.lower(),
            "courier_details": {
                "courier_id": best_match.get("courier_id"),
                "name": best_match.get("name"),
                "contact_info": best_match.get("contact_info", {}),
                "coverage_area": coverage_area,
                "service_types": best_match.get("service_types", ["standard"]),
                "base_cost": best_match.get("base_cost", 0),
                "rating": best_match.get("rating", 0),
                "specialties": best_match.get("specialties", []),
            },
            "service_capabilities": service_capabilities,
        }
        payload = result
        out = json.dumps(payload)
        return out
        
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCourierByName",
                "description": "Get courier details based on courier name with case-insensitive search. Returns exact matches first, then partial matches.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "courier_name": {
                            "type": "string",
                            "description": "Courier name to search for (case-insensitive, supports partial matching)",
                        }
                    },
                    "required": ["courier_name"],
                },
            },
        }


class FilterByProductIdPerProductName(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], product_names: list[str] = None, product_ids: list[str] = None
    ) -> str:
        """
        Filter and get product IDs based on product names (case-insensitive search)
        Returns product IDs in the same order as input product names
        Optionally filters results to only include products from a specified list of product IDs

        Data Sources: products.json (product_id, name)
        """
        if not product_names:
            payload = {"error": "Product names list cannot be empty", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Clean and validate input
        cleaned_product_names = []
        for name in product_names:
            if not name or not str(name).strip():
                cleaned_product_names.append("")
            else:
                cleaned_product_names.append(str(name).strip())

        # Convert product_ids filter to set for faster lookup
        product_ids_filter = None
        if product_ids:
            product_ids_filter = set(product_ids)

        products = data.get("products", [])
        result_mapping = []
        total_matches = 0
        total_not_found = 0
        total_filtered_out = 0

        # Process each product name in order
        for i, search_name in enumerate(cleaned_product_names):
            if not search_name:
                result_mapping.append(
                    {
                        "index": i,
                        "search_name": search_name,
                        "product_id": None,
                        "product_name": None,
                        "match_type": "empty_input",
                        "status": "failed",
                    }
                )
                total_not_found += 1
                continue

            # Find matching product (case-insensitive)
            matching_product = None
            match_type = "not_found"

            for product in products:
                stored_name = product.get("name", "")
                product_id = product.get("product_id")

                # Apply product_ids filter if specified
                if product_ids_filter and product_id not in product_ids_filter:
                    continue  # Skip products not in the filter list

                # Exact match (case-insensitive)
                if stored_name.lower() == search_name.lower():
                    matching_product = product
                    match_type = "exact_match"
                    break
                # Partial match (case-insensitive) - only if no exact match found
                elif (
                    search_name.lower() in stored_name.lower() and not matching_product
                ):
                    matching_product = product
                    match_type = "partial_match"

            if matching_product:
                result_mapping.append(
                    {
                        "index": i,
                        "search_name": search_name,
                        "product_id": matching_product.get("product_id"),
                        "product_name": matching_product.get("name"),
                        "match_type": match_type,
                        "status": "success",
                    }
                )
                total_matches += 1
            else:
                # Check if there would have been a match without the product_ids filter
                if product_ids_filter:
                    found_without_filter = False
                    for product in products:
                        stored_name = product.get("name", "")
                        if (
                            stored_name.lower() == search_name.lower()
                            or search_name.lower() in stored_name.lower()
                        ):
                            found_without_filter = True
                            break

                    if found_without_filter:
                        result_mapping.append(
                            {
                                "index": i,
                                "search_name": search_name,
                                "product_id": None,
                                "product_name": None,
                                "match_type": "filtered_out",
                                "status": "failed",
                            }
                        )
                        total_filtered_out += 1
                    else:
                        result_mapping.append(
                            {
                                "index": i,
                                "search_name": search_name,
                                "product_id": None,
                                "product_name": None,
                                "match_type": "not_found",
                                "status": "failed",
                            }
                        )
                        total_not_found += 1
                else:
                    result_mapping.append(
                        {
                            "index": i,
                            "search_name": search_name,
                            "product_id": None,
                            "product_name": None,
                            "match_type": "not_found",
                            "status": "failed",
                        }
                    )
                    total_not_found += 1

        # Create simple arrays for easy access
        product_ids_array = [mapping.get("product_id") for mapping in result_mapping]
        successful_matches = [
            mapping for mapping in result_mapping if mapping["status"] == "success"
        ]
        failed_matches = [
            mapping for mapping in result_mapping if mapping["status"] == "failed"
        ]
        filtered_out_matches = [
            mapping
            for mapping in failed_matches
            if mapping.get("match_type") == "filtered_out"
        ]

        result = {
            "status": "success",
            "search_criteria": {
                "product_names": product_names,
                "product_ids_filter": product_ids,
                "filter_applied": product_ids_filter is not None,
            },
            "search_summary": {
                "total_searches": len(cleaned_product_names),
                "successful_matches": total_matches,
                "failed_matches": total_not_found,
                "filtered_out_matches": total_filtered_out,
                "match_rate_percent": (
                    round((total_matches / len(cleaned_product_names) * 100), 1)
                    if cleaned_product_names
                    else 0
                ),
                "filter_effectiveness": (
                    {
                        "would_match_without_filter": total_matches
                        + total_filtered_out,
                        "matches_after_filter": total_matches,
                        "reduction_percent": (
                            round(
                                (
                                    total_filtered_out
                                    / (total_matches + total_filtered_out)
                                    * 100
                                ),
                                1,
                            )
                            if (total_matches + total_filtered_out) > 0
                            else 0
                        ),
                    }
                    if product_ids_filter
                    else None
                ),
            },
            "product_ids": product_ids_array,
            "detailed_mapping": result_mapping,
            "successful_matches": successful_matches,
            "failed_matches": failed_matches,
            "filtered_out_matches": filtered_out_matches,
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FilterByProductIdPerProductName",
                "description": "Filter and get product IDs based on product names with case-insensitive search. Returns product IDs in the same order as input product names, with null values for unmatched names. Optionally filters results to only include products from a specified list of product IDs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_names": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of product names to search for (case-insensitive, supports partial matching). Returns corresponding product IDs at the same index positions.",
                        },
                        "product_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional list of product IDs to filter results. Only products with IDs in this list will be considered for matching. If not provided, all products are considered.",
                        },
                    },
                    "required": ["product_names"],
                },
            },
        }


class AddToOrder(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str = None,
        item_id: str = None,
        payment_method: str = None,
        quantity: int = 1,
        tax_amount: float = None,
        shipping_cost: float = None,
    ) -> str:
        """
        Add an item to an existing order (only for pending orders) with payment processing

        Writes to: orders.json (updates existing order items)
        Data Sources: orders.json (order validation), products.json (item validation), users.json (payment validation)
        """
        if not order_id or not order_id.strip():
            payload = {"error": "Order ID is required", "status": "failed"}
            out = json.dumps(payload)
            return out

        if not item_id or not item_id.strip():
            payload = {"error": "Item ID is required", "status": "failed"}
            out = json.dumps(payload)
            return out

        if not payment_method or not payment_method.strip():
            payload = {"error": "Payment method is required", "status": "failed"}
            out = json.dumps(payload)
            return out

        if quantity <= 0:
            payload = {"error": "Quantity must be greater than 0", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Validate optional amounts
        if tax_amount is not None and tax_amount < 0:
            payload = {"error": "Tax amount cannot be negative", "status": "failed"}
            out = json.dumps(payload)
            return out

        if shipping_cost is not None and shipping_cost < 0:
            payload = {"error": "Shipping cost cannot be negative", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Add # prefix if not provided (for convenience)
        formatted_order_id = order_id if order_id.startswith("#") else f"#{order_id}"

        # Find the order to update
        orders = data.get("orders", [])
        order_to_update = None
        order_index = None

        for i, order in enumerate(orders):
            if order.get("order_id") == formatted_order_id:
                order_to_update = order
                order_index = i
                break

        if not order_to_update:
            payload = {"error": f"Order {formatted_order_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Rule: Can only add items to pending orders
        current_status = order_to_update.get("status")
        if current_status != "pending":
            payload = {
                "error": f"Cannot add items to order with status '{current_status}'. Items can only be added to pending orders.",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Get user ID from order for payment validation
        user_id = order_to_update.get("user_id")
        if not user_id:
            payload = {"error": "Order does not have associated user ID", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Rule: Validate user identity exists before processing any user requests
        users = data.get("users", [])
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            payload = {"error": f"User {user_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Validate payment method
        payment_methods = user.get("payment_methods", {})
        selected_payment = None

        for method_id in payment_methods:
            if payment_method in method_id:
                selected_payment = payment_methods[method_id]
                break

        if not selected_payment:
            payload = {
                "error": f"Payment method {payment_method} not found for user",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        payment_source = selected_payment.get("source")
        if payment_source not in ["credit_card", "paypal", "gift_card"]:
            payload = {
                "error": f"Invalid payment method type: {payment_source}",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Rule: Confirm item_id exists in product variants before including in orders
        products = data.get("products", [])
        variant_found = None
        product_found = None

        for product in products:
            variants = product.get("variants", {})
            if item_id in variants:
                variant_found = variants[item_id]
                product_found = product
                break

        if not variant_found:
            payload = {
                "error": f"Item {item_id} not found in product catalog",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Rule: Check product availability status before allocation - never allocate unavailable items
        if not variant_found.get("available", False):
            payload = {
                "error": f"Item {item_id} ({product_found.get('name')}) is not available",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Get item details
        unit_price = variant_found.get("price", 0)
        line_total = unit_price * quantity

        # Capture current order state before modification
        current_order_items = order_to_update.get("items", []).copy()
        current_subtotal = sum(
            item.get("price", 0) * item.get("quantity", 1)
            for item in current_order_items
        )
        current_payment_history = order_to_update.get("payment_history", []).copy()
        current_total_paid = sum(
            payment.get("amount", 0)
            for payment in current_payment_history
            if payment.get("transaction_type") == "payment"
        )

        # WRITE OPERATION: Add item to order
        order_items = order_to_update.get("items", [])

        # Check if item already exists in the order
        item_exists = False
        added_quantity = quantity
        for existing_item in order_items:
            if existing_item.get("item_id") == item_id:
                # Update quantity of existing item
                old_quantity = existing_item.get("quantity", 1)
                new_quantity = old_quantity + quantity
                existing_item["quantity"] = new_quantity
                existing_item["price"] = unit_price  # Update price in case it changed
                item_exists = True

                result_message = f"Updated quantity of existing item from {old_quantity} to {new_quantity}"
                break

        if not item_exists:
            # Add new item to order
            new_item = {
                "name": product_found.get("name"),
                "product_id": product_found.get("product_id"),
                "item_id": item_id,
                "price": unit_price,
                "options": variant_found.get("options", {}),
                "quantity": quantity,
            }
            order_items.append(new_item)
            result_message = "Added new item to order"

        order_to_update["items"] = order_items

        # Calculate new order totals
        new_subtotal = sum(
            item.get("price", 0) * item.get("quantity", 1) for item in order_items
        )

        # Calculate additional costs
        additional_tax = tax_amount if tax_amount is not None else 0
        additional_shipping = shipping_cost if shipping_cost is not None else 0

        # Calculate total additional amount (item cost + additional fees)
        total_additional_amount = line_total + additional_tax + additional_shipping
        new_order_total = new_subtotal + additional_tax + additional_shipping

        # Rule: High-value orders (>$1000 total) require payment verification before fulfillment
        requires_verification = new_order_total > 1000.0

        # Rule: Gift card payments cannot exceed available balance - verify balance sufficiency before processing
        if payment_source == "gift_card":
            available_balance = selected_payment.get("balance", 0)
            if total_additional_amount > available_balance:
                payload = {
                    "error": f"Insufficient gift card balance. Available: ${available_balance}, Required: ${total_additional_amount}",
                    "status": "failed",
                }
                out = json.dumps(payload)
                return out

        # Process payment for the additional amount
        payment_result = {
            "payment_method_id": payment_method,
            "payment_source": payment_source,
            "amount": total_additional_amount,
            "verification_required": requires_verification,
            "transaction_id": f"TXN_{user_id}_{payment_method}_{int(total_additional_amount)}",
        }

        # Add specific details based on payment type
        if payment_source == "gift_card":
            new_balance = selected_payment.get("balance", 0) - total_additional_amount
            payment_result["remaining_gift_card_balance"] = new_balance
        elif payment_source == "credit_card":
            payment_result["card_brand"] = selected_payment.get("brand")
            payment_result["card_last_four"] = selected_payment.get("last_four")

        # Add payment transaction to order history
        payment_transaction = {
            "transaction_type": "payment",
            "amount": total_additional_amount,
            "payment_method_id": payment_method,
            "payment_source": payment_source,
            "processed_date": datetime.now().isoformat(),
            "reason": "item_addition",
        }

        if "payment_history" not in order_to_update:
            order_to_update["payment_history"] = []
        order_to_update["payment_history"].append(payment_transaction)

        # Add order modification log
        if "modifications" not in order_to_update:
            order_to_update["modifications"] = []

        order_to_update["modifications"].append(
            {
                "type": "item_added",
                "item_id": item_id,
                "quantity": added_quantity,
                "unit_price": unit_price,
                "line_total": line_total,
                "additional_tax": additional_tax,
                "additional_shipping": additional_shipping,
                "total_additional_cost": total_additional_amount,
                "payment_method": payment_method,
                "timestamp": datetime.now().isoformat(),
                "action": result_message,
            }
        )

        order_to_update["last_updated"] = datetime.now().isoformat()

        # Update the order in the data structure
        data["orders"][order_index] = order_to_update

        # Calculate comprehensive metrics
        total_items_count = len(order_items)
        total_quantity = sum(item.get("quantity", 1) for item in order_items)
        new_total_paid = current_total_paid + total_additional_amount

        result = {
            "status": "success",
            "order_id": formatted_order_id,
            "user_id": user_id,
            "item_added": {
                "item_id": item_id,
                "product_name": product_found.get("name"),
                "product_id": product_found.get("product_id"),
                "quantity": added_quantity,
                "unit_price": unit_price,
                "line_total": line_total,
                "options": variant_found.get("options", {}),
            },
            "action_performed": result_message,
            "current_order_before_addition": {
                "items": current_order_items,
                "total_items": len(current_order_items),
                "total_quantity": sum(
                    item.get("quantity", 1) for item in current_order_items
                ),
                "subtotal": round(current_subtotal, 2),
                "total_paid": round(current_total_paid, 2),
            },
            "updated_order_after_addition": {
                "items": order_items,
                "total_items": total_items_count,
                "total_quantity": total_quantity,
                "new_subtotal": round(new_subtotal, 2),
                "additional_costs": {
                    "tax_amount": additional_tax,
                    "shipping_cost": additional_shipping,
                    "total_additional": round(total_additional_amount, 2),
                },
                "new_order_total": round(new_order_total, 2),
                "requires_verification": requires_verification,
                "new_total_paid": round(new_total_paid, 2),
            },
            "payment_processing": {
                "payment_method": payment_method,
                "payment_source": payment_source,
                "amount_charged": round(total_additional_amount, 2),
                "payment_breakdown": {
                    "item_cost": round(line_total, 2),
                    "tax_amount": additional_tax,
                    "shipping_cost": additional_shipping,
                },
                "payment_result": payment_result,
                "verification_required": requires_verification,
            },
            "order_changes": {
                "subtotal_increase": round(new_subtotal - current_subtotal, 2),
                "total_payment_increase": round(total_additional_amount, 2),
                "items_added": 1 if not item_exists else 0,
                "quantity_added": added_quantity,
            },
            "last_updated": order_to_update["last_updated"],
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddToOrder",
                "description": "Add an item to an existing pending order with payment processing. Shows both current and updated order details. Only works for pending orders.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Order identifier (e.g., 'W6893533' or '#W6893533')",
                        },
                        "item_id": {
                            "type": "string",
                            "description": "Product variant identifier to add to the order",
                        },
                        "payment_method": {
                            "type": "string",
                            "description": "Payment method identifier from customer's stored methods (required)",
                        },
                        "quantity": {
                            "type": "integer",
                            "description": "Quantity of the item to add (defaults to 1 if not specified)",
                            "default": 1,
                        },
                        "tax_amount": {
                            "type": "number",
                            "description": "Optional additional tax amount for the added item (defaults to 0)",
                        },
                        "shipping_cost": {
                            "type": "number",
                            "description": "Optional additional shipping cost for the added item (defaults to 0)",
                        },
                    },
                    "required": ["order_id", "item_id", "payment_method"],
                },
            },
        }


class GetOrderIdsByProductIds(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], product_ids: list[str] = None, user_id: str = None
    ) -> str:
        """
        Get list of order IDs that contain specified product IDs

        Data Sources: orders.json (order items)
        """
        if not product_ids:
            payload = {"error": "Product IDs list cannot be empty", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Rule: Validate user identity exists before processing any user requests (if user_id provided)
        if user_id:
            users = data.get("users", [])
            user = next((u for u in users if u.get("user_id") == user_id), None)
            if not user:
                payload = {"error": f"User {user_id} not found", "status": "failed"}
                out = json.dumps(payload)
                return out

        # Search through all orders to find matches
        orders = data.get("orders", [])
        matching_orders = []

        for order in orders:
            order_id = order.get("order_id")
            order_user_id = order.get("user_id")
            order_items = order.get("items", [])

            # Filter by user_id if specified
            if user_id and order_user_id != user_id:
                continue

            # Check which products this order contains
            for item in order_items:
                item_product_id = item.get("product_id")
                if item_product_id in product_ids:
                    matching_orders.append(
                        {
                            "order_id": order_id,
                            "user_id": order_user_id,
                            "order_status": order.get("status"),
                            "order_date": order.get("timestamp"),
                        }
                    )
                    break  # Found a match, no need to check other items in this order

        # Remove duplicates and get unique order IDs
        unique_order_ids = list({order["order_id"] for order in matching_orders})

        result = {
            "status": "success",
            "order_ids": unique_order_ids,
            "order_details": matching_orders,
            "total_orders_found": len(unique_order_ids),
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrderIdsByProductIds",
                "description": "Get list of order IDs that contain specified product IDs",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of product identifiers to find orders for",
                        },
                        "user_id": {
                            "type": "string",
                            "description": "Optional user identifier to filter orders by specific customer",
                        },
                    },
                    "required": ["product_ids"],
                },
            },
        }


class AssignTrackingNumber(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str = None,
        order_ids: list[str] = None,
        preferred_courier_id: str = None,
        courier_id: str = None,
        destination_country: str = None,
    ) -> str:
        """
        Assign tracking number for pending orders using a preferred courier
        Supports both single order and batch processing
        When order_ids is used, creates a single tracking ID for all orders

        Writes to: orders.json (updates order fulfillments with tracking info)
        Data Sources: orders.json (order status validation), couriers.json (courier availability)
        """
        #Validate input parameters
        if not order_id and not order_ids:
            payload = {
                    "error": "Either order_id or order_ids must be provided",
                    "status": "failed",
                }
            out = json.dumps(
                payload)
            return out

        if order_id and order_ids:
            payload = {
                    "error": "Cannot specify both order_id and order_ids. Use one or the other.",
                    "status": "failed",
                }
            out = json.dumps(
                payload)
            return out

        #Build list of orders to process
        orders_to_process = []
        batch_mode = False

        if order_id:
            orders_to_process.append(order_id.strip())
        if order_ids:
            orders_to_process.extend(
                [oid.strip() for oid in order_ids if oid and oid.strip()]
            )
            batch_mode = True

        if not orders_to_process:
            payload = {"error": "No valid order IDs provided", "status": "failed"}
            out = json.dumps(
                payload)
            return out

        #Handle both preferred_courier_id and courier_id parameters for backward compatibility
        selected_courier_preference = preferred_courier_id or courier_id

        #Find and validate all orders
        orders = data.get("orders", [])
        valid_orders = []
        invalid_orders = []

        for order_id_input in orders_to_process:
            #Add # prefix if not provided (for convenience)
            formatted_order_id = (
                order_id_input
                if order_id_input.startswith("#")
                else f"#{order_id_input}"
            )

            order_found = False
            for i, order in enumerate(orders):
                if order.get("order_id") == formatted_order_id:
                    current_status = order.get("status")

                    #Check if order is eligible for tracking assignment
                    if current_status != "pending":
                        invalid_orders.append(
                            {
                                "order_id": formatted_order_id,
                                "error": f"Cannot assign tracking to order with status '{current_status}'. Tracking can only be assigned to pending orders.",
                                "current_status": current_status,
                            }
                        )
                    else:
                        valid_orders.append(
                            {
                                "order_id": formatted_order_id,
                                "order_index": i,
                                "order_data": order,
                            }
                        )
                    order_found = True
                    break

            if not order_found:
                invalid_orders.append(
                    {"order_id": formatted_order_id, "error": "Order not found"}
                )

        if not valid_orders:
            payload = {
                    "error": "No valid orders found for tracking assignment",
                    "status": "failed",
                    "invalid_orders": invalid_orders,
                    "total_processed": len(orders_to_process),
                    "successful_assignments": 0,
                    "failed_assignments": len(invalid_orders),
                }
            out = json.dumps(
                payload)
            return out

        #Get destination country from first order if not provided
        if not destination_country:
            first_order = valid_orders[0]["order_data"]
            order_address = first_order.get("address", {})
            destination_country = order_address.get("country")

            if not destination_country:
                payload = {
                        "error": "Destination country not found in order address and not provided as parameter",
                        "status": "failed",
                    }
                out = json.dumps(
                    payload)
                return out

        #Rule: Assign couriers only if destination country matches their coverage areas
        couriers = data.get("couriers", [])
        eligible_couriers = []

        for courier in couriers:
            coverage_area = courier.get("coverage_area", [])
            if destination_country in coverage_area:
                eligible_couriers.append(courier)

        if not eligible_couriers:
            payload = {
                    "error": f"No couriers available for destination country: {destination_country}",
                    "status": "failed",
                }
            out = json.dumps(
                payload)
            return out

        #Select courier based on preference or use automatic selection
        selected_courier = None
        selection_method = "automatic"

        if selected_courier_preference:
            #Find the preferred courier if provided
            selected_courier = next(
                (
                    c
                    for c in eligible_couriers
                    if c.get("courier_id") == selected_courier_preference
                ),
                None,
            )

            if not selected_courier:
                #Preferred courier not available, provide alternatives
                available_courier_options = [
                    {
                        "courier_id": c.get("courier_id"),
                        "name": c.get("name"),
                        "rating": c.get("rating", 0),
                    }
                    for c in eligible_couriers
                ]
                payload = {
                        "error": f"Preferred courier {selected_courier_preference} not available for destination {destination_country}",
                        "status": "failed",
                        "available_alternatives": available_courier_options,
                    }
                out = json.dumps(
                    payload)
                return out
            selection_method = "preferred"
        else:
            #Use automatic selection logic - select highest rated courier
            eligible_couriers.sort(key=lambda x: x.get("rating", 0), reverse=True)
            selected_courier = eligible_couriers[0]

        #Generate tracking ID based on mode (single or batch)
        if batch_mode:
            #Create single tracking ID for all orders in batch
            batch_identifier = f"BATCH{len(valid_orders):02d}"
            courier_code = (
                selected_courier.get("courier_id", "")
                .replace("#", "")
                .replace("COU", "C")
            )
            assigned_tracking_id = f"TRK{batch_identifier}{courier_code}"
            tracking_generation_method = "single_batch_tracking"
        else:
            #Single order - generate tracking ID based on order_id + courier_id
            order_number = valid_orders[0]["order_id"].replace("#", "")
            courier_code = (
                selected_courier.get("courier_id", "")
                .replace("#", "")
                .replace("COU", "C")
            )
            assigned_tracking_id = f"TRK{order_number}{courier_code}"
            tracking_generation_method = "order_courier_based"

        #Process each valid order with the same tracking ID
        successful_assignments = []
        total_batch_value = 0.0

        for order_info in valid_orders:
            order_data = order_info["order_data"]
            order_index = order_info["order_index"]
            formatted_order_id = order_info["order_id"]

            #Calculate order value for insurance requirements
            order_items = order_data.get("items", [])
            order_value = sum(
                item.get("price", 0) * item.get("quantity", 1) for item in order_items
            )
            total_batch_value += order_value

            #Rule: High-value orders (>$1000 total) require payment verification before fulfillment
            requires_insurance = order_value > 1000.0

            #WRITE OPERATION: Add fulfillment information to order
            fulfillment_entry = {
                "tracking_id": assigned_tracking_id,
                "courier_id": selected_courier.get("courier_id"),
                "courier_name": selected_courier.get("name"),
                "courier_contact": selected_courier.get("contact_info", {}),
                "status": "processed",
                "assigned_date": datetime.now().isoformat(),
                "destination_country": destination_country,
                "requires_insurance": requires_insurance,
                "selection_method": selection_method,
                "batch_processing": batch_mode,
                "batch_size": len(valid_orders) if batch_mode else 1,
            }

            if "fulfillments" not in order_data:
                order_data["fulfillments"] = []
            order_data["fulfillments"].append(fulfillment_entry)

            #Update order status to processed
            previous_status = order_data.get("status")
            order_data["status"] = "processed"
            order_data["last_updated"] = datetime.now().isoformat()

            #Update the order in the data structure
            data["orders"][order_index] = order_data

            successful_assignments.append(
                {
                    "order_id": formatted_order_id,
                    "user_id": order_data.get("user_id"),
                    "tracking_id": assigned_tracking_id,
                    "courier_id": selected_courier.get("courier_id"),
                    "courier_name": selected_courier.get("name"),
                    "previous_status": previous_status,
                    "new_status": "processed",
                    "order_value": round(order_value, 2),
                    "requires_insurance": requires_insurance,
                    "assigned_date": fulfillment_entry["assigned_date"],
                }
            )

        #Check if batch requires insurance (total value > $1000)
        batch_requires_insurance = total_batch_value > 1000.0 if batch_mode else None

        #Prepare comprehensive response
        result = {
            "status": "success",
            "processing_summary": {
                "total_processed": len(orders_to_process),
                "successful_assignments": len(successful_assignments),
                "failed_assignments": len(invalid_orders),
            },
            "tracking_details": {
                "tracking_id": assigned_tracking_id,
                "shared_tracking": batch_mode,
                "tracking_generation_method": tracking_generation_method,
                "batch_requires_insurance": batch_requires_insurance,
            },
            "courier_details": {
                "courier_id": selected_courier.get("courier_id"),
                "name": selected_courier.get("name"),
                "rating": selected_courier.get("rating", 0),
                "service_types": selected_courier.get("service_types", ["standard"]),
                "specialties": selected_courier.get("specialties", []),
                "selection_method": selection_method,
            },
            "delivery_info": {
                "destination_country": destination_country,
                "tracking_generation_method": tracking_generation_method,
            },
            "successful_assignments": successful_assignments,
            "failed_assignments": invalid_orders,
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignTrackingNumber",
                "description": "Assign tracking number for pending orders using a preferred courier. Supports both single order and batch processing. When order_ids is used, creates a single shared tracking ID for all orders in the batch. Updates order status to 'processed' and adds fulfillment information.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Single order identifier (e.g., 'W6893533' or '#W6893533'). Cannot be used with order_ids. Creates individual tracking ID.",
                        },
                        "order_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Array of order identifiers for batch processing (e.g., ['W6893533', '#W6893534']). Cannot be used with order_id. Creates single shared tracking ID for all orders.",
                        },
                        "preferred_courier_id": {
                            "type": "string",
                            "description": "Optional preferred courier ID (e.g., 'COURIER001'). If not provided or unavailable, will auto-select the highest-rated available courier.",
                        },
                        "courier_id": {
                            "type": "string",
                            "description": "Optional courier ID (e.g., 'COURIER001'). Alternative parameter name for preferred_courier_id for backward compatibility.",
                        },
                        "destination_country": {
                            "type": "string",
                            "description": "Optional destination country for delivery. If not provided, will use country from first order's delivery address.",
                        },
                    },
                    "anyOf": [{"required": ["order_id"]}, {"required": ["order_ids"]}],
                },
            },
        }

class GetSupplierInventory:
    @staticmethod
    def invoke(
        data: dict[str, Any],
        supplier_id: str,
        product_types: list[str] = None,
        item_ids: list[str] = None,
        stock_available: bool = None,
        stock_level: int = None,
        stock_level_comparison: str = None,
    ) -> str:
        """
        Get supplier inventory filtered by product types, item IDs, stock availability, and stock level with comparison options
        """
        # Find supplier
        suppliers = data.get("suppliers", [])
        target_supplier = next(
            (s for s in suppliers if s.get("supplier_id") == supplier_id), None
        )

        if not target_supplier:
            payload = {"error": f"Supplier {supplier_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Validate stock_level parameter
        if stock_level is not None and stock_level < 0:
            payload = {"error": "Stock level filter must be non-negative", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Validate stock_level_comparison parameter
        valid_comparisons = ["above", "below", "equal"]
        if stock_level_comparison and stock_level_comparison not in valid_comparisons:
            payload = {
                "error": f"Invalid stock_level_comparison '{stock_level_comparison}'. Valid options: {', '.join(valid_comparisons)}",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # If stock_level_comparison is provided, stock_level must also be provided
        if stock_level_comparison and stock_level is None:
            payload = {
                "error": "stock_level must be provided when using stock_level_comparison",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Get product mapping
        products = data.get("products", [])
        item_to_product_map = {}
        product_details_map = {}

        for product in products:
            product_id = product.get("product_id")
            product_name = product.get("name", "").lower()
            variants = product.get("variants", {})

            if product_id:
                product_details_map[product_id] = {
                    "product_id": product_id,
                    "product_name": product.get("name"),
                    "product_category": product.get("category", ""),
                }

                for item_id in variants.keys():
                    item_to_product_map[item_id] = product_id

        # Filter supplier inventory
        supplier_item_stock = target_supplier.get("item_stock", {})
        matching_items = []

        for item_id, stock_level_value in supplier_item_stock.items():
            # Apply stock_available filter if specified
            if stock_available is not None:
                if stock_available:
                    # Only include items with numeric stock > 0
                    if not (
                        isinstance(stock_level_value, (int, str))
                        and str(stock_level_value).isdigit()
                        and int(stock_level_value) > 0
                    ):
                        continue
                else:
                    # Only include out_of_stock or discontinued items
                    if stock_level_value not in ["out_of_stock", "discontinued"]:
                        continue

            # Apply stock_level filter with comparison if specified
            if stock_level is not None:
                # Only check numeric stock levels against the threshold
                if (
                    isinstance(stock_level_value, (int, str))
                    and str(stock_level_value).isdigit()
                ):
                    numeric_stock = int(stock_level_value)

                    if stock_level_comparison:
                        if (
                            stock_level_comparison == "above"
                            and numeric_stock <= stock_level
                        ):
                            continue
                        elif (
                            stock_level_comparison == "below"
                            and numeric_stock >= stock_level
                        ):
                            continue
                        elif (
                            stock_level_comparison == "equal"
                            and numeric_stock != stock_level
                        ):
                            continue
                    else:
                        # Default behavior (greater than or equal to)
                        if numeric_stock < stock_level:
                            continue
                else:
                    # Non-numeric stock levels (out_of_stock, discontinued) don't meet numeric requirements
                    continue

            # Apply item_ids filter if specified
            if item_ids and item_id not in item_ids:
                continue

            # Apply product_types filter if specified
            product_id = item_to_product_map.get(item_id)
            if product_types and product_id:
                product_name = (
                    product_details_map.get(product_id, {})
                    .get("product_name", "")
                    .lower()
                )
                type_matches = any(
                    ptype.lower() in product_name for ptype in product_types
                )
                if not type_matches:
                    continue

            # Get product and variant details
            if product_id and product_id in product_details_map:
                product_info = product_details_map[product_id]

                # Get variant details
                product_variants = next(
                    (
                        p.get("variants", {})
                        for p in products
                        if p.get("product_id") == product_id
                    ),
                    {},
                )
                variant_info = product_variants.get(item_id, {})

                matching_items.append(
                    {
                        "item_id": item_id,
                        "product_id": product_id,
                        "product_name": product_info["product_name"],
                        "product_category": product_info["product_category"],
                        "stock_level": stock_level_value,
                        "numeric_stock_level": (
                            int(stock_level_value)
                            if isinstance(stock_level_value, (int, str))
                            and str(stock_level_value).isdigit()
                            else 0
                        ),
                        "price": variant_info.get("price", 0),
                        "available": variant_info.get("available", False),
                        "options": variant_info.get("options", {}),
                    }
                )

        result = {
            "status": "success",
            "supplier_id": supplier_id,
            "filters_applied": {
                "product_types": product_types,
                "item_ids": item_ids,
                "stock_available": stock_available,
                "stock_level_threshold": stock_level,
                "stock_level_comparison": (
                    stock_level_comparison
                    if stock_level_comparison
                    else "greater_than_or_equal"
                ),
            },
            "items": matching_items,
            "total_items": len(matching_items),
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSupplierInventory",
                "description": "Get supplier inventory filtered by product types, item IDs, stock availability, and stock level with comparison options (above, below, equal)",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier identifier (e.g., '#SUP0001')",
                        },
                        "product_types": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional list of product types to filter by (e.g., ['laptop', 'smartphone', 't-shirt']). Matches product names containing these terms (case-insensitive).",
                        },
                        "item_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional list of specific item IDs to include in results. Only these specific items will be returned if they exist in supplier's inventory.",
                        },
                        "stock_available": {
                            "type": "boolean",
                            "description": "Optional stock availability filter: true = only items with stock available, false = only out_of_stock/discontinued items, null/undefined = all items regardless of stock status",
                        },
                        "stock_level": {
                            "type": "integer",
                            "description": "Optional stock level threshold for filtering. Works with stock_level_comparison parameter.",
                            "minimum": 0,
                        },
                        "stock_level_comparison": {
                            "type": "string",
                            "description": "Optional comparison operator for stock level filtering. Requires stock_level to be specified. 'above' = greater than threshold, 'below' = less than threshold, 'equal' = exactly equal to threshold. If not specified, defaults to greater than or equal (>=).",
                            "enum": ["above", "below", "equal"],
                        },
                    },
                    "required": ["supplier_id"],
                },
            },
        }


class SearchGetSupplyOrders:
    @staticmethod
    def invoke(
        data: dict[str, Any],
        supplier_ids: list[str],
        min_quantity: int = None,
        max_quantity: int = None,
        status: str = None,
        statuses: list[str] = None,
        min_cost: float = None,
        max_cost: float = None,
    ) -> str:
        """
        Search and retrieve supply orders for specified suppliers with optional filtering
        Returns only product_ids, item_ids, supplier_ids, and supply_order_ids

        Data Sources: supply_orders.json (supply_order_id, supplier_id, quantity, status, total_cost)
        """
        if not supplier_ids:
            payload = {"error": "Supplier IDs list cannot be empty", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Basic validation
        if min_quantity is not None and min_quantity < 0:
            payload = {"error": "Minimum quantity must be non-negative", "status": "failed"}
            out = json.dumps(payload)
            return out
        if max_quantity is not None and max_quantity < 0:
            payload = {"error": "Maximum quantity must be non-negative", "status": "failed"}
            out = json.dumps(payload)
            return out
        if min_cost is not None and min_cost < 0:
            payload = {"error": "Minimum cost must be non-negative", "status": "failed"}
            out = json.dumps(payload)
            return out
        if max_cost is not None and max_cost < 0:
            payload = {"error": "Maximum cost must be non-negative", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Handle status filtering (single or multiple)
        if status and statuses:
            payload = {
                "error": "Cannot specify both 'status' and 'statuses' parameters. Use one or the other.",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        status_filter = []
        valid_statuses = ["pending", "fulfilled", "cancelled"]

        if status:
            if status not in valid_statuses:
                payload = {
                    "error": f"Invalid status '{status}'. Valid statuses: {', '.join(valid_statuses)}",
                    "status": "failed",
                }
                out = json.dumps(payload)
                return out
            status_filter = [status]
        elif statuses:
            invalid_statuses = [s for s in statuses if s not in valid_statuses]
            if invalid_statuses:
                payload = {
                    "error": f"Invalid statuses: {', '.join(invalid_statuses)}. Valid statuses: {', '.join(valid_statuses)}",
                    "status": "failed",
                }
                out = json.dumps(payload)
                return out
            status_filter = statuses

        # Get product information for item-to-product mapping
        products = data.get("products", [])
        item_to_product_map = {}
        for product in products:
            product_id = product.get("product_id")
            if product_id:
                variants = product.get("variants", {})
                for item_id in variants.keys():
                    item_to_product_map[item_id] = product_id

        # Filter supply orders and collect IDs
        supply_orders = data.get("supply_orders", [])
        all_supply_order_ids = set()
        all_supplier_ids = set()
        all_product_ids = set()
        all_item_ids = set()

        for order in supply_orders:
            order_supplier_id = order.get("supplier_id")
            order_quantity = order.get("quantity", 0)
            order_status = order.get("status", "")
            order_cost = order.get("total_cost", 0.0)

            # Apply filters
            if order_supplier_id not in supplier_ids:
                continue
            if min_quantity is not None and order_quantity < min_quantity:
                continue
            if max_quantity is not None and order_quantity > max_quantity:
                continue
            if status_filter and order_status not in status_filter:
                continue
            if min_cost is not None and order_cost < min_cost:
                continue
            if max_cost is not None and order_cost > max_cost:
                continue

            # Collect IDs from matching orders
            supply_order_id = order.get("supply_order_id")
            if supply_order_id:
                all_supply_order_ids.add(supply_order_id)

            if order_supplier_id:
                all_supplier_ids.add(order_supplier_id)

            # Get product_ids and item_ids
            if order.get("product_id"):
                all_product_ids.add(order.get("product_id"))

            if order.get("item_id"):
                all_item_ids.add(order.get("item_id"))
                # Map item to product if not already present
                product_id = item_to_product_map.get(order.get("item_id"))
                if product_id:
                    all_product_ids.add(product_id)

            # Handle multi-item orders
            if "items" in order and order.get("items"):
                for item_detail in order.get("items", []):
                    item_id = item_detail.get("item_id")
                    if item_id:
                        all_item_ids.add(item_id)
                        # Map item to product
                        product_id = item_to_product_map.get(item_id)
                        if product_id:
                            all_product_ids.add(product_id)

        # Convert sets to sorted lists
        result = {
            "status": "success",
            "supply_order_ids": sorted(list(all_supply_order_ids)),
            "supplier_ids": sorted(list(all_supplier_ids)),
            "product_ids": sorted(list(all_product_ids)),
            "item_ids": sorted(list(all_item_ids)),
            "total_orders": len(all_supply_order_ids),
            "total_suppliers": len(all_supplier_ids),
            "total_products": len(all_product_ids),
            "total_items": len(all_item_ids),
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchGetSupplyOrders",
                "description": "Search and retrieve supply orders for specified suppliers with optional filtering. Returns only the essential IDs: supply_order_ids, supplier_ids, product_ids, and item_ids.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of supplier identifiers to search orders for (e.g., ['#SUP0001', '#SUP0002'])",
                        },
                        "min_quantity": {
                            "type": "integer",
                            "description": "Optional minimum quantity filter - only returns orders with quantity >= this value",
                            "minimum": 0,
                        },
                        "max_quantity": {
                            "type": "integer",
                            "description": "Optional maximum quantity filter - only returns orders with quantity <= this value",
                            "minimum": 0,
                        },
                        "status": {
                            "type": "string",
                            "description": "Optional single status filter - only returns orders with this status (cannot be used with 'statuses')",
                            "enum": ["pending", "fulfilled", "cancelled"],
                        },
                        "statuses": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "enum": ["pending", "fulfilled", "cancelled"],
                            },
                            "description": "Optional list of statuses to filter by - returns orders matching any of these statuses (cannot be used with 'status')",
                        },
                        "min_cost": {
                            "type": "number",
                            "description": "Optional minimum total cost filter - only returns orders with total_cost >= this value",
                            "minimum": 0,
                        },
                        "max_cost": {
                            "type": "number",
                            "description": "Optional maximum total cost filter - only returns orders with total_cost <= this value",
                            "minimum": 0,
                        },
                    },
                    "required": ["supplier_ids"],
                },
            },
        }


TOOLS = [
    ProcessPayment(),
    AllocateInventory(),
    AssignCourier(),
    ValidateOrderItems(),
    ValidateShippingAddress(),
    CheckSupplyOrderStatus(),
    SearchProductsByFilter(),
    GetUserOrderHistory(),
    CalculateShippingCost(),
    ValidateSupplierCapacity(),
    GenerateOrderSummary(),
    CreateSupplyOrder(),
    UpdateOrderStatus(),
    CreateOrder(),
    UpdateSupplyOrderStatus(),
    UpdateProductAvailability(),
    ValidateUserIdentity(),
    CancelOrder(),
    UpdateDeliveryAddress(),
    AddPaymentMethod(),
    UpdateUserProfile(),
    RequestOrderReturn(),
    GetPurchasedItems(),
    GetCourier(),
    VerifyGiftCardBalance(),
    CheckOrderStatus(),
    GetUserInfo(),
    GetProductInfo(),
    CheckUserPaymentMethods(),
    UpdateSupplierInfo(),
    UpdateInventoryStock(),
    UpdateSupplyOrderTerms(),
    GetSupplierDetails(),
    GetSupplyOrderDetails(),
    SearchSuppliersByProduct(),
    GetProductIds(),
    GetSupplierByProduct(),
    GetItemIdByProduct(),
    GetProductItemsPerSupplier(),
    UpdateSupplierProduct(),
    GetCourierByName(),
    FilterByProductIdPerProductName(),
    AddToOrder(),
    GetOrderIdsByProductIds(),
    AssignTrackingNumber(),
    GetSupplierInventory(),
    SearchGetSupplyOrders(),
]
