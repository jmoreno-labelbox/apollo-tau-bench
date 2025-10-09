from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class SearchCustomerByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], first_name: str = None, last_name: str = None) -> str:
        customers = data.get("customers", [])
        results = []
        for customer in customers:
            pi = customer.get("personal_info", {})
            if pi.get("first_name", "").lower().strip() == first_name.lower().strip() and \
                    pi.get("last_name", "").lower().strip() == last_name.lower().strip():
                results.append(customer)
        return json.dumps(results)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "SearchCustomerByName",
                        "description": "Searches for a customer by their first and last name.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "first_name": {"type": "string", "description": "The customer's first name."},
                                        "last_name": {"type": "string", "description": "The customer's last name."}
                                },
                                "required": ["first_name", "last_name"],
                        },
                },
        }
