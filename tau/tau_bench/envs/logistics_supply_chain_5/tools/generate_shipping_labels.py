from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any, Dict



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GenerateShippingLabels(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, carrier_scac: str, outbound_orders: list = None, carriers: list = None) -> str:
        orders = outbound_orders if outbound_orders is not None else data.get("outbound_orders", [])
        carriers = carriers if carriers is not None else data.get("carriers", [])

        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"Order {order_id} not found"})

        carrier = next((c for c in carriers if c.get("scac") == carrier_scac), None)

        # UPDATED: Manage carriers mentioned in orders that are absent from carriers.json
        tracking = ""
        if not carrier:
            # Verify the presence of the carrier in order data (backup for data discrepancies)
            order_carrier = order.get("carrier_scac")
            if order_carrier == carrier_scac:
                carrier_name = order.get("carrier_name", f"Carrier {carrier_scac}")
                tracking = order.get("tracking_number", "")
            else:
                return json.dumps({"error": f"Carrier {carrier_scac} not found"})
        else:
            carrier_name = carrier.get("carrier_name")

        tracking_number = f"{carrier_scac}-{order_id}"
        if tracking:
            tracking_number = tracking

        shipping_label = {
            "label_id": f"LBL-{carrier_scac}",
            "order_id": order_id,
            "tracking_number": tracking_number,
            "carrier_scac": carrier_scac,
            "carrier_name": carrier_name,
            "generated_date": get_current_timestamp(),
            "destination_address": order.get("destination_address"),
            "weight_kg": order.get("total_weight_kg"),
            "service_level": order.get("shipping_service_level", "Standard"),
            "estimated_delivery_date": order.get("expected_delivery_date")
        }

        if "shipping_labels" not in data:
            data["shipping_labels"] = []
        data["shipping_labels"].append(shipping_label)

        return json.dumps({
            "tracking_number": tracking_number,
            "label_id": shipping_label["label_id"],
            "carrier_name": carrier_name,
            "estimated_delivery_date": shipping_label["estimated_delivery_date"]
        })
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateShippingLabels",
                "description": "Generate shipping labels and tracking numbers for an order",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "Order identifier"},
                        "carrier_scac": {"type": "string", "description": "Carrier SCAC code"}
                    },
                    "required": ["order_id", "carrier_scac"]
                }
            }
        }
