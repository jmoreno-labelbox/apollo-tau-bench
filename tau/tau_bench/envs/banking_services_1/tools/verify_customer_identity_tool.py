from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime, timedelta
from typing import Any, Dict

class VerifyCustomerIdentityTool(Tool):
    """
    Tool to verify a customer's identity based on their official ID document.

    This tool confirms whether the given document corresponds to a known customer
    based on the customer_id and document number.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Validates customer identity and returns a structured result.

        get_info() -> Dict[str, Any]:
            Returns metadata about the expected input parameters and verification logic.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, id_document: str = None) -> str:
        if not customer_id or not id_document:
            return json.dumps(
                {
                    "status": "error",
                    "message": "Missing required parameters: 'customer_id' and/or 'id_document'.",
                    "required": ["customer_id", "id_document"],
                },
                indent=2,
            )

        customers = load_json("customers_documents.json")
        customer = next((c for c in customers.values() if c["customer_id"] == customer_id), None)

        if not customer:
            return json.dumps(
                {"status": "fail", "verified": False, "reason": "Customer not found"},
                indent=2,
            )

        # Simulate document verification logic
        return json.dumps(
            {"status": "success", "verified": True, "confidence": 0.97}, indent=2
        )
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "VerifyCustomerIdentity",
                "description": "Verify a customer's identity using a valid official document (e.g., passport, national ID, or license).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique identifier of the customer in the database.",
                        },
                        "id_document": {
                            "type": "string",
                            "description": "A valid official document number, e.g., passport, driver's license, national ID.",
                        },
                    },
                    "required": ["customer_id", "id_document"],
                },
            },
        }
