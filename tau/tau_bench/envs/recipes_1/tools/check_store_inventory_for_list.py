from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CheckStoreInventoryForList(Tool):
    """Mark low/out_of_stock items for a list at a specific store; include the best in-store option if it exists."""

    @staticmethod
    def invoke(data: dict[str, Any], list_id: int = None, store_id: int = None) -> str:
        if list_id is None or store_id is None:
            return _json_dump({"error": "list_id and store_id are required"})
        gl_items = [
            i
            for i in data.get("grocery_list_items", [])
            if int(i.get("list_id")) == int(list_id)
        ]
        results = []
        for it in gl_items:
            iid = int(it["ingredient_id"])
            prods = _store_products_for_ingredient(data, int(store_id), iid)
            best = _lowest_price_pref_stock(prods)
            status = best.get("stock_status_enum") if best else "out_of_catalog"
            results.append(
                {
                    "item_id": int(it["item_id"]),
                    "ingredient_id": iid,
                    "matched_product_id": int(best["product_id"]) if best else None,
                    "stock_status_enum": status,
                    "price_cents": int(best.get("price_cents", 0)) if best else None,
                }
            )
        return _json_dump({"store_check": results})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckStoreInventoryForList",
                "description": "Check availability for each list item at a store and return best options.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {"type": "integer"},
                        "store_id": {"type": "integer"},
                    },
                    "required": ["list_id", "store_id"],
                },
            },
        }
