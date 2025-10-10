# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AppendTrackingEvent(Tool):
    """Insert/overwrite an event timestamp in tracking_history for a tracking id (key -> timestamp)."""
    @staticmethod
    def invoke(data, event, timestamp, tracking_id) -> str:
        if not tracking_id or not event or not timestamp:
            return json.dumps({"error":"tracking_id, event, timestamp are required"}, indent=2)
        t = _find_tracking(data, tracking_id)
        if not t:
            return json.dumps({"error": f"tracking_id {tracking_id} not found"}, indent=2)
        history = t.setdefault('tracking_history', {})
        history[event] = timestamp
        return json.dumps({"success": True, "tracking_id": tracking_id, "event": event, "timestamp": timestamp}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"append_tracking_event","description":"Set an event timestamp in tracking.tracking_history for a given tracking_id.","parameters":{"type":"object","properties":{"tracking_id":{"type":"string"},"event":{"type":"string"},"timestamp":{"type":"string"}},"required":["tracking_id","event","timestamp"]}}}
