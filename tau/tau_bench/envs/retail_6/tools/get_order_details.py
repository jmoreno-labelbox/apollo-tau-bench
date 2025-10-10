# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOrderDetails(Tool):
    """Return an order by ID."""
    @staticmethod
    def invoke(data, order_id) -> str:
        if not order_id:
            return json.dumps({"error":"order_id is required"}, indent=2)
        order = _find_order(data, order_id)
        return json.dumps(order or {"error": f"order_id {order_id} not found"}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"get_order_details","description":"Fetch an order by ID.","parameters":{"type":"object","properties":{"order_id":{"type":"string"}},"required":["order_id"]}}}
