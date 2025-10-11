# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _find_tracking(data, tracking_id):
    return next((t for t in data.get('tracking', []) if tracking_id in t.get('tracking_id', [])), None)

class UpsertTrackingAddress(Tool):
    """Update the address on a tracking record."""
    @staticmethod
    def invoke(data, address, tracking_id) -> str:
        if not tracking_id or not isinstance(address, dict):
            return json.dumps({"error":"tracking_id and address (object) are required"}, indent=2)
        tr = _find_tracking(data, tracking_id)
        if not tr:
            return json.dumps({"error": f"tracking_id {tracking_id} not found"}, indent=2)
        tr['address'] = address
        return json.dumps({"success": True, "tracking_id": tracking_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"upsert_tracking_address","description":"Replace address on a tracking record.","parameters":{"type":"object","properties":{"tracking_id":{"type":"string"},"address":{"type":"object"}},"required":["tracking_id","address"]}}}