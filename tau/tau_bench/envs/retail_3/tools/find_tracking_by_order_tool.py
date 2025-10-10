# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindTrackingByOrderTool(Tool):
    """Finds tracking data for an order from the shared in-memory state."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        order_id = kwargs.get("order_id")
        # Fetches the tracking information from the in-memory state.
        tracking_data = data.get("tracking", [])

        tr = next((t for t in tracking_data if t.get("order_id") == order_id), None)
        if not tr:
            return json.dumps(
                {"error": f"Tracking for order '{order_id}' not found in the current state"},
                indent=2,
            )

        # The 'item_ids' field will now update to show any prior modifications.
        return json.dumps(tr, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_tracking_by_order",
                "description": "Finds the tracking record for a given order_id from the current state.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }
