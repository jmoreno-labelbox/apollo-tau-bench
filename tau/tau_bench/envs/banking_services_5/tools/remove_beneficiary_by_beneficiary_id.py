# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveBeneficiaryByBeneficiaryId(Tool):
    """Removes a beneficiary from the database using their beneficiary ID and customer ID for verification."""

    @staticmethod
    def invoke(data: Dict[str, Any], beneficiary_id, customer_id) -> str:

        if not customer_id or not beneficiary_id:
            return json.dumps({"error": "customer_id and beneficiary_id are required."}, indent=2)

        beneficiaries = list(data.get("beneficiaries", {}).values())
        for i, beneficiary in enumerate(beneficiaries):
            if (beneficiary.get("beneficiary_id") == beneficiary_id
                    and beneficiary.get("customer_id") == customer_id):
                del beneficiaries[i]
                return json.dumps({
                    "status": "Beneficiary removed successfully."
                }, indent=2)

        return json.dumps({"error": "Beneficiary not found for this customer."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_beneficiary_by_beneficiary_id",
                "description": "Removes a beneficiary from the database using the beneficiary ID and customer ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer who owns the beneficiary"
                        },
                        "beneficiary_id": {
                            "type": "string",
                            "description": "Unique ID of the beneficiary to be removed"
                        }
                    },
                    "required": ["customer_id", "beneficiary_id"]
                }
            }
        }
