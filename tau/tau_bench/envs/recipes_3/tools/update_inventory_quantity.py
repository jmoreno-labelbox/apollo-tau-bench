from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateInventoryQuantity(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], household_id: int, ingredient_id: int, delta: float
    ) -> str:
        inv = _get_table(data, "inventory_items")
        row = next(
            (
                x
                for x in inv
                if x.get("household_id") == household_id
                and x.get("ingredient_id") == ingredient_id
            ),
            None,
        )
        if not row:
            row = {
                "inv_item_id": _max_int(inv, "inv_item_id", 0) + 1,
                "household_id": household_id,
                "ingredient_id": ingredient_id,
                "quantity": 0,
                "unit": None,
                "location_enum": None,
                "best_by_date": None,
            }
            inv.append(row)
        q = float(row.get("quantity") or 0)
        q = max(0.0, q + float(delta))
        row["quantity"] = q
        payload = {"ingredient_id": ingredient_id, "quantity": q}
        out = json.dumps(payload, indent=2)
        return out
        pass
        inv = _get_table(data, "inventory_items")
        row = next(
            (
                x
                for x in inv
                if x.get("household_id") == household_id
                and x.get("ingredient_id") == ingredient_id
            ),
            None,
        )
        if not row:
            row = {
                "inv_item_id": _max_int(inv, "inv_item_id", 0) + 1,
                "household_id": household_id,
                "ingredient_id": ingredient_id,
                "quantity": 0,
                "unit": None,
                "location_enum": None,
                "best_by_date": None,
            }
            inv.append(row)
        q = float(row.get("quantity") or 0)
        q = max(0.0, q + float(delta))
        row["quantity"] = q
        payload = {"ingredient_id": ingredient_id, "quantity": q}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateInventoryQuantity",
                "description": "Adjusts inventory quantity by delta with floor at zero.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "ingredient_id": {"type": "integer"},
                        "delta": {"type": "number"},
                    },
                    "required": ["household_id", "ingredient_id", "delta"],
                },
            },
        }
