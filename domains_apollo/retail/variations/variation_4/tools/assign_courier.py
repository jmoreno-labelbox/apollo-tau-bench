from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

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
