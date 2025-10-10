# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCartByContactId(Tool):
    """Fetch full cart details by contact_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], contact_id: Any) -> str:
        contact_id = _idstr(contact_id)
        if not contact_id:
            return json.dumps({"error": "Missing required field: contact_id"}, indent=2)
        carts = list(data.get("carts", {}).values())
        for cart in carts:
            if cart.get("contact_id") == contact_id:
                return json.dumps(cart, indent=2)

        return json.dumps({"error": f"No cart found for contact_id '{contact_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_cart_by_contact_id",
                "description": "Fetch full cart details by contact_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact_id": {
                            "type": "string",
                            "description": "Exact contact ID to retrieve cart for.",
                        }
                    },
                    "required": ["contact_id"],
                },
            },
        }
