# Copyright Sierra

from typing import Tuple
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _max_id, _json_dump














def _sum_grocery_items(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    # Sum quantities per (ingredient_id, unit)
    agg: Dict[Tuple[int, str], float] = {}
    for r in rows:
        iid = int(r["ingredient_id"])
        unit = str(r.get("unit"))
        qty = float(r.get("quantity", 0))
        agg[(iid, unit)] = agg.get((iid, unit), 0.0) + qty
    out = []
    for (iid, unit), qty in agg.items():
        out.append({"ingredient_id": iid, "quantity": qty, "unit": unit})
    return out

def _parse_json_list_ids(json_str: str) -> List[int]:
    try:
        arr = json.loads(json_str)
        if isinstance(arr, list):
            return [int(x) for x in arr]
    except Exception:
        pass
    return []

def _max_id(records: List[Dict[str, Any]], key: str, default: int) -> int:
    if not records:
        return default
    vals = []
    for r in records:
        try:
            vals.append(int(r.get(key)))
        except Exception:
            pass
    return max(vals) if vals else default

def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

def _ingredient_by_id(data: Dict[str, Any], ingredient_id: int) -> Optional[Dict[str, Any]]:
    return next((i for i in data.get("ingredients", []) if int(i.get("ingredient_id")) == ingredient_id), None)

def _collect_recipe_ingredients(data: Dict[str, Any], recipe_ids: List[int]) -> List[Dict[str, Any]]:
    ri = data.get("recipe_ingredients", [])
    ridset = set(recipe_ids)
    return [row for row in ri if int(row.get("recipe_id")) in ridset]

class UpsertGroceryListItemsFromRecipes(Tool):
    """Replace all items for list_id with the aggregated ingredients from recipe_ids_json."""
    @staticmethod
    def invoke(data: Dict[str, Any], list_id, recipe_ids_json = "[]") -> str:
        if list_id is None:
            return _json_dump({"error": "list_id is required"})
        recipe_ids = _parse_json_list_ids(recipe_ids_json)
        ri = _collect_recipe_ingredients(data, recipe_ids)
        items = _sum_grocery_items(ri)

        # eliminate outdated
        gli_tbl = data.setdefault("grocery_list_items", [])
        gli_tbl[:] = [r for r in gli_tbl if int(r.get("list_id")) != int(list_id)]

        # add new
        next_id = _max_id(gli_tbl, "item_id", 8100)
        created_ids: List[int] = []
        for it in items:
            next_id += 1
            ing = _ingredient_by_id(data, int(it["ingredient_id"]))
            row = {
                "item_id": next_id,
                "list_id": int(list_id),
                "ingredient_id": int(it["ingredient_id"]),
                "quantity": float(it["quantity"]),
                "unit": str(it["unit"]),
                "grocery_section": (ing or {}).get("grocery_section", "Misc"),
                "pantry_staple_flag": bool((ing or {}).get("pantry_staple_flag", False)),
                "overlap_last_month_flag": False
            }
            gli_tbl.append(row)
            created_ids.append(next_id)
        return _json_dump({"created_item_ids": created_ids})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"upsert_grocery_list_items_from_recipes",
            "description":"Replace list items with aggregation from the provided recipe_ids.",
            "parameters":{"type":"object","properties":{
                "list_id":{"type":"integer"},
                "recipe_ids_json":{"type":"string"}
            },"required":["list_id","recipe_ids_json"]}
        }}