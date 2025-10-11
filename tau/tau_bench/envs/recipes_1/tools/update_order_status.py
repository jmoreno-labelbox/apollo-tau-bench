# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require, _json_dump






def _require(data: Dict[str, Any], table: str, key: str, value: Any) -> Optional[Dict[str, Any]]:
    row = next((r for r in data.get(table, []) if r.get(key) == value), None)
    return row

def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

class UpdateOrderStatus(Tool):
    """Set orders.status_enum to a new value (e.g., 'placed', 'delivered')."""
    @staticmethod
    def invoke(data: Dict[str, Any], new_status, order_id) -> str:
        if order_id is None or not new_status:
            return _json_dump({"error": "order_id and new_status are required"})
        row = _require(data, "orders", "order_id", int(order_id))
        if not row:
            return _json_dump({"error": f"order_id {order_id} not found"})
        row["status_enum"] = str(new_status)
        return _json_dump(row)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_order_status",
            "description":"Update the status of an order.",
            "parameters":{"type":"object","properties":{
                "order_id":{"type":"integer"},
                "new_status":{"type":"string"}
            },"required":["order_id","new_status"]}
        }}