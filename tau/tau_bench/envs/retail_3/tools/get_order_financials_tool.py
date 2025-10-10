# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOrderFinancialsTool(Tool):
    """Gets financial data for an order from the shared in-memory state."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id) -> str:
        # Fetches the 'orders' object from the in-memory state, which might have been altered.
        orders = list(data.get("orders", {}).values())

        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps(
                {"error": f"Order '{order_id}' not found in the current state"}, indent=2
            )

        # This will now incorporate changes made by earlier tools.
        return json.dumps(
            {"order_id": order_id, "items_total": order.get("items_total", 0)}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_order_financials",
                "description": "Retrieves financial totals for a given order from the current state.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }
