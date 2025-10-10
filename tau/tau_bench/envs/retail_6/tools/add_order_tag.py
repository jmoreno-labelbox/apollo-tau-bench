# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddOrderTag(Tool):
    """Add a tag string to an order (idempotent)."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        order_id = kwargs.get('order_id')
        tag = kwargs.get('tag')
        if not order_id or tag is None:
            return json.dumps({"error":"order_id and tag are required"}, indent=2)
        o = _find_order(data, order_id)
        if not o:
            return json.dumps({"error":f"order_id {order_id} not found"}, indent=2)
        tags = o.setdefault('order_tags', [])
        if tag not in tags:
            tags.append(tag)
        return json.dumps({"success": True, "order_id": order_id, "tag": tag}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"add_order_tag","description":"Append a tag to order.order_tags if not present.","parameters":{"type":"object","properties":{"order_id":{"type":"string"},"tag":{"type":"string"}},"required":["order_id","tag"]}}}
