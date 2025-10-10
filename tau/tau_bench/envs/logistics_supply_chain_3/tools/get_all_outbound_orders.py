# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAllOutboundOrders(Tool):
    """Retrieves all outbound order records from the dataset, with an option to filter."""

    @staticmethod
    def invoke(data: Dict[str, Any], filters) -> str:
        outbound_orders = list(data.get("outbound_orders", {}).values())

        if not outbound_orders:
            return json.dumps({"message": "No outbound orders found."})

        if not filters:
            return json.dumps(outbound_orders)

        filtered_orders = []
        for order in outbound_orders:
            match = True
            for key, value in filters.items():
                order_value = order.get(key)
                # Manage case-insensitive string comparisons.
                if isinstance(order_value, str) and isinstance(value, str):
                    if order_value.lower() != value.lower():
                        match = False
                        break
                # Manage boolean comparisons for string values 'true'/'false'.
                elif isinstance(order_value, bool) and isinstance(value, str):
                    if str(order_value).lower() != value.lower():
                        match = False
                        break
                elif order_value != value:
                    match = False
                    break
            if match:
                filtered_orders.append(order)

        if filtered_orders:
            return json.dumps(filtered_orders)
        else:
            return json.dumps(
                {"message": "No outbound orders found matching the specified filters."}
            )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_outbound_orders",
                "description": "Retrieves a list of all outbound orders, with an option to filter by specific criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filters": {
                            "type": "object",
                            "description": "Optional. A dictionary of key-value pairs to filter the orders. Keys must be valid fields from the order record. Example: {'status': 'In Transit', 'fragile': true}",
                        }
                    },
                    "required": [],
                },
            },
        }
