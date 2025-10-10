# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateSupplyOrderStatus(Tool):
    """Set status on a supply order."""
    @staticmethod
    def invoke(data, status, supply_order_id) -> str:
        if not supply_order_id or not status:
            return json.dumps({"error":"supply_order_id and status are required"}, indent=2)
        so = next((s for s in data.get('supply_orders', []) if s.get('supply_order_id') == supply_order_id), None)
        if not so:
            return json.dumps({"error": f"supply_order_id {supply_order_id} not found"}, indent=2)
        so['status'] = status
        return json.dumps({"success": True, "supply_order_id": supply_order_id, "status": status}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"update_supply_order_status","description":"Update a supply order's status.","parameters":{"type":"object","properties":{"supply_order_id":{"type":"string"},"status":{"type":"string"}},"required":["supply_order_id","status"]}}}
