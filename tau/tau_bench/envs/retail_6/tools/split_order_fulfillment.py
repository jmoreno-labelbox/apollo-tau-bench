# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SplitOrderFulfillment(Tool):
    """Create a new tracking record and fulfillment for a subset of items, based on provided tracking_id and courier_id."""
    @staticmethod
    def invoke(data, address, courier_id, order_id, tracking_id, delivery_options = 'Standard', item_ids = []) -> str:
        if not order_id or not item_ids or not tracking_id or not courier_id:
            return json.dumps({"error":"order_id, item_ids, tracking_id, courier_id are required"}, indent=2)
        order = _find_order(data, order_id)
        if not order:
            return json.dumps({"error":f"order_id {order_id} not found"}, indent=2)
        # Generate or update tracking entry.
        tr_list = data.setdefault('tracking', [])
        tr = _find_tracking(data, tracking_id)
        if not tr:
            tr = {"tracking_id":[tracking_id], "item_ids": item_ids, "address": address or order.get('address'), "delivery_carrier": courier_id, "delivery_options": delivery_options, "order_id": order_id, "tracking_history": {}}
            tr_list.append(tr)
        else:
            tr['item_ids'] = item_ids
            tr['delivery_carrier'] = courier_id
            tr['delivery_options'] = delivery_options
            tr['order_id'] = order_id
            tr['address'] = address or order.get('address')
        # Connection to order completions
        fl = _ensure_list(order, 'fulfillments')
        payload = {"tracking_id":[tracking_id], "item_ids": item_ids}
        if payload not in fl:
            fl.append(payload)
        return json.dumps({"success": True, "order_id": order_id, "tracking_id": tracking_id, "courier_id": courier_id, "item_ids": item_ids}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"split_order_fulfillment","description":"Create a tracking record and link a subset of items to it.","parameters":{"type":"object","properties":{"order_id":{"type":"string"},"item_ids":{"type":"array","items":{"type":"string"}},"tracking_id":{"type":"string"},"courier_id":{"type":"string"},"delivery_options":{"type":"string"},"address":{"type":"object"}},"required":["order_id","item_ids","tracking_id","courier_id"]}}}
