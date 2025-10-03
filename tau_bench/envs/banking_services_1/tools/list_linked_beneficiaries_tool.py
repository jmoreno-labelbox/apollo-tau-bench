from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime, timedelta
from typing import Any, Dict

class ListLinkedBeneficiariesTool(Tool):
    """
    Tool to list all beneficiaries linked to a specific customer.

    This tool gathers the beneficiary records registered under the customer's ID
    and returns structured data such as name, relationship, and account details.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Lists all beneficiaries for the provided customer ID.

        get_info() -> Dict[str, Any]:
            Describes usage schema and return structure.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        if not customer_id:
            return json.dumps({"error": "customer_id is required"}, indent=2)
        beneficiaries = load_json("beneficiaries.json")
        linked = [b for b in beneficiaries if b["customer_id"] == customer_id]
        return json.dumps({"beneficiaries": linked}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListLinkedBeneficiaries",
                "description": "Retrieve all beneficiaries linked to the customer's account.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer ID"}
                    },
                    "required": ["customer_id"],
                },
            },
        }
