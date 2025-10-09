from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ApplyOfferToOrder(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str,
        offer_id: str,
        orders: list = None,
        offers: list = None
    ) -> str:
        order_id, offer_id = _sid(order_id), _sid(offer_id)
        orders = orders if orders is not None else data.get("orders", {}).values()
        offers = offers if offers is not None else data.get("offers", {}).values()
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        off = _active_offer(offers, offer_id)
        if not off:
            payload = {"error": "offer not active or not found"}
            out = json.dumps(payload, indent=2)
            return out
        order["applied_offer_id"] = offer_id
        payload = {"order_id": order_id, "applied_offer_id": offer_id}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "applyOfferToOrder",
                "description": "Apply an active offer to an order. (Does not recompute totals.)",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "offer_id": {"type": "string"},
                    },
                    "required": ["order_id", "offer_id"],
                },
            },
        }
