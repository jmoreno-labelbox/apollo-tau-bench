# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOutboundOrderDetailsBySo(Tool):
    """Retrieves order details using the Sales Order (SO) number."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sales_order_number = kwargs.get('sales_order_number')
        if not sales_order_number:
            return json.dumps({"error": "sales_order_number is a required argument."}, indent=2)

        order = next((o for o in data.get('outbound_orders', []) if o.get('sales_order_number') == sales_order_number), None)

        if not order:
            return json.dumps({"error": f"Order with Sales Order number '{sales_order_number}' not found."}, indent=2)

        return json.dumps(order, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_outbound_order_details_by_so",
                "description": "Retrieves the full details for a single outbound order by its Sales Order (SO) number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sales_order_number": {"type": "string", "description": "The Sales Order number (e.g., 'SO-2024-0001')."}
                    },
                    "required": ["sales_order_number"]
                }
            }
        }
