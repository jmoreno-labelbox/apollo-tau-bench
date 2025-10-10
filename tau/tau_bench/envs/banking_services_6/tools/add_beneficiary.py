# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddBeneficiary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        beneficiary_id = _get_next_beneficiary_id(data)
        new_beneficiary = {
                "beneficiary_id": beneficiary_id,
                "customer_id": kwargs.get("customer_id"),
                "beneficiary_name": kwargs.get("name"),
                "relationship": kwargs.get("relationship"),
                "account_details": {
                        "iban": kwargs.get("iban"),
                        "account_number": kwargs.get("account_number"),
                        "sort_code": kwargs.get("sort_code"),
                        "routing_number": kwargs.get("routing_number"),
                        "bank_name": kwargs.get("bank_name"),
                        "country": kwargs.get("country")
                },
                "date_added": NOW.strftime(DT_STR_FORMAT)
        }
        data['beneficiaries'].append(new_beneficiary)
        return json.dumps(new_beneficiary)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "add_beneficiary",
                        "description": "Adds a new beneficiary to a customer's profile.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string"}, "name": {"type": "string"}, "relationship": {"type": "string"},
                                        "iban": {"type": "string"},
                                        "account_number": {"type": "string"},
                                        "sort_code": {"type": "string"},
                                        "routing_number": {"type": "string"},
                                        "bank_name": {"type": "string"}, "country": {"type": "string"}
                                },
                                "required": ["customer_id", "name", "relationship", "iban", "bank_name", "country"]
                        }
                }
        }
