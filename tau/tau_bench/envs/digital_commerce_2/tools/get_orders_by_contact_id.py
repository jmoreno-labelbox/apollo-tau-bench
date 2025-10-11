# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _idstr(v):
    return str(v) if isinstance(v, int) else v

class GetOrdersByContactId(Tool):
    """Fetch all orders for a given contact_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], contact_id: Any) -> str:
        contact_id = _idstr(contact_id)
        if not contact_id:
            return json.dumps({"error": "Missing required field: contact_id"}, indent=2)

        orders = list(data.get("orders", {}).values())
        contact_orders = [o for o in orders if o.get("contact_id") == contact_id]
        return json.dumps(contact_orders, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_orders_by_contact_id",
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