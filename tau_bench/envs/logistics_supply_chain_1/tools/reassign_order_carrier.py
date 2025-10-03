from tau_bench.envs.tool import Tool
import json
import random
from typing import Any

class ReassignOrderCarrier(Tool):
    """Modifies the designated carrier for a particular outbound order."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, new_carrier_scac: str = None) -> str:
        if not all([order_id, new_carrier_scac]):
            payload = {"error": "order_id and new_carrier_scac are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        order = next(
            (
                o
                for o in data.get("outbound_orders", [])
                if o.get("order_id") == order_id
            ),
            None,
        )
        if not order:
            payload = {"error": f"Order '{order_id}' not found."}
            out = json.dumps(payload, indent=2)
            return out
        new_carrier = next(
            (c for c in data.get("carriers", []) if c.get("scac") == new_carrier_scac),
            None,
        )
        if not new_carrier:
            payload = {"error": f"New carrier with SCAC '{new_carrier_scac}' not found."}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        order["carrier_name"] = new_carrier.get("carrier_name")
        order["carrier_scac"] = new_carrier.get("scac")
        order_id_number = order_id.split("-")[1]
        order["tracking_number"] = f"{new_carrier.get('scac')}-{order_id_number}"
        payload = order
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReassignOrderCarrier",
                "description": "Changes the assigned carrier for a specific outbound order and generates a new tracking number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "new_carrier_scac": {"type": "string"},
                    },
                    "required": ["order_id", "new_carrier_scac"],
                },
            },
        }
