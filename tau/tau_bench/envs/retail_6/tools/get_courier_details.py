# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _find_courier(data, courier_id):
    return next((c for c in data.get('couriers', []) if c.get('courier_id') == courier_id), None)

class GetCourierDetails(Tool):
    """Read courier record."""
    @staticmethod
    def invoke(data, courier_id) -> str:
        if not courier_id:
            return json.dumps({"error":"courier_id is required"}, indent=2)
        c = _find_courier(data, courier_id)
        return json.dumps(c or {"error": f"courier_id {courier_id} not found"}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"get_courier_details","description":"Fetch courier record by ID.","parameters":{"type":"object","properties":{"courier_id":{"type":"string"}},"required":["courier_id"]}}}