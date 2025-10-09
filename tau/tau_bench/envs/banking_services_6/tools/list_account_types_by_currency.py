from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class ListAccountTypesByCurrency(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], currency: str = None) -> str:
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
                        "name": "ListAccountTypesByCurrency",
                        "description": "Lists the types of accounts available for a given currency.",
                        "parameters": {
                                "type": "object",
                                "properties": {"currency": {"type": "string", "description": "The three-letter currency code (e.g., GBP)."}},
                                "required": ["currency"]
                        }
                }
        }
