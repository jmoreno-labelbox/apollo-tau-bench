# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListAccountTypesByCurrency(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], currency) -> str:
        account_types = []
        if currency == "GBP":
            account_types = ["Checking", "Savings", "ISA"]
        elif currency == "USD":
            account_types = ["Checking", "Savings", "Credit Card", "Investment"]
        elif currency == "EUR":
            account_types = ["Current Account", "Savings Account", "Credit"]

        return json.dumps({"currency": currency, "available_account_types": account_types})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "list_account_types_by_currency",
                        "description": "Lists the types of accounts available for a given currency.",
                        "parameters": {
                                "type": "object",
                                "properties": {"currency": {"type": "string", "description": "The three-letter currency code (e.g., GBP)."}},
                                "required": ["currency"]
                        }
                }
        }
