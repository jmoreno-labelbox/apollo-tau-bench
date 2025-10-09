from tau_bench.envs.tool import Tool
import json
import random
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ShipOutboundOrder(Tool):
    """Modifies an order to 'Shipped', designates a carrier, distributes inventory, and computes shipping expenses."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, warehouse_id: str = None, carrier_scac: str = None) -> str:
        if not all([order_id, warehouse_id, carrier_scac]):
            payload = {"error": "order_id, warehouse_id, and carrier_scac are required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        order_to_update = next(
            (
                o
                for o in data.get("outbound_orders", {}).values()
                if o.get("order_id") == order_id
            ),
            None,
        )
        if not order_to_update:
            payload = {"error": f"Order '{order_id}' not found."}
            out = json.dumps(payload, indent=2)
            return out

        #--- NEW LOGIC INITIATION ---
        total_weight_kg = 0
        line_items = order_to_update.get("line_items", [])
        product_master = data.get("product_master", {}).values()
        for item in line_items:
            product = next(
                (p for p in product_master.values() if p.get("sku") == item["sku"]), None
            )
            if product:
                total_weight_kg += product.get("weight_kg", 0) * item["quantity"]

        #Predictable shipping cost assessment
        shipping_cost = round((total_weight_kg * 2.5) + 100, 2)
        order_to_update["shipping_cost"] = shipping_cost
        #--- NEW LOGIC CONCLUSION ---

        order_to_update["status"] = "Shipped"
        order_to_update["warehouse_id"] = warehouse_id
        carrier_name = next(
            (
                c.get("carrier_name")
                for c in data.get("carriers", {}).values()
                if c.get("scac") == carrier_scac
            ),
            "Unknown",
        )
        order_to_update["carrier_name"] = carrier_name
        order_to_update["carrier_scac"] = carrier_scac
        order_id_number = order_id.split("-")[1]
        order_to_update["tracking_number"] = f"{carrier_scac}-{order_id_number}"

        for item in line_items:
            for inv_record in data.get("inventory", {}).values():
                if (
                    inv_record.get("sku") == item.get("sku")
                    and inv_record.get("warehouse_id") == warehouse_id
                ):
                    inv_record["quantity_available"] -= item.get("quantity", 0)
                    inv_record["quantity_allocated"] += item.get("quantity", 0)
                    break
        payload = order_to_update
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ShipOutboundOrder",
                "description": "Updates an order's status to 'Shipped', adjusts inventory, and assigns a carrier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "warehouse_id": {"type": "string"},
                        "carrier_scac": {"type": "string"},
                    },
                    "required": ["order_id", "warehouse_id", "carrier_scac"],
                },
            },
        }
