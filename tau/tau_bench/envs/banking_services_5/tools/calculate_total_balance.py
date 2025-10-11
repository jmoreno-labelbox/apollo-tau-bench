# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateTotalBalance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id, account_ids = []) -> str:
        if not customer_id or not isinstance(account_ids, list) or not account_ids:
            return json.dumps(
                {"error": "customer_id and a non-empty list of account_ids are required."},
                indent=2
            )

        customers = list(data.get("customers", {}).values())
        if not any(c.get("customer_id") == customer_id for c in customers):
            return json.dumps({"error": "Customer not found."}, indent=2)

        accounts = list(data.get("accounts", {}).values())
        total = 0.0
        for acc in accounts:
            if acc.get("account_id") in account_ids and acc.get("customer_id") == customer_id:

                total += acc.get("balance", 0.0)

        return json.dumps({"total_balance": total}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_total_balance",
                "description": "Calculates the sum of balances for the specified accounts of a given customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer whose accounts are to be summed"
                        },
                        "account_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of account IDs to include in the total"
                        }
                    },
                    "required": ["customer_id", "account_ids"]
                }
            }
        }
