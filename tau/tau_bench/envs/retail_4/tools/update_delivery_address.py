# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateDeliveryAddress(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, order_id: str, new_address: Dict[str, str]) -> str:
        """
        Update delivery address for an existing order (if not yet shipped)

        Writes to: orders.json (updates order address)
        Data Sources: couriers.json for delivery validation
        """
        # Requirement: Confirm the existence of user identity prior to handling any requests.
        users = list(data.get("users", {}).values())
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            return json.dumps({"error": f"User {user_id} not found", "status": "failed"})

        # Determine the sequence for updates.
        orders = list(data.get("orders", {}).values())
        order_to_update = None
        order_index = None

        for i, order in enumerate(orders):
            if order.get("order_id") == order_id and order.get("user_id") == user_id:
                order_to_update = order
                order_index = i
                break

        if not order_to_update:
            return json.dumps({
                "error": f"Order {order_id} not found or does not belong to user {user_id}",
                "status": "failed"
            })

        current_status = order_to_update.get("status")

        # Address updates are allowed solely for pending orders.
        if current_status not in ["pending"]:
            return json.dumps({
                "error": f"Cannot update address for order with status '{current_status}'. Address can only be changed for pending orders.",
                "status": "failed"
            })

        # Requirement: Check that all mandatory address fields are filled: address1, city, country, state, zip.
        required_fields = ["address1", "city", "country", "state", "zip"]
        missing_fields = []

        for field in required_fields:
            if not new_address.get(field):
                missing_fields.append(field)

        if missing_fields:
            return json.dumps({
                "error": f"Missing required address fields: {', '.join(missing_fields)}",
                "status": "failed"
            })

        # Condition: Assign couriers solely when the destination country aligns with their service regions.
        couriers = data.get("couriers", [])
        supported_countries = set()
        for courier in couriers:
            supported_countries.update(courier.get("coverage_area", []))

        destination_country = new_address.get("country")
        if destination_country not in supported_countries:
            return json.dumps({
                "error": f"No delivery service available to {destination_country}",
                "status": "failed"
            })

        # UPDATE OPERATION: Modify order shipping address
        old_address = order_to_update.get("address", {})
        order_to_update["address"] = new_address
        order_to_update["address_updated"] = {
            "updated_date": datetime.now().isoformat(),
            "updated_by": "customer",
            "previous_address": old_address
        }
        order_to_update["last_updated"] = datetime.now().isoformat()

        # Revise the sequence in the data structure.
        data["orders"][order_index] = order_to_update

        result = {
            "status": "success",
            "order_id": order_id,
            "user_id": user_id,
            "address_update": {
                "previous_address": old_address,
                "new_address": new_address,
                "delivery_available": True,
                "destination_country": destination_country
            },
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_delivery_address",
                "description": "Update delivery address for a pending order",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Customer identifier"},
                        "order_id": {"type": "string", "description": "Order identifier to update"},
                        "new_address": {
                            "type": "object",
                            "properties": {
                                "address1": {"type": "string"},
                                "address2": {"type": "string"},
                                "city": {"type": "string"},
                                "country": {"type": "string"},
                                "state": {"type": "string"},
                                "zip": {"type": "string"}
                            },
                            "required": ["address1", "city", "country", "state", "zip"],
                            "description": "New delivery address"
                        }
                    },
                    "required": ["user_id", "order_id", "new_address"]
                }
            }
        }
