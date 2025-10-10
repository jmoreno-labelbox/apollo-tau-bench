# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddNewBeneficiaryForCustomer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        for field in (
            "customer_id",
            "beneficiary_name",
            "beneficiary_type",
            "relationship",
            "bank_name",
        ):
            if not kwargs.get(field):
                return json.dumps({"error": f"{field} is required."}, indent=2)

        beneficiary_id = get_next_beneficiary_id()

        date_added = kwargs.get("date_added")
        if date_added is None:
            date_added = get_current_timestamp()

        account_details = {
            k: v
            for k, v in {
                "bank_name": kwargs.get("bank_name"),
                "account_number": kwargs.get("account_number"),
                "routing_number": kwargs.get("routing_number"),
                "ifsc_code": kwargs.get("ifsc_code"),
                "iban": kwargs.get("iban"),
                "bic_swift": kwargs.get("bic_swift"),
                "sort_code": kwargs.get("sort_code"),
                "bank_code": kwargs.get("bank_code"),
                "branch_code": kwargs.get("branch_code"),
            }.items()
            if v is not None
        }

        new_beneficiary = {
            "beneficiary_id": beneficiary_id,
            "customer_id": kwargs["customer_id"],
            "beneficiary_name": kwargs["beneficiary_name"],
            "beneficiary_type": kwargs["beneficiary_type"],
            "relationship": kwargs["relationship"],
            "account_details": account_details,
            "date_added": date_added,
        }

        data.setdefault("beneficiaries", []).append(new_beneficiary)
        return json.dumps(new_beneficiary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_new_beneficiary_for_customer",
                "description": (
                    "Adds a new beneficiary for a customer and returns the full beneficiary record. "
                    "Supports various global bank account formats."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string"},
                        "beneficiary_name": {"type": "string"},
                        "beneficiary_type": {"type": "string"},
                        "relationship": {"type": "string"},
                        "bank_name": {"type": "string"},
                        "account_number": {"type": "string"},
                        "routing_number": {"type": "string"},
                        "ifsc_code": {"type": "string"},
                        "iban": {"type": "string"},
                        "bic_swift": {"type": "string"},
                        "sort_code": {"type": "string"},
                        "bank_code": {"type": "string"},
                        "branch_code": {"type": "string"},
                        "date_added":  {"type": "string"},
                    },
                    "required": [
                        "customer_id",
                        "beneficiary_name",
                        "beneficiary_type",
                        "relationship",
                        "bank_name",
                        "date_added"
                    ],
                },
            },
        }
