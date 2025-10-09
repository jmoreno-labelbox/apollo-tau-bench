from tau_bench.envs.tool import Tool
import json
import random
from typing import Any

class GetOutboundOrderDetailsBySo(Tool):
    """Obtains order details by referencing the Sales Order (SO) number."""

    @staticmethod
    def invoke(data: dict[str, Any], sales_order_number: str = None) -> str:
        if not sales_order_number:
            payload = {"error": "sales_order_number is a required argument."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        order = next(
            (
                o
                for o in data.get("outbound_orders", [])
                if o.get("sales_order_number") == sales_order_number
            ),
            None,
        )

        if not order:
            payload = {
                    "error": f"Order with Sales Order number '{sales_order_number}' not found."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = order
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOutboundOrderDetailsBySo",
                "description": "Retrieves the full details for a single outbound order by its Sales Order (SO) number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sales_order_number": {
                            "type": "string",
                            "description": "The Sales Order number (e.g., 'SO-2024-0001').",
                        }
                    },
                    "required": ["sales_order_number"],
                },
            },
        }
