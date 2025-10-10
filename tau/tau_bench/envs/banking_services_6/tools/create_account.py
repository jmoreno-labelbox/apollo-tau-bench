# Copyright by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAccount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = _get_next_account_id(data)
        customer_id = kwargs.get("customer_id")
        account_type = kwargs.get("account_type")
        currency = kwargs.get("currency")

        customer = next((c for c in data['customers'] if c['customer_id'] == customer_id), None)
        if not customer:
            return json.dumps({"error": "Customer not found"})

        new_account = {
                "account_id": account_id,
                "customer_id": customer_id,
                "account_type": account_type,
                "balance": 0.0,
                "currency": currency,
                "date_opened": NOW.strftime('%Y-%m-%d'),
                "status": "Active",
        }

        if account_type.lower() in ["checking", "current account"]:
            new_account["overdraft_limit"] = 100.00
        elif account_type.lower() == "savings":
            new_account["interest_rate"] = 1.05
        elif account_type.lower() == "credit card":
            new_account["credit_limit"] = 5000.00

        data['accounts'].append(new_account)
        customer['account_ids'].append(account_id)

        return json.dumps(new_account)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "create_account",
                        "description": "Creates a new bank account for a customer.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string"},
                                        "account_type": {"type": "string"},
                                        "currency": {"type": "string"}
                                },
                                "required": ["customer_id", "account_type", "currency"]
                        }
                }
        }
