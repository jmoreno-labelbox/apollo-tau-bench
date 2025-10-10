# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCustomerBeneficiariesTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get('customer_id')
        beneficiaries = list(data.get('beneficiaries', {}).values())

        customer_beneficiaries = []
        for beneficiary in beneficiaries:
            if beneficiary['customer_id'] == customer_id:
                bank_name = beneficiary.get('bank_name')
                if not bank_name and 'account_details' in beneficiary:
                    bank_name = beneficiary['account_details'].get('bank_name', 'N/A')

                customer_beneficiaries.append({
                    'beneficiary_id': beneficiary['beneficiary_id'],
                    'beneficiary_name': beneficiary['beneficiary_name'],
                    'bank_name': bank_name or 'N/A',
                    'status': beneficiary.get('status', 'Active'),
                    'date_added': beneficiary.get('date_added', 'N/A')
                })

        return json.dumps(customer_beneficiaries, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_customer_beneficiaries",
                "description": "Get all beneficiaries for a customer",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer identifier"}
                    },
                    "required": ["customer_id"]
                }
            }
        }
