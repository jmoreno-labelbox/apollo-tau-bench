# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCustomerLoanApplications(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        applications = data.get("loan_applications", [])
        customer_loans = [app for app in applications if app.get("customer_id") == customer_id]
        return json.dumps(customer_loans)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_customer_loan_applications",
                        "description": "Retrieves all loan applications associated with a given customer ID.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string", "description": "The unique identifier for the customer."}
                                },
                                "required": ["customer_id"],
                        },
                },
        }
