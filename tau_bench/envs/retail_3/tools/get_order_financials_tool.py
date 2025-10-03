from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime
from typing import Any

class GetOrderFinancialsTool(Tool):
    """Retrieves financial information for an order from the shared in-memory state."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None) -> str:
        # Fetches the 'orders' object from the in-memory state, which could have been altered.
        orders = data.get("orders", [])

        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"Order '{order_id}' not found in the current state"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {"order_id": order_id, "items_total": order.get("items_total", 0)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrderFinancials",
                "description": "Retrieves financial totals for a given order from the current state.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }
