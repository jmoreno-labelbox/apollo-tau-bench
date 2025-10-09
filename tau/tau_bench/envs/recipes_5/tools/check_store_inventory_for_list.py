from tau_bench.envs.tool import Tool
import json
from datetime import date, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CheckStoreInventoryForList(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], list_id: int = None, store_id: int = None) -> str:
        if store_id is None:
            store_id = _default_store_id(data)
        if list_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            list_id = _latest_list_id(data, household_id)
        if list_id is None or store_id is None:
            return _json_dump({"flagged_items": []})
        flagged = []
        for item in data.get("grocery_list_items", []):
            if item.get("list_id") != list_id:
                continue
            products = _store_products_for_ingredient(
                data, store_id, int(item["ingredient_id"])
            )
            best = _lowest_price_in_stock(products)
            if not best:
                flagged.append(
                    {
                        "ingredient_id": int(item["ingredient_id"]),
                        "status": "out_of_stock",
                    }
                )
            else:
                if best.get("stock_status_enum") == "low":
                    flagged.append(
                        {"ingredient_id": int(item["ingredient_id"]), "status": "low"}
                    )
        return _json_dump({"flagged_items": flagged})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckStoreInventoryForList",
                "description": "Flag low/out-of-stock items for a list and store; defaults to latest list and first store.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {"type": "integer"},
                        "store_id": {"type": "integer"},
                    },
                    "required": [],
                },
            },
        }
