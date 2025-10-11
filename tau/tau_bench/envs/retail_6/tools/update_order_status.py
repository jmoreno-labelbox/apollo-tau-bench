# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _find_order(data, order_id):
    return next((o for o in data.get('orders', []) if o.get('order_id') == order_id), None)

class UpdateOrderStatus(Tool):
    """Set order status to provided value."""
    @staticmethod
    def invoke(data, order_id, status) -> str:
        if not order_id or status is None:
            return json.dumps({"error":"order_id and status are required"}, indent=2)
        o = _find_order(data, order_id)
        if not o:
            return json.dumps({"error":f"order_id {order_id} not found"}, indent=2)
        o['status'] = status
        return json.dumps({"success": True, "order_id": order_id, "status": status}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"update_order_status","description":"Update the status field on an order.","parameters":{"type":"object","properties":{"order_id":{"type":"string"},"status":{"type":"string"}},"required":["order_id","status"]}}}