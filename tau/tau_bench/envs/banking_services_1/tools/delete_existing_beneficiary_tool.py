# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteExistingBeneficiaryTool(Tool):
    """
    Tool to delete a registered beneficiary from a customer's profile.

    This tool checks whether the specified beneficiary exists and is associated
    with the given customer. If the match is found, the beneficiary is removed.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Deletes the beneficiary if it belongs to the customer.

        get_info() -> Dict[str, Any]:
            Returns structured information about expected input and tool purpose.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], beneficiary_id, customer_id) -> str:
        if not customer_id or not beneficiary_id:
            return json.dumps(
                {"error": "customer_id and beneficiary_id are required"}, indent=2
            )

        beneficiaries = load_json("beneficiaries.json")
        updated = [
            b
            for b in beneficiaries
            if not (
                b["beneficiary_id"] == beneficiary_id
                and b["customer_id"] == customer_id
            )
        ]

        if len(updated) == len(beneficiaries):
            return json.dumps(
                {"error": "Beneficiary not found or does not belong to customer"},
                indent=2,
            )

        return json.dumps(
            {"status": "deleted", "beneficiary_id": beneficiary_id}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_existing_beneficiary",
                "description": "Remove a beneficiary from the customer's account after validation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer ID"},
                        "beneficiary_id": {
                            "type": "string",
                            "description": "Beneficiary ID",
                        },
                    },
                    "required": ["customer_id", "beneficiary_id"],
                },
            },
        }
