from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone, date, timedelta
import calendar
from typing import Any, Dict
import random

class GetAccountTypeAndAccountTypeCode(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], account_type: str = "") -> str:
        account_type_input = account_type.strip().lower()

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
            standardized_type = account_type_input.title()  # e.g., "savings" → "Savings"
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
                "name": "GetAccountTypeAndAccountTypeCode",
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
