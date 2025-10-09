from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

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
},
            },
        }
