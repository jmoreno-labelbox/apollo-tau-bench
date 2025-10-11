# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _now_iso() -> str:
    """Return current UTC timestamp in ISO format (seconds precision)."""
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"

def _gen_order_id(seed: Optional[int] = None) -> str:
    """
    Generate a synthetic order identifier matching dataset flavor.

    Note: Collisions are unlikely but not impossible; this is OK for simulation.
    """
    base = seed if isinstance(seed, int) else int(datetime.utcnow().timestamp())
    return f"#W{base % 10_000_000:07d}"

class DuplicateOrderTool(Tool):
    """
    Duplicate an existing order into a new one for the same user.

    Behavior:
    - Validates the source order exists.
    - Clones user_id, address, items; resets fulfillments to [] and payment_history to [].
    - Sets status to "pending" and generates a new order_id and timestamp.
    - Appends the new order to orders.json.

    Input (kwargs):
        source_order_id (str, required)

    Output:
        JSON string with {"source_order_id","new_order_id","items_count"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], source_order_id) -> str:
        src_id = source_order_id
        if not src_id:
            return json.dumps({"error": "source_order_id is required"}, indent=2)

        orders = list(data.get("orders", {}).values())
        src = next((o for o in orders if o.get("order_id") == src_id), None)
        if not src:
            return json.dumps({"error": f"source_order_id '{src_id}' not found"}, indent=2)

        new_order = {
            "order_id": _gen_order_id(),
            "user_id": src.get("user_id"),
            "address": src.get("address"),
            "items": list(src.get("items", [])),
            "fulfillments": [],
            "status": "pending",
            "payment_history": [],
            "timestamp": _now_iso(),
        }
        orders.append(new_order)

        return json.dumps(
            {
                "source_order_id": src_id,
                "new_order_id": new_order["order_id"],
                "items_count": len(new_order.get("items", [])),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "duplicate_order",
                "description": "Duplicate an existing order (same user/address/items) with a fresh id, pending status, and no payments/fulfillments.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_order_id": {"type": "string"},
                    },
                    "required": ["source_order_id"],
                },
            },
        }