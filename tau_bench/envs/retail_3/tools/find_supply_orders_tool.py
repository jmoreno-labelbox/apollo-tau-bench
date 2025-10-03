from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime
from typing import Any

class FindSupplyOrdersTool(Tool):
    """
    Locate supply orders filtered by optional supplier_id and/or status.

    Behavior:
    - If supplier_id is provided, only returns matching entries.
    - If status is provided, only returns entries with an exact match.
    - Returns a concise view: supply_order_id, supplier_id, status, items_count, created_at.

    Input (kwargs):
        supplier_id (str, optional)
        status (str, optional)

    Output:
        JSON string with {"count","supply_orders":[...]}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None, status: str = None) -> str:
        supply_orders = data.get("supply_orders", [])
        filtered = []
        for so in supply_orders:
            if supplier_id and so.get("supplier_id") != supplier_id:
                continue
            if status and so.get("status") != status:
                continue
            filtered.append(
                {
                    "supply_order_id": so.get("supply_order_id"),
                    "supplier_id": so.get("supplier_id"),
                    "status": so.get("status"),
                    "items_count": len(so.get("items", [])),
                    "created_at": so.get("created_at"),
                }
            )
        payload = {"count": len(filtered), "supply_orders": filtered}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindSupplyOrders",
                "description": "Find supply orders filtered by optional supplier_id and/or status from supply_orders.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                },
            },
        }
