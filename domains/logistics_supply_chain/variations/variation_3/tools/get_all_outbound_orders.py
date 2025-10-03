from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class GetAllOutboundOrders(Tool):
    """Fetches all outbound order records from the dataset, with filtering options."""

    @staticmethod
    def invoke(data: dict[str, Any], filters: dict[str, Any] = None) -> str:
        outbound_orders = data.get("outbound_orders", [])

        if not outbound_orders:
            payload = {"message": "No outbound orders found."}
            out = json.dumps(payload)
            return out

        if not filters:
            payload = outbound_orders
            out = json.dumps(payload)
            return out

        filtered_orders = []
        for order in outbound_orders:
            match = True
            for key, value in filters.items():
                order_value = order.get(key)
                if isinstance(order_value, str) and isinstance(value, str):
                    if order_value.lower() != value.lower():
                        match = False
                        break
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
            payload = filtered_orders
            out = json.dumps(payload)
            return out
        else:
            payload = {"message": "No outbound orders found matching the specified filters."}
            out = json.dumps(payload)
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllOutboundOrders",
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
