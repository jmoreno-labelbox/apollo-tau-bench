# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _first_user_id


class UpdateOrderStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id, new_status = "placed") -> str:
        if order_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            order_id = _latest_order_id(data, household_id)
        order = next((o for o in list(data.get("orders", {}).values()) if o.get("order_id") == order_id), None)
        if not order:
            return _json_dump({"error": "no order available"})
        order["status_enum"] = str(new_status)
        return _json_dump(order)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"update_order_status","description":"Update order status; defaults to latest order and status 'placed'.","parameters":{"type":"object","properties":{"order_id":{"type":"integer"},"new_status":{"type":"string"}},"required":[]}}}
