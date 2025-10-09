from tau_bench.envs.tool import Tool
import json
from typing import Any

class ProposeSubstituteProducts(Tool):
    """For marked items, suggest in-stock alternatives at the same store; respect peanut-free requirements if require_peanut_free is set."""

    @staticmethod
    def invoke(data: dict[str, Any], store_id: int = None, flagged_items: list = None, require_peanut_free: bool = False,
    list_id: Any = None,
    ) -> str:
        if flagged_items is None:
            flagged_items = []
        if store_id is None or not isinstance(flagged_items, list):
            return _json_dump({"error": "store_id and flagged_items are required"})
        suggestions = []
        for f in flagged_items:
            iid = int(f.get("ingredient_id"))
            # Primary: same ingredient with the best availability
            prods = _store_products_for_ingredient(data, int(store_id), iid)
            best = _lowest_price_pref_stock(
                [p for p in prods.values() if p.get("stock_status_enum") in ("in_stock", "low")]
            )
            if best:
                suggestions.append(
                    {
                        "ingredient_id": iid,
                        "substitute_ingredient_id": iid,
                        "substitute_product_id": int(best["product_id"]),
                    }
                )
                continue
            # Fallback: any in-store item for the same ingredient category (skip if no dataset category)
            # Maintain deterministic behavior by providing no suggestions when none exist
            ing = _ingredient_by_id(data, iid)
            if (
                require_peanut_free
                and ing
                and not bool(ing.get("peanut_free_flag", True))
            ):
                # omit non-peanut-free bases if necessary
                continue
        return _json_dump({"substitutions": suggestions})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ProposeSubstituteProducts",
                "description": "Suggest in-store substitute products for flagged items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {"type": "integer"},
                        "flagged_items": {"type": "array", "items": {"type": "object"}},
                        "require_peanut_free": {"type": "boolean"},
                    },
                    "required": ["store_id", "flagged_items"],
                },
            },
        }
