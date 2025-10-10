# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignCourier(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], destination_country: str, order_value: float = None, order_values: List[float] = None, location: Dict[str, str] = None, tracking_ids: List[str] = None, **kwargs) -> str:
        """
        Assign appropriate courier for order delivery based on coverage and requirements
        Supports both single order value and multiple order values for batch processing
        Uses a single tracking ID for all scenarios (single order or multiple orders)

        Data Sources: couriers.json (courier_id, name, coverage_area, contact_info)
        """
        # Check the input arguments for validity.
        if order_value is not None and order_values is not None:
            return json.dumps({
                "error": "Cannot specify both order_value and order_values. Use one or the other.",
                "status": "failed"
            })

        if order_value is None and order_values is None:
            return json.dumps({
                "error": "Either order_value or order_values must be provided",
                "status": "failed"
            })

        # Check the tracking_ids parameter for validity if it is included.
        if tracking_ids is not None:
            # In single tracking ID mode, allow either a single tracking ID or mandate uniformity across all IDs.
            if len(tracking_ids) == 1:
                # Unified tracking ID for all orders - this is our goal.
                single_tracking_id = tracking_ids[0]
            elif len(tracking_ids) > 1:
                # Verify that all tracking IDs are identical.
                if len(set(tracking_ids)) == 1:
                    single_tracking_id = tracking_ids[0]
                else:
                    return json.dumps({
                        "error": "For single tracking ID mode, all tracking_ids must be the same or provide only one tracking_id",
                        "status": "failed"
                    })
            else:
                return json.dumps({
                    "error": "tracking_ids cannot be empty if provided",
                    "status": "failed"
                })

        # Create a list of order values for processing.
        values_to_process = []
        if order_value is not None:
            if order_value < 0:
                return json.dumps({
                    "error": "Order value cannot be negative",
                    "status": "failed"
                })
            values_to_process.append(order_value)

        if order_values is not None:
            if not order_values:
                return json.dumps({
                    "error": "Order values list cannot be empty",
                    "status": "failed"
                })
            for i, value in enumerate(order_values):
                if not isinstance(value, (int, float)) or value < 0:
                    return json.dumps({
                        "error": f"Order value at index {i} must be a non-negative number: {value}",
                        "status": "failed"
                    })
            values_to_process = order_values

        # Condition: Only assign couriers if the destination country falls within their designated coverage regions.
        couriers = data.get("couriers", [])
        eligible_couriers = []

        for courier in couriers:
            coverage_area = courier.get("coverage_area", [])
            if destination_country in coverage_area:
                eligible_couriers.append(courier)

        if not eligible_couriers:
            return json.dumps({
                "error": f"No couriers available for destination country: {destination_country}",
                "status": "failed"
            })

        # Choose a courier based on user preference or enable automatic selection.
        selected_courier = eligible_couriers[0]  # Basic selection criteria
        if "courier_id" in kwargs:
            courier_id = kwargs["courier_id"]
            selected_courier = next((c for c in eligible_couriers if c.get("courier_id") == courier_id), selected_courier)

        # Retrieve the courier's tracking pool for backup generation.
        tracking_ids_pool = selected_courier.get("tracking_ids", [])

        # Handle location data if available.
        delivery_location = None
        if location:
            # Check that the location contains all necessary fields.
            required_location_fields = ["city", "country"]
            missing_fields = [field for field in required_location_fields if not location.get(field)]

            if missing_fields:
                return json.dumps({
                    "error": f"Location missing required fields: {', '.join(missing_fields)}",
                    "status": "failed"
                })

            delivery_location = {
                "address1": location.get("address1", ""),
                "address2": location.get("address2", ""),
                "city": location.get("city"),
                "state": location.get("state", ""),
                "zip": location.get("zip", ""),
                "country": location.get("country")
            }

            # Check if the location's country corresponds to the destination_country parameter.
            if delivery_location["country"] != destination_country:
                return json.dumps({
                    "error": f"Location country '{delivery_location['country']}' does not match destination_country '{destination_country}'",
                    "status": "failed"
                })

        # Create a unified tracking ID for all orders, regardless of quantity.
        batch_mode = len(values_to_process) > 1

        if tracking_ids is not None:
            # Utilize the specified single tracking ID.
            assigned_tracking_id = single_tracking_id
            tracking_source = "custom_provided"
        else:
            # Create a unique tracking identifier.
            if batch_mode:
                # Generate a batch tracking ID for several orders.
                batch_identifier = f"BATCH{len(values_to_process):02d}"
                courier_code = selected_courier.get("courier_id", "").replace("#", "").replace("COU", "C")
                assigned_tracking_id = f"TRK{batch_identifier}{courier_code}"
            else:
                # Utilize standard generation with individual tracking for single orders.
                base_tracking_id = tracking_ids_pool[0] if tracking_ids_pool else "TRK001"
                total_value = values_to_process[0]
                assigned_tracking_id = f'{base_tracking_id}-{total_value}'
            tracking_source = "courier_pool_generated"

        # Handle all order values using the identical tracking ID.
        courier_assignments = []
        total_order_value = sum(values_to_process)
        high_value_orders = 0

        for i, current_order_value in enumerate(values_to_process):
            # Guideline: Orders exceeding $1000 must undergo payment verification prior to processing.
            requires_insurance = current_order_value > 1000.0
            if requires_insurance:
                high_value_orders += 1

            courier_assignments.append({
                "order_index": i + 1 if batch_mode else None,
                "order_value": current_order_value,
                "assigned_tracking_id": assigned_tracking_id,  # Uniform tracking ID for all.
                "tracking_source": tracking_source,
                "requires_insurance": requires_insurance,
            })

        # Compute metrics for the batch.
        batch_metrics = {
            "total_orders": len(values_to_process),
            "total_order_value": round(total_order_value, 2),
            "high_value_orders": high_value_orders,
            "average_order_value": round(total_order_value / len(values_to_process), 2),
            "min_order_value": min(values_to_process),
            "max_order_value": max(values_to_process),
            "single_tracking_id_used": True,
            "tracking_id_sharing": True  # Always valid now as we consistently utilize single tracking.
        }

        result = {
            "status": "success",
            "batch_processing": batch_mode,
            "courier_assignment": {
                "courier_id": selected_courier.get("courier_id"),
                "courier_name": selected_courier.get("name"),
                "contact_info": selected_courier.get("contact_info"),
                "destination_country": destination_country,
                "delivery_location": delivery_location
            },
            "tracking_configuration": {
                "single_tracking_id": assigned_tracking_id,
                "shared_across_orders": True,  # Currently always true
                "tracking_source": tracking_source,
                "custom_tracking_provided": tracking_ids is not None,
                "courier_tracking_pool_size": len(tracking_ids_pool)
            },
            "batch_metrics": batch_metrics,
            "order_assignments": courier_assignments,
            "processing_summary": {
                "total_assignments": len(courier_assignments),
                "high_value_assignments": high_value_orders,
            }
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_courier",
                "description": "Assign courier for order delivery based on destination and order requirements. Supports both single order value and batch processing with multiple order values. Always uses a single tracking ID for all orders (whether single or multiple).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "destination_country": {"type": "string", "description": "Destination country for delivery"},
                        "order_value": {"type": "number", "description": "Single order value in dollars. Cannot be used with order_values. Uses single tracking ID."},
                        "order_values": {
                            "type": "array",
                            "items": {"type": "number"},
                            "description": "Array of order values in dollars for batch processing. Cannot be used with order_value. All orders will share a single tracking ID."
                        },
                        "location": {
                            "type": "object",
                            "properties": {
                                "address1": {"type": "string", "description": "Primary street address"},
                                "address2": {"type": "string", "description": "Secondary address line (apartment, suite, etc.)"},
                                "city": {"type": "string", "description": "City name"},
                                "state": {"type": "string", "description": "State or province"},
                                "zip": {"type": "string", "description": "ZIP or postal code"},
                                "country": {"type": "string", "description": "Country name"}
                            },
                            "required": ["city", "country"],
                            "description": "Optional detailed delivery address information"
                        },
                        "tracking_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional single tracking ID for all orders. Provide either one tracking ID (which will be used for all orders) or the same tracking ID repeated. Can be used with both single order and multiple orders."
                        },
                        "courier_id": {
                            "type": "string",
                            "description": "Optional specific courier ID to assign, if known"
                        }
                    },
                    "required": ["destination_country"],
                    "anyOf": [
                        {"required": ["order_value"]},
                        {"required": ["order_values"]}
                    ]
                }
            }
        }
