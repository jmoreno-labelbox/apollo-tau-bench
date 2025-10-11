# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CancelOrderItems(Tool):
    """Mark specific items in an order as cancelled with a reason_code (adds 'cancelled': True)."""
    @staticmethod
    def invoke(data, order_id, reason_code, item_ids = []) -> str:
        if not order_id or not item_ids or not reason_code:
            return json.dumps({"error":"order_id, item_ids, reason_code are required"}, indent=2)
        o = _find_order(data, order_id)
        if not o:
            return json.dumps({"error":f"order_id {order_id} not found"}, indent=2)
        updated = []
        for item in o.get('items', []):
            if item.get('item_id') in item_ids:
                item['cancelled'] = True
                item['cancellation_reason'] = reason_code
                updated.append(item['item_id'])
        return json.dumps({"success": True, "order_id": order_id, "cancelled_item_ids": updated, "reason_code": reason_code}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"cancel_order_items","description":"Mark given item_ids in an order as cancelled with a reason_code.","parameters":{"type":"object","properties":{"order_id":{"type":"string"},"item_ids":{"type":"array","items":{"type":"string"}},"reason_code":{"type":"string"}},"required":["order_id","item_ids","reason_code"]}}}
