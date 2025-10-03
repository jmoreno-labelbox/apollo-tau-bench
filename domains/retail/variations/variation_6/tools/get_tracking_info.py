from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetTrackingInfo(Tool):
    """Fetch tracking record using tracking_id."""

    @staticmethod
    def invoke(data, tracking_id=None) -> str:
        if not tracking_id:
            payload = {"error": "tracking_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        t = _find_tracking(data, tracking_id)
        payload = t or {"error": f"tracking_id {tracking_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "getTrackingInfo",
                "description": "Get tracking record by tracking_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"tracking_id": {"type": "string"}},
                    "required": ["tracking_id"],
                },
            },
        }
