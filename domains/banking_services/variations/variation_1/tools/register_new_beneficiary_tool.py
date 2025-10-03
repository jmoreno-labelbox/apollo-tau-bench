from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime, timedelta
from typing import Any, Dict

class RegisterNewBeneficiaryTool(Tool):
    """
    Tool to add a new beneficiary to a customer's profile.

    This tool generates a unique beneficiary ID and associates the new entry
    with the customer, including details such as bank information and country.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Adds the beneficiary and returns the new ID and status.

        get_info() -> Dict[str, Any]:
            Returns parameter schema and functional metadata for tool registration.
    """

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        customer_id: str = None,
        beneficiary_name: str = None,
        country: str = None,
        bank_details: dict = None,
        beneficiary_id: str = None,
        beneficiary_type: str = None,
        relationship: str = None
    ) -> str:
        beneficiary_id = beneficiary_id or f"ben_{generate_unique_id()}"

        if not all([customer_id, beneficiary_name, country, bank_details]):
            return json.dumps({"error": "Missing required fields"}, indent=2)

        result = {
            "beneficiary_id": beneficiary_id,
            "customer_id": customer_id,
            "beneficiary_name": beneficiary_name,
            "country": country,
            "bank_details": bank_details,
            "status": "Active",
        }
        if beneficiary_type:
            result["beneficiary_type"] = beneficiary_type
        if relationship:
            result["relationship"] = relationship
        
        return json.dumps(result, indent=2)
        beneficiary_id = beneficiary_id or f"ben_{generate_unique_id()}"

        if not all([customer_id, beneficiary_name, country, bank_details]):
            return json.dumps({"error": "Missing required fields"}, indent=2)

        return json.dumps(
            {
                "beneficiary_id": beneficiary_id,
                "customer_id": customer_id,
                "beneficiary_name": beneficiary_name,
                "country": country,
                "bank_details": bank_details,
                "status": "Active",
            },
            indent=2,
        )
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RegisterNewBeneficiary",
                "description": "Add a new beneficiary to the customer's profile with validations.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer id"},
                        "beneficiary_name": {
                            "type": "string",
                            "description": "Beneficiary name",
                        },
                        "country": {"type": "string", "description": "Country"},
                        "bank_details": {
                            "type": "object",
                            "properties": {
                                "account_number": {"type": "string"},
                                "bank_name": {"type": "string"},
                                "routing_info": {"type": "string"},
                            },
                        },
                    },
                    "required": [
                        "customer_id",
                        "beneficiary_name",
                        "country",
                        "bank_details",
                    ],
                },
            },
        }
