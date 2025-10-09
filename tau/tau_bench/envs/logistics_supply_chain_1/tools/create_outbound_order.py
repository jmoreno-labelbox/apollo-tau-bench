from tau_bench.envs.tool import Tool
import json
import random
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateOutboundOrder(Tool):
    """A utility for generating a new outbound order within the system."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        customer_name: str = None,
        destination_city: str = None,
        priority_level: str = None,
        line_items: list[dict[str, Any]] = None
    ) -> str:
        if not all([customer_name, destination_city, priority_level, line_items]):
            payload = {
                "error": "customer_name, destination_city, priority_level, and line_items are required."
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        outbound_orders = data.get("outbound_orders", {}).values()
        max_id = max(
            (int(o.get("order_id", "ORD-0").split("-")[1]) for o in outbound_orders.values()),
            default=0,
        )
        new_order_id = f"ORD-{max_id + 1:04d}"
        customer_details = next(
            (o for o in outbound_orders.values() if o.get("customer_name") == customer_name), {}
        )
        new_order = {
            "order_id": new_order_id,
            "sales_order_number": f"SO-2025-{max_id + 1:04d}",
            "customer_id": customer_details.get("customer_id"),
            "customer_name": customer_name,
            "customer_address": customer_details.get("customer_address"),
            "customer_city": destination_city,
            "customer_country": customer_details.get("customer_country"),
            "destination_address": customer_details.get("customer_address"),
            "destination_city": destination_city,
            "destination_country": customer_details.get("customer_country"),
            "status": "Pending",
            "number_of_line_items": len(line_items),
            "total_units": sum(item.get("quantity", 0) for item in line_items.values()),
            "priority_level": priority_level,
            "line_items": line_items,
            "warehouse_id": None,
            "actual_ship_date": None,
            "carrier_name": None,
            "tracking_number": None,
        }
        outbound_data["orders"][order_id] = new_order
        payload = {"order_id": new_order_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateOutboundOrder",
                "description": "Creates a new outbound customer order with a 'Pending' status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_name": {"type": "string"},
                        "destination_city": {"type": "string"},
                        "priority_level": {"type": "string"},
                        "line_items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                },
                                "required": ["sku", "quantity"],
                            },
                        },
                    },
                    "required": [
                        "customer_name",
                        "destination_city",
                        "priority_level",
                        "line_items",
                    ],
                },
            },
        }
