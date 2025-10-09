from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetTrackingHistory(Tool):
    """Obtain the tracking history for a specified order_id from tracking.json entries."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str) -> str:
        tracking_records = data.get("tracking", {}).values()
        # Entries in tracking.json are expected to include: order_id, tracking_history, tracking_id[], address, etc.
        for rec in tracking_records:
            if rec.get("order_id") == order_id:
                payload = {
                    "order_id": order_id,
                    "tracking_id": rec.get("tracking_id"),
                    "delivery_carrier": rec.get("delivery_carrier"),
                    "tracking_history": list(rec.get("tracking_history", {}).values()),
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Tracking record not found", "order_id": order_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTrackingHistory",
                "description": "Get tracking history for an order from tracking.json.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }
