# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ValidateShippingAddress(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, custom_address: Dict[str, str] = None) -> str:
        """
        Validate shipping address for order fulfillment
        """
        # Requirement: Ensure the user's identity is confirmed prior to handling any requests.
        users = list(data.get("users", {}).values())
        user = next((u for u in users if u.get("user_id") == user_id), None)

        if not user:
            return json.dumps({"error": f"User {user_id} not found", "status": "failed"})

        # Utilize the specified address if available; otherwise, fallback to the user's saved address.
        address = custom_address if custom_address else user.get("address", {})

        # Requirement: Ensure all mandatory address fields are validated: address1, city, country, state, zip.
        required_fields = ["address1", "city", "country", "state", "zip"]
        missing_fields = []

        for field in required_fields:
            if not address.get(field):
                missing_fields.append(field)

        if missing_fields:
            return json.dumps({
                "error": f"Missing required address fields: {', '.join(missing_fields)}",
                "status": "failed"
            })

        # Extra checks for validated countries.
        couriers = data.get("couriers", [])
        supported_countries = set()
        for courier in couriers:
            supported_countries.update(courier.get("coverage_area", []))

        destination_country = address.get("country")
        if destination_country not in supported_countries:
            return json.dumps({
                "error": f"No delivery service available to {destination_country}",
                "status": "failed"
            })

        result = {
            "status": "success",
            "user_id": user_id,
            "validated_address": address,
            "destination_country": destination_country,
            "delivery_available": True
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "validate_shipping_address",
                "description": "Validate shipping address completeness and delivery availability",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Customer identifier"},
                        "custom_address": {
                            "type": "object",
                            "properties": {
                                "address1": {"type": "string"},
                                "address2": {"type": "string"},
                                "city": {"type": "string"},
                                "country": {"type": "string"},
                                "state": {"type": "string"},
                                "zip": {"type": "string"}
                            },
                            "description": "Optional custom shipping address, uses user's stored address if not provided"
                        }
                    },
                    "required": ["user_id"]
                }
            }
        }
