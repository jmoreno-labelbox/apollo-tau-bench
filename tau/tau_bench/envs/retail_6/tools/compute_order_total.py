# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _find_order(data, order_id):
    return next((o for o in data.get('orders', []) if o.get('order_id') == order_id), None)

class ComputeOrderTotal(Tool):
    """Compute the sum of item prices for an order (ignores refunds/payments)."""
    @staticmethod
    def invoke(data, order_id) -> str:
        if not order_id:
            return json.dumps({"error":"order_id is required"}, indent=2)
        o = _find_order(data, order_id)
        if not o:
            return json.dumps({"error":f"order_id {order_id} not found"}, indent=2)
        total = sum(i.get('price', 0) for i in o.get('items', []))
        return json.dumps({"order_id": order_id, "computed_total": round(float(total),2)}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"compute_order_total","description":"Return computed sum of item prices for an order.","parameters":{"type":"object","properties":{"order_id":{"type":"string"}},"required":["order_id"]}}}