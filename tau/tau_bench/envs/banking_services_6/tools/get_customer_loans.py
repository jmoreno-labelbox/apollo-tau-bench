from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class GetCustomerLoans(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        loans = data.get("loans", [])
        customer_loans = [loan for loan in loans if loan.get("customer_id") == customer_id]
        return json.dumps(customer_loans)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetCustomerLoans",
                        "description": "Retrieves all loans associated with a given customer ID.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string", "description": "The unique identifier for the customer."}
                                },
                                "required": ["customer_id"],
                        },
                },
        }
