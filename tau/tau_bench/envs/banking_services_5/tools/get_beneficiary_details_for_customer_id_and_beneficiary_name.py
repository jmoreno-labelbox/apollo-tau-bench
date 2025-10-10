# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetBeneficiaryDetailsForCustomerIdAndBeneficiaryName(Tool):
    """Retrieves full details of a beneficiary using customer_id and beneficiary_name."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        beneficiary_name = kwargs.get("beneficiary_name", "").strip().lower()

        if not customer_id or not beneficiary_name:
            return json.dumps({
                "error": "Both customer_id and beneficiary_name are required."
            }, indent=2)

        beneficiaries = list(data.get("beneficiaries", {}).values())
        for beneficiary in beneficiaries:
            if (beneficiary.get("customer_id") == customer_id and
                beneficiary.get("beneficiary_name", "").strip().lower() == beneficiary_name):
                return json.dumps(beneficiary, indent=2)

        return json.dumps({"error": "Beneficiary not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_beneficiary_details_for_customer_id_and_beneficiary_name",
                "description": "Fetches the full details of a beneficiary using customer ID and beneficiary name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer who owns the beneficiary"
                        },
                        "beneficiary_name": {
                            "type": "string",
                            "description": "Full name of the beneficiary to match (case-insensitive)"
                        }
                    },
                    "required": ["customer_id", "beneficiary_name"]
                }
            }
        }
