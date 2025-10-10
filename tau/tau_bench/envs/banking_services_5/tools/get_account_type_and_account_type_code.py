# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAccountTypeAndAccountTypeCode(Tool):
    """Returns both standardized account type and its 3-letter code."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_type_input = kwargs.get("account_type", "").strip().lower()

        if not account_type_input:
            return json.dumps({"error": "account_type is required."}, indent=2)

        type_map = {
            "checking": "chk",
            "savings": "sav",
            "credit card": "crd",
            "loan": "loan",
            "investment": "inv"
        }

        account_code = type_map.get(account_type_input)
        if account_code:
            standardized_type = account_type_input.title()  # For instance, "savings" becomes "Savings".
            return json.dumps({
                "account_type": standardized_type,
                "account_code": account_code
            }, indent=2)
        else:
            return json.dumps({
                "error": f"Unknown account type: {account_type_input}"
            }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_account_type_and_account_type_code",
                "description": (
                    "Returns both the standardized account type and its 3-letter account code. "
                    "Acceptable input values: 'Checking', 'Savings', 'Credit Card', 'Loan', 'Investment'."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_type": {
                            "type": "string",
                            "description": (
                                "Human-readable account type. Acceptable values: "
                                "'Checking', 'Savings', 'Credit Card', 'Loan', 'Investment'."
                            )
                        }
                    },
                    "required": ["account_type"]
                }
            }
        }
