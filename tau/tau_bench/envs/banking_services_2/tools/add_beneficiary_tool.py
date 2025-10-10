# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddBeneficiaryTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get('customer_id')
        beneficiary_name = kwargs.get('beneficiary_name')
        account_number = kwargs.get('account_number')
        routing_number = kwargs.get('routing_number')
        bank_name = kwargs.get('bank_name')

        beneficiaries = list(data.get('beneficiaries', {}).values())

        beneficiary_id = f"ben_{generate_unique_id()}"

        new_beneficiary = {
            "beneficiary_id": beneficiary_id,
            "customer_id": customer_id,
            "beneficiary_name": beneficiary_name,
            "account_number": account_number,
            "routing_number": routing_number,
            "bank_name": bank_name,
            "status": "Active",
            "date_added": get_current_timestamp()
        }

        beneficiaries.append(new_beneficiary)

        return json.dumps({
            "beneficiary_id": beneficiary_id,
            "beneficiary_name": beneficiary_name,
            "status": "Active",
            "date_added": new_beneficiary["date_added"]
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_beneficiary",
                "description": "Add a new payment beneficiary",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer identifier"},
                        "beneficiary_name": {"type": "string", "description": "Name of beneficiary"},
                        "account_number": {"type": "string", "description": "Beneficiary account number"},
                        "routing_number": {"type": "string", "description": "Bank routing number"},
                        "iban": {"type": "string", "description": "Iban routing number"},
                        "bank_name": {"type": "string", "description": "Bank name"},
                        "sort_code": {"type": "string", "description": "Sort_code routing number"}
                    },
                    "required": ["customer_id", "beneficiary_name", "bank_name"]
                }
            }
        }
