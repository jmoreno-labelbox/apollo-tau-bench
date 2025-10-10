# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindSupplyOrdersTool(Tool):
    """
    Find supply orders filtered by optional supplier_id and/or status.

    Behavior:
    - If supplier_id is provided, only returns matching records.
    - If status is provided, only returns records with exact status.
    - Returns a compact view: supply_order_id, supplier_id, status, items_count, created_at.

    Input (kwargs):
        supplier_id (str, optional)
        status (str, optional)

    Output:
        JSON string with {"count","supply_orders":[...]}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supplier_id = kwargs.get("supplier_id")
        status = kwargs.get("status")

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

        return json.dumps({"count": len(filtered), "supply_orders": filtered}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_supply_orders",
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
