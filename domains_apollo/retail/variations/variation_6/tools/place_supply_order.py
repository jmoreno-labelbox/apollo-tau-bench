from tau_bench.envs.tool import Tool
import json
from typing import Any

class PlaceSupplyOrder(Tool):
    """Establish or modify a supply order using the given supply_order_id."""

    @staticmethod
    def invoke(
        data,
        supply_order_id: str = None,
        supplier_id: str = None,
        product_id: str = None,
        item_id: str = None,
        quantity: int = None,
        unit_cost: float = None,
        status: str = "pending"
    ) -> str:
        if (
            not all([supply_order_id, supplier_id, product_id, item_id])
            or quantity is None
            or unit_cost is None
        ):
            payload = {
                "error": "supply_order_id, supplier_id, product_id, item_id, quantity, unit_cost are required"
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        so_list = data.setdefault("supply_orders", [])
        existing = next(
            (s for s in so_list if s.get("supply_order_id") == supply_order_id), None
        )
        record = {
            "supply_order_id": supply_order_id,
            "supplier_id": supplier_id,
            "product_id": product_id,
            "item_id": item_id,
            "quantity": int(quantity),
            "status": status,
            "order_date": "2025-01-01T00:00:00",
            "unit_cost": float(unit_cost),
            "total_cost": round(float(unit_cost) * int(quantity), 2),
        }
        if existing:
            existing.update(record)
        else:
            so_list.append(record)
        payload = {"success": True, "supply_order_id": supply_order_id}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "placeSupplyOrder",
                "description": "Create or overwrite a supply order by supply_order_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {"type": "string"},
                        "supplier_id": {"type": "string"},
                        "product_id": {"type": "string"},
                        "item_id": {"type": "string"},
                        "quantity": {"type": "integer"},
                        "unit_cost": {"type": "number"},
                        "status": {"type": "string"},
                    },
                    "required": [
                        "supply_order_id",
                        "supplier_id",
                        "product_id",
                        "item_id",
                        "quantity",
                        "unit_cost",
                    ],
                },
            },
        }
