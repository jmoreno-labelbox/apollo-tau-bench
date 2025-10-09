from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

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
            couriers = data.get("couriers", {}).values()

            for courier in couriers.values():
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
        orders = data.get("orders", {}).values()
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
            for i, order in enumerate(orders.values()):
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
},
            },
        }
