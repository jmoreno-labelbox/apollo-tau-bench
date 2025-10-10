# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindOutboundOrderBySO(Tool):
    """Finds a single outbound order record by its Sales Order (SO) number."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        so_number = kwargs.get("sales_order_number")
        outbound_orders = list(data.get("outbound_orders", {}).values())
        for order in outbound_orders:
            if order.get("sales_order_number") == so_number:
                return json.dumps(order)
        return json.dumps(
            {"error": "Outbound order not found for that Sales Order number"}
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_outbound_order_by_so",
                "description": "Finds the full details of an outbound order using its Sales Order (SO) number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sales_order_number": {
                            "type": "string",
                            "description": "The Sales Order number of the order to find (e.g., 'SO-2024-0002').",
                        }
                    },
                    "required": ["sales_order_number"],
                },
            },
        }
