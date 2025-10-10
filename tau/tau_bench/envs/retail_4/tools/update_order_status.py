# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateOrderStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str = None, order_ids: List[str] = None, new_status: str = None, tracking_id: str = None, courier_id: str = None) -> str:
        """
        Update order status and add fulfillment tracking information
        Supports both single order and batch processing

        Writes to: orders.json (updates existing order status and fulfillments)
        Data Sources: couriers.json for tracking validation
        """
        # Verify input arguments.
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

        if not new_status:
            return json.dumps({
                "error": "new_status is required",
                "status": "failed"
            })

        # Condition: Only handle orders that have a valid status: pending, processed, delivered, or cancelled.
        valid_statuses = ["pending", "processed", "delivered", "cancelled", "for return"]
        if new_status not in valid_statuses:
            return json.dumps({
                "error": f"Invalid status '{new_status}'. Valid statuses: {', '.join(valid_statuses)}",
                "status": "failed"
            })

        # Create a list of orders for processing.
        orders_to_process = []
        if order_id:
            orders_to_process.append(order_id.strip())
        if order_ids:
            orders_to_process.extend([oid.strip() for oid in order_ids if oid and oid.strip()])

        if not orders_to_process:
            return json.dumps({
                "error": "No valid order IDs provided",
                "status": "failed"
            })

        # Check the tracking and courier information if available.
        selected_courier = None
        if tracking_id and courier_id:
            couriers = data.get("couriers", [])

            for courier in couriers:
                if courier.get("courier_id") == courier_id:
                    selected_courier = courier
                    break

            if not selected_courier:
                return json.dumps({"error": f"Courier {courier_id} not found", "status": "failed"})

            # Directive: Verify tracking_id allocations against the courier's tracking pools to avoid duplication.
            courier_tracking_ids = selected_courier.get("tracking_ids", [])
            if tracking_id not in courier_tracking_ids:
                return json.dumps({
                    "error": f"Tracking ID {tracking_id} not available for courier {courier_id}",
                    "status": "failed"
                })
        elif (tracking_id and not courier_id) or (not tracking_id and courier_id):
            return json.dumps({
                "error": "Both tracking_id and courier_id must be provided together, or neither",
                "status": "failed"
            })

        # Locate and handle all orders.
        orders = list(data.get("orders", {}).values())
        successful_updates = []
        failed_updates = []

        for order_id_input in orders_to_process:
            # Add # Prefix with # if absent (for ease of use)
            formatted_order_id = order_id_input if order_id_input.startswith("#") else f"#{order_id_input}"

            order_found = False
            for i, order in enumerate(orders):
                if order.get("order_id") == formatted_order_id:
                    order_found = True
                    old_status = order.get("status")

                    # Include fulfillment details when tracking information is available.
                    if tracking_id and courier_id and selected_courier:
                        fulfillment_entry = {
                            "tracking_id": tracking_id,
                            "courier_id": courier_id,
                            "courier_name": selected_courier.get("name"),
                            "status": new_status,
                            "timestamp": datetime.now().isoformat()
                        }

                        # UPDATE OPERATION: Modify fulfillments array
                        if "fulfillments" not in order:
                            order["fulfillments"] = []
                        order["fulfillments"].append(fulfillment_entry)

                    # UPDATE OPERATION: Modify the order status within orders.json
                    order["status"] = new_status
                    order["last_updated"] = datetime.now().isoformat()

                    # Modify the sequence within the data structure.
                    data["orders"][i] = order

                    successful_updates.append({
                        "order_id": formatted_order_id,
                        "user_id": order.get("user_id"),
                        "previous_status": old_status,
                        "new_status": new_status,
                        "tracking_info": {
                            "tracking_id": tracking_id,
                            "courier_id": courier_id,
                            "courier_name": selected_courier.get("name") if selected_courier else None
                        } if tracking_id and courier_id else None,
                        "fulfillments_count": len(order.get("fulfillments", [])),
                        "last_updated": order["last_updated"]
                    })
                    break

            if not order_found:
                failed_updates.append({
                    "order_id": formatted_order_id,
                    "error": "Order not found"
                })

        # Develop a thorough reply.
        result = {
            "status": "success" if successful_updates else "failed",
            "batch_processing": len(orders_to_process) > 1,
            "processing_summary": {
                "total_processed": len(orders_to_process),
                "successful_updates": len(successful_updates),
                "failed_updates": len(failed_updates)
            },
            "new_status": new_status,
            "tracking_assignment": {
                "tracking_id": tracking_id,
                "courier_id": courier_id,
                "courier_name": selected_courier.get("name") if selected_courier else None
            } if tracking_id and courier_id else None,
            "successful_updates": successful_updates,
            "failed_updates": failed_updates
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_order_status",
                "description": "Update order status and add tracking information. Supports both single order and batch processing.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "Single order identifier to update. Cannot be used with order_ids."},
                        "order_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Array of order identifiers for batch processing. Cannot be used with order_id."
                        },
                        "new_status": {"type": "string", "description": "New status (pending, processed, delivered, cancelled)"},
                        "tracking_id": {"type": "string", "description": "Tracking number for shipment (optional, requires courier_id)"},
                        "courier_id": {"type": "string", "description": "Courier identifier (required if tracking_id provided)"}
                    },
                    "anyOf": [
                        {"required": ["order_id", "new_status"]},
                        {"required": ["order_ids", "new_status"]}
                    ]
                }
            }
        }
