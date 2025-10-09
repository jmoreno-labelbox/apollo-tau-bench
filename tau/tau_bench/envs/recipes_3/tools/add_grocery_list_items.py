from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddGroceryListItems(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], list_id: int, items: list[dict[str, Any]]) -> str:
        table = _get_table(data, "grocery_list_items")
        next_id = _max_int(table, "item_id", 0)
        inserted = []
        for it in items or []:
            next_id += 1
            rec = {
                "item_id": next_id,
                "list_id": list_id,
                "ingredient_id": it["ingredient_id"],
                "quantity": it["quantity"],
                "unit": it["unit"],
                "grocery_section": it["grocery_section"],
                "pantry_staple_flag": bool(it["pantry_staple_flag"]),
                "overlap_last_month_flag": bool(it["overlap_last_month_flag"]),
            }
            table.append(rec)
            inserted.append(rec)
        payload = {"count": len(inserted)}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addGroceryListItems",
                "description": "Appends categorized items to a grocery list with deterministic item_ids.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {"type": "integer"},
                        "items": {"type": "array"},
                    },
                    "required": ["list_id", "items"],
                },
            },
        }
