# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _tbl(db: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return db.setdefault(name, [])

def _max_id(rows: List[Dict[str, Any]], id_field: str, base: int) -> int:
    if not rows:
        return base
    vals: List[int] = []
    for r in rows:
        try:
            vals.append(int(r.get(id_field)))
        except Exception:
            pass
    return max(vals) if vals else base

class UpdateInventoryQuantity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int, ingredient_id: int, delta: float) -> str:
        tbl = _tbl(data, "inventory_items")
        row = next(
            (
                i
                for i in tbl
                if int(i.get("household_id")) == int(household_id)
                and int(i.get("ingredient_id")) == int(ingredient_id)
            ),
            None,
        )
        if row is None:
            next_id = _max_id(tbl, "inv_item_id", 7000) + 1
            qty = float(delta)
            row = {
                "inv_item_id": next_id,
                "household_id": int(household_id),
                "ingredient_id": int(ingredient_id),
                "quantity": qty,
            }
            tbl.append(row)
            return json.dumps({"inv_item_id": next_id, "quantity": qty})
        qty = float(row.get("quantity", 0)) + float(delta)
        row["quantity"] = qty
        return json.dumps({"inv_item_id": int(row.get("inv_item_id")), "quantity": qty})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_inventory_quantity",
                "description": "Apply delta to inventory; create if missing.",
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