from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone, date, timedelta
import calendar
from typing import Any, Dict
import random

class AddNewBeneficiaryForCustomer(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        beneficiary_name: str,
        beneficiary_type: str,
        customer_id: str,
        relationship: str,
        account_number: str = None,
        bank_code: str = None,
        bank_name: str = None,
        bic_swift: str = None,
        branch_code: str = None,
        date_added: str = None,
        iban: str = None,
        ifsc_code: str = None,
        routing_number: str = None,
        sort_code: str = None
    ) -> str:
        for field in (
            "customer_id",
            "beneficiary_name",
            "beneficiary_type",
            "relationship",
            "bank_name",
        ):
            if not locals().get(field):
                return json.dumps({"error": f"{field} is required."}, indent=2)

        beneficiary_id = get_next_beneficiary_id()

        if date_added is None:
            date_added = get_current_timestamp()

        account_details = {
            k: v
            for k, v in {
                "bank_name": bank_name,
                "account_number": account_number,
                "routing_number": routing_number,
                "ifsc_code": ifsc_code,
                "iban": iban,
                "bic_swift": bic_swift,
                "sort_code": sort_code,
                "bank_code": bank_code,
                "branch_code": branch_code,
            }.items()
            if v is not None
        }

        new_beneficiary = {
            "beneficiary_id": beneficiary_id,
            "customer_id": customer_id,
            "beneficiary_name": beneficiary_name,
            "beneficiary_type": beneficiary_type,
            "relationship": relationship,
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
                "name": "AddNewBeneficiaryForCustomer",
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
