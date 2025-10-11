# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindCustomersByCriteria(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], membership_levels = [], purchase_history_skus = []) -> str:

        customers = list(data.get("customers", {}).values())  # Ajustado para lista
        transactions = list(data.get("transactions", {}).values())  # Ajustado para lista

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

        return json.dumps(qualified_customers)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_customers_by_criteria",
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
