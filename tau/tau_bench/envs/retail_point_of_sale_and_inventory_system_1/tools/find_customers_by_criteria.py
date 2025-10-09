from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FindCustomersByCriteria(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], membership_levels: list = None, purchase_history_skus: list = None) -> str:
        if membership_levels is None:
            membership_levels = []
        if purchase_history_skus is None:
            purchase_history_skus = []

        customers = data.get("customers", [])
        transactions = data.get("transactions", [])

        qualified_customers = []

        for customer in customers:
            if customer.get("membership_level") in membership_levels:
                customer_id = customer.get("customer_id")
                for txn in transactions:
                    if txn.get("customer_id") == customer_id:
                        for item in txn.get("line_items", []):
                            if item.get("sku") in purchase_history_skus:
                                qualified_customers.append(customer)
                                break
                        break
        payload = qualified_customers
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCustomersByCriteria",
                "description": "Finds customers based on multiple criteria like membership level and purchase history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "membership_levels": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of membership levels to filter by (e.g., ['gold', 'platinum']).",
                        },
                        "purchase_history_skus": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of product SKUs to check for in the customers' purchase history.",
                        },
                    },
                    "required": ["membership_levels"],
                },
            },
        }
