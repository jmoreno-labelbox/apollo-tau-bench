# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateItemOption(Tool):
    """Update a specific option key for a given item in an order."""
    @staticmethod
    def invoke(data, item_id, option_key, option_value, order_id) -> str:
        if not order_id or not item_id or option_key is None or option_value is None:
            return json.dumps({"error":"order_id, item_id, option_key, option_value are required"}, indent=2)
        o = _find_order(data, order_id)
        if not o:
            return json.dumps({"error":f"order_id {order_id} not found"}, indent=2)
        it = next((i for i in o.get('items', []) if i.get('item_id') == item_id), None)
        if not it:
            return json.dumps({"error":f"item_id {item_id} not in order {order_id}"}, indent=2)
        opts = it.setdefault('options', {})
        opts[option_key] = option_value
        return json.dumps({"success": True, "order_id": order_id, "item_id": item_id, "option_key": option_key, "option_value": option_value}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"update_item_option","description":"Update a single option on an order item.","parameters":{"type":"object","properties":{"order_id":{"type":"string"},"item_id":{"type":"string"},"option_key":{"type":"string"},"option_value":{}},"required":["order_id","item_id","option_key","option_value"]}}}
