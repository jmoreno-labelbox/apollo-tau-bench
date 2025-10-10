# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindCourierByTrackingId(Tool):
    """Identify courier from a tracking ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], tracking_id: str) -> str:
        couriers = data.get("couriers", [])
        for c in couriers:
            if tracking_id in c.get("tracking_ids", []):
                return json.dumps({"tracking_id": tracking_id, "courier_id": c.get("courier_id"), "name": c.get("name")})
        return json.dumps({"error": "Courier not found for tracking ID", "tracking_id": tracking_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_courier_by_tracking_id",
                "description": "Find the courier that owns a given tracking ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {"type": "string"}
                    },
                    "required": ["tracking_id"]
                }
            }
        }
