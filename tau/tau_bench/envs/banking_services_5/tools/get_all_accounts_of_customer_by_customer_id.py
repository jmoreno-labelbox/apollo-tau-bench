from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone, date, timedelta
import calendar
from typing import Any, Dict
import random

class GetAllAccountsOfCustomerByCustomerId(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        if not customer_id:
            return json.dumps({"error": "customer_id is required."}, indent=2)

        customers = data.get("customers", [])
        for customer in customers:
            if customer.get("customer_id") == customer_id:
                return json.dumps({
                    "account_ids": customer.get("account_ids", [])
                }, indent=2)

        return json.dumps({"error": "Customer not found."}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllAccountsOfCustomerByCustomerId",
                "description": "Returns all account IDs associated with a given customer ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer"
                        }
                    },
                    "required": ["customer_id"]
                }
            }
        }
