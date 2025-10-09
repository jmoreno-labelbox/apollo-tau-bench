from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal

class GetOrdersByContactId(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], contact_id: Any) -> str:
        contact_id = _idstr(contact_id)
        if not contact_id:
            payload = {"error": "Missing required field: contact_id"}
            out = json.dumps(payload, indent=2)
            return out

        orders = data.get("orders", [])
        contact_orders = [o for o in orders if o.get("contact_id") == contact_id]
        payload = contact_orders
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrdersByContactId",
                "description": "Fetch all orders for a given contact_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact_id": {
                            "type": "string",
                            "description": "Exact contact ID to retrieve orders for.",
                        }
                    },
                    "required": ["contact_id"],
                },
            },
        }
