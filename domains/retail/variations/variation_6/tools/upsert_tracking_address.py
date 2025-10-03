from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpsertTrackingAddress(Tool):
    """Modify the address in a tracking record."""

    @staticmethod
    def invoke(data, tracking_id=None, address=None) -> str:
        if not tracking_id or not isinstance(address, dict):
            payload = {"error": "tracking_id and address (object) are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        tr = _find_tracking(data, tracking_id)
        if not tr:
            payload = {"error": f"tracking_id {tracking_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        tr["address"] = address
        payload = {"success": True, "tracking_id": tracking_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "upsertTrackingAddress",
                "description": "Replace address on a tracking record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {"type": "string"},
                        "address": {"type": "object"},
                    },
                    "required": ["tracking_id", "address"],
                },
            },
        }
