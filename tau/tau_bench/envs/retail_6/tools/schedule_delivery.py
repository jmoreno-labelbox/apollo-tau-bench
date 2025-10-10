# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ScheduleDelivery(Tool):
    """Set a 'scheduled' timestamp in tracking_history."""
    @staticmethod
    def invoke(data, scheduled, tracking_id) -> str:
        if not tracking_id or not scheduled:
            return json.dumps({"error":"tracking_id and scheduled (ISO string) are required"}, indent=2)
        tr = _find_tracking(data, tracking_id)
        if not tr:
            return json.dumps({"error": f"tracking_id {tracking_id} not found"}, indent=2)
        hist = tr.setdefault('tracking_history', {})
        hist['scheduled'] = scheduled
        return json.dumps({"success": True, "tracking_id": tracking_id, "scheduled": scheduled}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"schedule_delivery","description":"Set scheduled timestamp for a tracking record.","parameters":{"type":"object","properties":{"tracking_id":{"type":"string"},"scheduled":{"type":"string"}},"required":["tracking_id","scheduled"]}}}
