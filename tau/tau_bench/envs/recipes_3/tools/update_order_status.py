# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateOrderStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: int, new_status: str) -> str:
        row = _require(data, "orders", "order_id", int(order_id))
        if not row:
            return json.dumps({"error": f"order_id {order_id} not found"})
        row["status_enum"] = str(new_status)
        # Deterministic field to guarantee write behavior even when status remains the same.
        row["last_status_update_at"] = "2025-01-02T11:05:00"
        return json.dumps({"order": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_order_status",
                "description": "Update the status of an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "integer"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["order_id", "new_status"],
                },
            },
        }
