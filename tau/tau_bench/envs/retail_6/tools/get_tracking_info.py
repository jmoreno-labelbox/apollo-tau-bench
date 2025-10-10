# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTrackingInfo(Tool):
    """Return tracking record by tracking_id."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        tracking_id = kwargs.get('tracking_id')
        if not tracking_id:
            return json.dumps({"error":"tracking_id is required"}, indent=2)
        t = _find_tracking(data, tracking_id)
        return json.dumps(t or {"error": f"tracking_id {tracking_id} not found"}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"get_tracking_info","description":"Get tracking record by tracking_id.","parameters":{"type":"object","properties":{"tracking_id":{"type":"string"}},"required":["tracking_id"]}}}
