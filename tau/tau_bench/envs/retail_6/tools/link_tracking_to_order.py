# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _find_order(data, order_id):
    return next((o for o in data.get('orders', []) if o.get('order_id') == order_id), None)

def _ensure_list(dct, key):
    if key not in dct or not isinstance(dct[key], list):
        dct[key] = []
    return dct[key]

class LinkTrackingToOrder(Tool):
    """Add a fulfillment record linking tracking_id and item_ids to an order (idempotent by exact tuple)."""
    @staticmethod
    def invoke(data, order_id, tracking_id, item_ids = []) -> str:
        if not order_id or not tracking_id or not item_ids:
            return json.dumps({"error":"order_id, tracking_id, item_ids are required"}, indent=2)
        o = _find_order(data, order_id)
        if not o:
            return json.dumps({"error": f"order_id {order_id} not found"}, indent=2)
        fl = _ensure_list(o, 'fulfillments')
        payload = {"tracking_id":[tracking_id],"item_ids":item_ids}
        if payload not in fl:
            fl.append(payload)
        return json.dumps({"success": True, "order_id": order_id, "tracking_id": tracking_id, "item_ids": item_ids}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"link_tracking_to_order","description":"Append a fulfillment mapping (tracking_id, item_ids) to an order.","parameters":{"type":"object","properties":{"order_id":{"type":"string"},"tracking_id":{"type":"string"},"item_ids":{"type":"array","items":{"type":"string"}}},"required":["order_id","tracking_id","item_ids"]}}}