from tau_bench.envs.tool import Tool
import json
from typing import Any

class FindCourierByTrackingId(Tool):
    """Determine the courier associated with a tracking ID."""

    @staticmethod
    def invoke(data: dict[str, Any], tracking_id: str) -> str:
        couriers = data.get("couriers", [])
        for c in couriers:
            if tracking_id in c.get("tracking_ids", []):
                payload = {
                    "tracking_id": tracking_id,
                    "courier_id": c.get("courier_id"),
                    "name": c.get("name"),
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Courier not found for tracking ID", "tracking_id": tracking_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCourierByTrackingId",
                "description": "Find the courier that owns a given tracking ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"tracking_id": {"type": "string"}},
                    "required": ["tracking_id"],
                },
            },
        }
