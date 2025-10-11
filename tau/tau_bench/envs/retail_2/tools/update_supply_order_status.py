# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateSupplyOrderStatus(Tool):
    """Change status of a supply order deterministically."""

    @staticmethod
    def invoke(data: Dict[str, Any], supply_order_id: str, status: str) -> str:
        supply_orders = data.get("supply_orders", [])
        for so in supply_orders:
            if so.get("supply_order_id") == supply_order_id:
                so["status"] = status
                return json.dumps({"status": "success", "supply_order_id": supply_order_id, "new_status": status})
        return json.dumps({"error": "Supply order not found", "supply_order_id": supply_order_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_supply_order_status",
                "description": "Update the status field of a supply order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {"type": "string"},
                        "status": {"type": "string"}
                    },
                    "required": ["supply_order_id", "status"]
                }
            }
        }
