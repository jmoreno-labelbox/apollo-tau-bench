from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

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
        users = data.get("users", {}).values()
        user = next((u for u in users.values() if u.get("user_id") == user_id), None)

        if not user:
            payload = {"error": f"User {user_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Use custom address if provided, otherwise use user's stored address
        address = custom_address if custom_address else user.get("address", {}).values()

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
        couriers = data.get("couriers", {}).values()
        supported_countries = set()
        for courier in couriers.values():
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
