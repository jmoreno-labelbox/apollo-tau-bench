from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ComputeUserFillRate(Tool):
    """Calculate a basic fill rate for a user's orders: delivered_items divided by total_items across all orders."""

    @staticmethod
    def invoke(data, user_id: str = None) -> str:
        if not user_id:
            payload = {"error": "user_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        user_orders = [o for o in data.get("orders", []) if o.get("user_id") == user_id]
        total = sum(len(o.get("items", [])) for o in user_orders)
        delivered = 0
        for o in user_orders:
            #tally items in fulfillments that tracking indicates as delivered
            for f in o.get("fulfillments", []):
                for tid in f.get("tracking_id", []):
                    tr = _find_tracking(data, tid)
                    if tr and tr.get("tracking_history", {}).get("delivered"):
                        delivered += len(f.get("item_ids", []))
        rate = (delivered / total) if total else 0.0
        payload = {"user_id": user_id, "fill_rate": round(rate, 4)}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "computeUserFillRate",
                "description": "Compute delivered item share across a user's orders.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
