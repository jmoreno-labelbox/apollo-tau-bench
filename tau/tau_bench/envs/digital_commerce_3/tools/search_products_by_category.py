from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SearchProductsByCategory(Tool):
    """Look for items in a designated category and provide pricing details."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        category_name: Any = None,
        category_id: Any = None,
        account_id: Any = None,
        categories: list = None,
        products: list = None,
        accounts: list = None,
        pricebook_entries: list = None
    ) -> str:
        pass
        cat_id = _idstr(category_id) if category_id is not None else None
        cat_name = f"{category_name}".strip() if category_name is not None else None
        account_id = _idstr(account_id) if account_id is not None else None

        if not cat_id and not cat_name:
            return _error("category_id or category_name is required.")

        categories = categories or data.get("categories", {}).values()
        category = None
        if cat_id:
            category = _find_one(list(categories.values()), "category_id", cat_id)
        elif cat_name:
            category = _find_one(list(categories.values()), "category_name", cat_name)

        if not category:
            return _error(f"Category '{cat_id or cat_name}' not found.")

        products = products or data.get("products", {}).values()
        resolved_cid = f"{category.get('category_id')}"
        category_products = [
            p for p in products.values() if f"{p.get('category_id')}" == resolved_cid
        ]

        if account_id:
            accounts = accounts or data.get("accounts", {}).values()
            account = _find_one(list(accounts.values()), "account_id", account_id)
            if account:
                pricebook_id = _idstr(account.get("default_pricebook_id"))
                pricebook_entries = pricebook_entries or data.get("pricebook_entries", {}).values()
                for product in category_products:
                    pbe = _find_one(
                        pricebook_entries, "product_id", product.get("product_id")
                    )
                    if pbe and f"{pbe.get('pricebook_id')}" == f"{pricebook_id}":
                        product["price"] = pbe.get("price")
        payload = category_products
        out = json.dumps(payload, indent=2)
        return out
        pass
        cat_id = _idstr(category_id) if category_id is not None else None
        cat_name = f"{category_name}".strip() if category_name is not None else None
        account_id = _idstr(account_id) if account_id is not None else None

        if not cat_id and not cat_name:
            return _error("category_id or category_name is required.")

        categories = data.get("categories", {}).values()
        category = None
        if cat_id:
            category = _find_one(list(categories.values()), "category_id", cat_id)
        elif cat_name:
            category = _find_one(list(categories.values()), "category_name", cat_name)

        if not category:
            return _error(f"Category '{cat_id or cat_name}' not found.")

        products = data.get("products", {}).values()
        resolved_cid = f"{category.get('category_id')}"
        category_products = [
            p for p in products.values() if f"{p.get('category_id')}" == resolved_cid
        ]

        if account_id:
            accounts = data.get("accounts", {}).values()
            account = _find_one(list(accounts.values()), "account_id", account_id)
            if account:
                pricebook_id = _idstr(account.get("default_pricebook_id"))
                pricebook_entries = data.get("pricebook_entries", {}).values()
                for product in category_products:
                    pbe = _find_one(
                        pricebook_entries, "product_id", product.get("product_id")
                    )
                    if pbe and f"{pbe.get('pricebook_id')}" == f"{pricebook_id}":
                        product["price"] = pbe.get("price")
        payload = category_products
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchProductsByCategory",
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
