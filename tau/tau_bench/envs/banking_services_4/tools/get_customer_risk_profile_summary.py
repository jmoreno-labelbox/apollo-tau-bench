# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCustomerRiskProfileSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get('customer_id')
        if not customer_id:
            return json.dumps({'error': 'customer_id is required'})
        customers = load_json('customers.json')
        customer = next((c for c in customers if c['customer_id'] == customer_id), None)
        if not customer:
            return json.dumps({'error': 'Customer not found'})
        summary = {
            'aml_risk_level': customer.get('compliance', {}).get('aml_risk_level'),
            'credit_score': customer.get('financial_profile', {}).get('credit_score'),
            'kyc_status': customer.get('compliance', {}).get('kyc_status')
        }
        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            'type': 'function',
            'function': {
                'name': 'get_customer_risk_profile_summary',
                'description': 'Retrieves AML risk level, credit score, and KYC status.',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'customer_id': {'type': 'string', 'description': 'Customer ID'}
                    },
                    'required': ['customer_id']
                }
            }
        }
