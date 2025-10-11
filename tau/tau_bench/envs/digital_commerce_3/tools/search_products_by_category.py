# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _find_one


class SearchProductsByCategory(Tool):
    """Search for products within a specific category and return pricing information."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        category_name: Any = None,
        category_id: Any = None,
        account_id: Any = None,
    ) -> str:
        cat_id = _idstr(category_id) if category_id is not None else None
        cat_name = f"{category_name}".strip() if category_name is not None else None
        account_id = _idstr(account_id) if account_id is not None else None

        if not cat_id and not cat_name:
            return _error("category_id or category_name is required.")

        categories = data.get("categories", [])
        category = None
        if cat_id:
            category = _find_one(categories, "category_id", cat_id)
        elif cat_name:
            category = _find_one(categories, "category_name", cat_name)

        if not category:
            return _error(f"Category '{cat_id or cat_name}' not found.")

        products = list(data.get("products", {}).values())
        resolved_cid = f"{category.get('category_id')}"
        category_products = [p for p in products if f"{p.get('category_id')}" == resolved_cid]

        if account_id:
            accounts = list(data.get("accounts", {}).values())
            account = _find_one(accounts, "account_id", account_id)
            if account:
                pricebook_id = _idstr(account.get("default_pricebook_id"))
                pricebook_entries = data.get("pricebook_entries", [])
                for product in category_products:
                    pbe = _find_one(pricebook_entries, "product_id", product.get("product_id"))
                    if pbe and f"{pbe.get('pricebook_id')}" == f"{pricebook_id}":
                        product["price"] = pbe.get("price")

        return json.dumps(category_products, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_products_by_category",
                "description": "Search for products within a specific category and optionally include pricing for an account.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category_name": {"type": "string"},
                        "category_id": {"type": "string"},
                        "account_id": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
