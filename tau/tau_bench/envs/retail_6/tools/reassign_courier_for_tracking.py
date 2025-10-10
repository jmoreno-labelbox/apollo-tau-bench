# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReassignCourierForTracking(Tool):
    """Change the delivery_carrier for an existing tracking record."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        tracking_id = kwargs.get('tracking_id')
        courier_id = kwargs.get('courier_id')
        if not tracking_id or not courier_id:
            return json.dumps({"error":"tracking_id and courier_id are required"}, indent=2)
        tr = _find_tracking(data, tracking_id)
        if not tr:
            return json.dumps({"error": f"tracking_id {tracking_id} not found"}, indent=2)
        tr['delivery_carrier'] = courier_id
        return json.dumps({"success": True, "tracking_id": tracking_id, "courier_id": courier_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"reassign_courier_for_tracking","description":"Update delivery_carrier for a tracking record.","parameters":{"type":"object","properties":{"tracking_id":{"type":"string"},"courier_id":{"type":"string"}},"required":["tracking_id","courier_id"]}}}
