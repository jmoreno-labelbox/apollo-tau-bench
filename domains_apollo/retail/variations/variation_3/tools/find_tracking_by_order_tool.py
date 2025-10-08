from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime
from typing import Any

class FindTrackingByOrderTool(Tool):
    """Locates tracking information for an order from the shared in-memory state."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None) -> str:
        # Retrieves the tracking information from the in-memory state.
        tracking_data = data.get("tracking", [])

        tr = next((t for t in tracking_data if t.get("order_id") == order_id), None)
        if not tr:
            payload = {
                "error": f"Tracking for order '{order_id}' not found in the current state"
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = tr
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindTrackingByOrder",
                "description": "Finds the tracking record for a given order_id from the current state.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }
