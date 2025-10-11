# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignTrackingNumber(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str = None, order_ids: List[str] = None, preferred_courier_id: str = None, courier_id: str = None, destination_country: str = None) -> str:
        """
        Assign tracking number for pending orders using a preferred courier
        Supports both single order and batch processing
        When order_ids is used, creates a single tracking ID for all orders

        Writes to: orders.json (updates order fulfillments with tracking info)
        Data Sources: orders.json (order status validation), couriers.json (courier availability)
        """
        # Verify input arguments
        if not order_id and not order_ids:
            return json.dumps({
                "error": "Either order_id or order_ids must be provided",
                "status": "failed"
            })

        if order_id and order_ids:
            return json.dumps({
                "error": "Cannot specify both order_id and order_ids. Use one or the other.",
                "status": "failed"
            })

        # Create a list of orders for processing.
        orders_to_process = []
        batch_mode = False

        if order_id:
            orders_to_process.append(order_id.strip())
        if order_ids:
            orders_to_process.extend([oid.strip() for oid in order_ids if oid and oid.strip()])
            batch_mode = True

        if not orders_to_process:
            return json.dumps({
                "error": "No valid order IDs provided",
                "status": "failed"
            })

        # Manage both preferred_courier_id and courier_id parameters to ensure backward compatibility.
        selected_courier_preference = preferred_courier_id or courier_id

        # Retrieve and verify all orders.
        orders = list(data.get("orders", {}).values())
        valid_orders = []
        invalid_orders = []

        for order_id_input in orders_to_process:
            # Add # Prefix with # if absent (for ease of use)
            formatted_order_id = order_id_input if order_id_input.startswith("#") else f"#{order_id_input}"

            order_found = False
            for i, order in enumerate(orders):
                if order.get("order_id") == formatted_order_id:
                    current_status = order.get("status")

                    # Verify if the order qualifies for tracking assignment.
                    if current_status != "pending":
                        invalid_orders.append({
                            "order_id": formatted_order_id,
                            "error": f"Cannot assign tracking to order with status '{current_status}'. Tracking can only be assigned to pending orders.",
                            "current_status": current_status
                        })
                    else:
                        valid_orders.append({
                            "order_id": formatted_order_id,
                            "order_index": i,
                            "order_data": order
                        })
                    order_found = True
                    break

            if not order_found:
                invalid_orders.append({
                    "order_id": formatted_order_id,
                    "error": "Order not found"
                })

        if not valid_orders:
            return json.dumps({
                "error": "No valid orders found for tracking assignment",
                "status": "failed",
                "invalid_orders": invalid_orders,
                "total_processed": len(orders_to_process),
                "successful_assignments": 0,
                "failed_assignments": len(invalid_orders)
            })

        # Obtain the destination country from the initial order if it is unspecified.
        if not destination_country:
            first_order = valid_orders[0]["order_data"]
            order_address = first_order.get("address", {})
            destination_country = order_address.get("country")

            if not destination_country:
                return json.dumps({
                    "error": "Destination country not found in order address and not provided as parameter",
                    "status": "failed"
                })

        # Condition: Allocate couriers solely when the destination country aligns with their service regions.
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

        # Choose a courier according to preference or opt for automatic selection.
        selected_courier = None
        selection_method = "automatic"

        if selected_courier_preference:
            # Identify the selected courier if available.
            selected_courier = next((c for c in eligible_couriers if c.get("courier_id") == selected_courier_preference), None)

            if not selected_courier:
                # Preferred shipping option is unavailable; please suggest alternatives.
                available_courier_options = [
                    {"courier_id": c.get("courier_id"), "name": c.get("name"), "rating": c.get("rating", 0)}
                    for c in eligible_couriers
                ]
                return json.dumps({
                    "error": f"Preferred courier {selected_courier_preference} not available for destination {destination_country}",
                    "status": "failed",
                    "available_alternatives": available_courier_options
                })
            selection_method = "preferred"
        else:
            # Implement automated selection criteria to choose the top-rated courier.
            eligible_couriers.sort(key=lambda x: x.get("rating", 0), reverse=True)
            selected_courier = eligible_couriers[0]

        # Create a tracking identifier according to the mode (single or batch).
        if batch_mode:
            # Generate a unified tracking ID for every order in the batch.
            batch_identifier = f"BATCH{len(valid_orders):02d}"
            courier_code = selected_courier.get("courier_id", "").replace("#", "").replace("COU", "C")
            assigned_tracking_id = f"TRK{batch_identifier}{courier_code}"
            tracking_generation_method = "single_batch_tracking"
        else:
            # Generate tracking ID for a single order using order_id combined with courier_id.
            order_number = valid_orders[0]["order_id"].replace("#", "")
            courier_code = selected_courier.get("courier_id", "").replace("#", "").replace("COU", "C")
            assigned_tracking_id = f"TRK{order_number}{courier_code}"
            tracking_generation_method = "order_courier_based"

        # Handle all legitimate orders sharing the same tracking ID.
        successful_assignments = []
        total_batch_value = 0.0

        for order_info in valid_orders:
            order_data = order_info["order_data"]
            order_index = order_info["order_index"]
            formatted_order_id = order_info["order_id"]

            # Compute the value of the order for insurance purposes.
            order_items = order_data.get("items", [])
            order_value = sum(item.get("price", 0) * item.get("quantity", 1) for item in order_items)
            total_batch_value += order_value

            # Policy: Orders exceeding $1000 must undergo payment verification prior to processing.
            requires_insurance = order_value > 1000.0

            # EXECUTE OPERATION: Incorporate fulfillment details into the order.
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
                "batch_size": len(valid_orders) if batch_mode else 1
            }

            if "fulfillments" not in order_data:
                order_data["fulfillments"] = []
            order_data["fulfillments"].append(fulfillment_entry)

            # Change order status to processed.
            previous_status = order_data.get("status")
            order_data["status"] = "processed"
            order_data["last_updated"] = datetime.now().isoformat()

            # Modify the sequence in the data structure.
            data["orders"][order_index] = order_data

            successful_assignments.append({
                "order_id": formatted_order_id,
                "user_id": order_data.get("user_id"),
                "tracking_id": assigned_tracking_id,
                "courier_id": selected_courier.get("courier_id"),
                "courier_name": selected_courier.get("name"),
                "previous_status": previous_status,
                "new_status": "processed",
                "order_value": round(order_value, 2),
                "requires_insurance": requires_insurance,
                "assigned_date": fulfillment_entry["assigned_date"]
            })

        # Verify if the batch needs insurance (total value exceeds $1000).
        batch_requires_insurance = total_batch_value > 1000.0 if batch_mode else None

        # Develop a detailed reply.
        result = {
            "status": "success",
            "processing_summary": {
                "total_processed": len(orders_to_process),
                "successful_assignments": len(successful_assignments),
                "failed_assignments": len(invalid_orders)
            },
            "tracking_details": {
                "tracking_id": assigned_tracking_id,
                "shared_tracking": batch_mode,
                "tracking_generation_method": tracking_generation_method,
                "batch_requires_insurance": batch_requires_insurance
            },
            "courier_details": {
                "courier_id": selected_courier.get("courier_id"),
                "name": selected_courier.get("name"),
                "rating": selected_courier.get("rating", 0),
                "service_types": selected_courier.get("service_types", ["standard"]),
                "specialties": selected_courier.get("specialties", []),
                "selection_method": selection_method
            },
            "delivery_info": {
                "destination_country": destination_country,
                "tracking_generation_method": tracking_generation_method
            },
            "successful_assignments": successful_assignments,
            "failed_assignments": invalid_orders
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_tracking_number",
                "description": "Assign tracking number for pending orders using a preferred courier. Supports both single order and batch processing. When order_ids is used, creates a single shared tracking ID for all orders in the batch. Updates order status to 'processed' and adds fulfillment information.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Single order identifier (e.g., 'W6893533' or '#W6893533'). Cannot be used with order_ids. Creates individual tracking ID."
                        },
                        "order_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Array of order identifiers for batch processing (e.g., ['W6893533', '#W6893534']). Cannot be used with order_id. Creates single shared tracking ID for all orders."
                        },
                        "preferred_courier_id": {
                            "type": "string",
                            "description": "Optional preferred courier ID (e.g., 'COURIER001'). If not provided or unavailable, will auto-select the highest-rated available courier."
                        },
                        "courier_id": {
                            "type": "string",
                            "description": "Optional courier ID (e.g., 'COURIER001'). Alternative parameter name for preferred_courier_id for backward compatibility."
                        },
                        "destination_country": {
                            "type": "string",
                            "description": "Optional destination country for delivery. If not provided, will use country from first order's delivery address."
                        }
                    },
                    "anyOf": [
                        {"required": ["order_id"]},
                        {"required": ["order_ids"]}
                    ]
                }
            }
        }
